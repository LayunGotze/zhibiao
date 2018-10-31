# encoding:utf-8

import MySQLdb
import time
import re


class CapPrbDic():

    dic = {}

    def __init__(self, filename):

        # super(CapPrbDic, self).__init__()
        for line in open(filename):
            words = line.strip().split('\t')
            self.dic[words[0]] = float(words[3])
#返回这个单词大写的概率，如果找不到这个单词就默认返回大写概率是1
    def getPrb(self, word):
        if self.dic.has_key(word):
            return self.dic[word]
        return 1


class LocNameDic():

    def __init__(self):
        # super(LocNameDic, self).__init__()
        try:
            # self.conn = MySQLdb.connect(user='root', passwd='hfrhfr', host='localhost', db='source',unix_socket='/data/mysql/mysql.sock')
            # self.conn = MySQLdb.connect(user='root', passwd='19910101', host='localhost', db='loc')
            self.conn = MySQLdb.connect(user='rock', passwd='19910101', host='192.168.1.137', db='loc')
            # self.conn = MySQLdb.connect(user='zhou', passwd='19910101', host='localhost', db='loc')
            #
            # self.conn = MySQLdb.connect(user='zhou', passwd='19910101', host='192.168.1.151', db='loc')
            self.cur = self.conn.cursor()
        except Exception as e:
            print('SQL ERROR: (__init__) ' + str(e))

    def getByUfi(self, ufi):
        try:
            re = []
            # Select from GNS
            sql = 'SELECT `id`,`full_name_nd_ro`,`sort_name_ro`,`cc1`,`adm1`,`lat`,`long`,`dsg`,`nt`,`ufi` FROM gns WHERE ufi = \'' + str(
                ufi) + '\' and nt = \'C\''
            self.cur.execute(sql)
            for x in self.cur.fetchall():
                tmp = dict(
                    zip(['id', 'full_name', 'search_name', 'adm1', 'adm2', 'lat', 'long', 'type', 'nt', 'feature_id'],
                        x))

                tmp['admLevel'] = self.gnsDsg2AdmLevel(tmp)
                tmp['level'] = self.gnsDsg2level(tmp)
                if tmp['type'] == 'ADM1' or tmp['type'] == 'PPLA' or tmp['type'] == 'PCLI':
                    tmp['isBigCity'] = True
                else:
                    tmp['isBigCity'] = False
                del tmp['type']
                re.append(tmp)

            return re
        except Exception as e:
            print('SQL ERROR: (getByUfi) ' + str(e))

#参数：fetchAll后的数据,从[[],[],...]转换成[{},{},...]
    def get_gnsdata(self, mysqldata):
        gns_data = []
        for x in mysqldata:
            #这里的type指的是DSG的等级，ADM1其实是数据库cc1，adm2其实是数据库中adm1
            tmp = dict(
                zip(['id', 'full_name', 'search_name', 'adm1', 'adm2', 'lat', 'long','fc','type', 'nt', 'feature_id'], x))

            tmp['admLevel'] = self.gnsDsg2AdmLevel(tmp)#仅使用dsg的等级评级，越小约好
            tmp['level'] = self.gnsDsg2level(tmp)#使用dsg+nt的评级，越大越好
            if tmp['type'] == 'ADM1' or tmp['type'] == 'PPLA' or tmp['type'] == 'PCLI':
                #标记是否为大城市，大城市在后面的消歧有用
                tmp['isBigCity'] = True
            else:
                tmp['isBigCity'] = False
            #删除了字典中的type元素
            # del tmp['type']
            gns_data.append(tmp)
        return gns_data

    def get_gnisdata(self, mysqldata):
        gnis_data = []
        for x in mysqldata:
            tmp = dict(zip(['id', 'full_name', 'search_name', 'adm2', 'lat', 'long', 'feature_id', 'county_name'], x))
            tmp['adm1'] = 'US'
            tmp['admLevel'] = self.gnisName2AdmLevel(tmp['full_name'], tmp['county_name'])#越小越好，1.2.5
            #*10是对应gns那边的level1和2的等级，+6是对应gns那边nt=n的一般情况
            tmp['level'] = (6 - tmp['admLevel'])*10+6#越高约好
            if self.gnisFc(tmp['full_name'], tmp['county_name']):
                tmp['fc'] = 'A'
            else:
                tmp['fc'] = 'P'
            if tmp['admLevel'] <= 1:
                tmp['isBigCity'] = True
            else:
                tmp['isBigCity'] = False
            del tmp['county_name']
            gnis_data.append(tmp)
        return gnis_data

    #结合数据库查询结果获取标准格式结果，参数为：词，23表，32表
    def direct_get(self, word, two_thr_code, thr_two_code):
        re = []
        #isupper:方法检测字符串中所有的字母是否都为大写
        #如果搜索的地名是国家
        if word.isupper() and (word in two_thr_code.keys() or word in thr_two_code.keys()):
            if word in two_thr_code.keys():
                two_code = word
            elif word in thr_two_code.keys():
                two_code = thr_two_code[word]
            try:
                sql = 'SELECT `id`,`full_name_nd_ro`,`sort_name_ro`,`cc1`,`adm1`,`lat`,`long`,`fc`,`dsg`,`nt`,`ufi`\
                    FROM gns WHERE cc1 = \'' + two_code + '\' AND dsg = "PCLI" '
                self.cur.execute(sql)
                gnsdata = self.cur.fetchall()
                tmp = self.get_gnsdata(gnsdata)
                #extend：函数用于在列表末尾一次性追加另一个序列中的多个值
                re.extend(tmp)
            except Exception as e:
                print('SQL direct_countrycode from gns ERROR: (get) ' + str(e))
            return re
        else:
            try:
                sql = 'SELECT `id`,`full_name_nd_ro`,`sort_name_ro`,`cc1`,`adm1`,`lat`,`long`,`fc`,`dsg`,`nt`,`ufi`\
                    FROM gns WHERE full_name_nd_ro = \''+ word +'\''
                self.cur.execute(sql)
                gnsdata = self.cur.fetchall()
                tmp = self.get_gnsdata(gnsdata)
                re.extend(tmp)

                # sql = 'SELECT `id`,`feature_name`,`search_name`,`state_numeric`,`prim_lat_dec`,`prim_long_dec`,`feature_id`,`county_name` \
				# FROM gnis WHERE  feature_name = \'' + word + '\' '
                #这里修改成使用search_name进行搜索,首先消除空格，然后全部转换成大写进行搜索
                tmp_search_name = word.replace(" ","")
                tmp_search_name = tmp_search_name.upper()
                # sql = 'SELECT `id`,`feature_name`,`search_name`,`state_numeric`,`prim_lat_dec`,`prim_long_dec`,`feature_id`,`county_name` \
				# # FROM gnis WHERE  search_name = \'' + tmp_search_name + '\' '
                sql = 'SELECT `id`,`feature_name`,`search_name`,`state_numeric`,`prim_lat_dec`,`prim_long_dec`,`feature_id`,`county_name` \
				FROM gnis WHERE  search_name = \'' + tmp_search_name + '\' '
                self.cur.execute(sql)
                gnisdata = self.cur.fetchall()
                tmp = self.get_gnisdata(gnisdata)
                re.extend(tmp)
            except Exception as e:
                print('SQL direct_countrycode from gnis ERROR: (get) ' + str(e))
            return re

    #分别从美国和非美国的地理数据库中查询并拼接结果到一个数据集中，然后返回
    def get(self, word):
        re = []
        try:
            # Select from GNS
            # select word%
            sql = 'SELECT `id`,`full_name_nd_ro`,`sort_name_ro`,`cc1`,`adm1`,`lat`,`long`,`fc`,`dsg`,`nt`,`ufi` \
              FROM gns WHERE full_name_nd_ro LIKE \'' + word + ' %' + '\''
            self.cur.execute(sql)
            gnsdata = self.cur.fetchall()
            tmp = self.get_gnsdata(gnsdata)
            re.extend(tmp)
            # select %word
            sql = 'SELECT `id`,`full_name_nd_ro`,`sort_name_ro`,`cc1`,`adm1`,`lat`,`long`,`fc`,`dsg`,`nt`,`ufi` \
                FROM gns WHERE full_name_nd_ro_reverse LIKE reverse(\'' + '% ' + word + '\')'
            self.cur.execute(sql)
            gnsdata = self.cur.fetchall()
            tmp = self.get_gnsdata(gnsdata)
            re.extend(tmp)

            # Select from gnis
            # select word%
            sql = 'SELECT `id`,`feature_name`,`search_name`,`state_numeric`,`prim_lat_dec`,`prim_long_dec`,`feature_id`,`county_name` \
				FROM gnis WHERE  feature_name LIKE \'' + word + ' %' + '\''
            self.cur.execute(sql)
            gnisdata = self.cur.fetchall()
            tmp = self.get_gnisdata(gnisdata)
            re.extend(tmp)
            # select %word
            sql = 'SELECT `id`,`feature_name`,`search_name`,`state_numeric`,`prim_lat_dec`,`prim_long_dec`,`feature_id`,`county_name` \
				FROM gnis WHERE  feature_name_reverse LIKE reverse(\'' + '% '+ word + '\')'
            self.cur.execute(sql)
            gnisdata = self.cur.fetchall()
            tmp = self.get_gnisdata(gnisdata)
            re.extend(tmp)
        except Exception as e:
            print('SQL ERROR: (get) ' + str(e))
        return re

    def test(self):
        try:
            sql = 'SELECT `id`,`full_name`,`search_name`,`adm1`,`adm2`,`lat`,`long`,`level`,`source_id` FROM loc WHERE search_name = \'' + word.upper() + '\''

            re = []
            for x in self.cur.execute(sql):
                re.append(
                    dict(zip(['id', 'full_name', 'search_name', 'adm1', 'adm2', 'lat', 'long', 'level', 'loc_id'], x)))
            return re
        except Exception as e:
            print('SQL ERROR: (test) ' + str(e))

#返回DSG标记，ADM1是一级行政区，ADM2是二级行政区。。。
    def gnsDsg2AdmLevel(self, loc):
        if loc['type'] == 'PCLI':  # 如果是国家
            return 0
        if loc['type'] == 'ADM1':
            return 1
        if loc['type'] == 'AMD2':
            return 2
        if loc['type'] == 'ADM3':
            return 3
        if loc['type'] == 'ADM4':
            return 4
        return 5

    def gnsDsg2level(self, loc):
        ntl = 0
        if loc['nt'] == 'C':
            ntl = 7
        elif loc['nt'] == 'N':
            ntl = 6
        elif loc['nt'] == 'D':
            ntl = 5
        elif loc['nt'] == 'P':
            ntl = 3
        elif loc['nt'] == 'VA':
            ntl = 2
        elif loc['nt'] == 'V':
            ntl = 1

        if loc['type'] == 'PCLI':
            return 80 + ntl
        if loc['type'] == 'ADM1' or loc['type'] == 'PPLA' or loc['type'] == 'PPLC':
            return 50 + ntl
        if loc['type'] == 'AMD2' or loc['type'] == 'PPL2':
            return 40 + ntl
        if loc['type'] == 'ADM3' or loc['type'] == 'PPL3':
            return 30 + ntl
        if loc['type'] == 'ADM4' or loc['type'] == 'PPL4':
            return 20 + ntl
        return 10 + ntl

    def gnisName2AdmLevel(self, full_name, county_name):
        USStateNames = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware',
                        'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky',
                        'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi',
                        'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New hampshire', 'New jersey', 'New mexico',
                        'New york', 'North carolina', 'North dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania',
                        'Rhode island', 'South carolina', 'South dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont',
                        'Virginia', 'Washington', 'West virginia', 'Wisconsin', 'Wyoming']
        if (full_name in USStateNames):
            return 1

        if (full_name == county_name):
            return 2

        return 5

    #判定区域等级是否等价于gns的fc=A
    def gnisFc(self,full_name, county_name):
        USStateNames = ['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware',
                        'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky',
                        'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi',
                        'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New hampshire', 'New jersey', 'New mexico',
                        'New york', 'North carolina', 'North dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania',
                        'Rhode island', 'South carolina', 'South dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont',
                        'Virginia', 'Washington', 'West virginia', 'Wisconsin', 'Wyoming']
        if (full_name in USStateNames):
            return True

        if (full_name == county_name):
            return True
        #我们并不能很好的判定美国地名是否为fc=A,只能令其都等于A了
        return True

###############################################################
# Tools
###############################################################

def tidyLocName(word):
    re = ''
    for x in word.lower():
        if str.isalpha(x):
            re += x
    return re


#旧的次函数有bug，是不安全的
# def list2string(words):
#     l = len(words)
#     if len(words) == 2 and len(words[0] + words[1]) <= 4:
#         return words[0] + ' ' + words[1]
#
#     re = ''
#     for x in words:
#         re += x
#         re += ' '
#     re = re.strip()
#     return re

#修正后的
def list2string(words):

    if isinstance(words,list):
        if len(words) == 1:
            return words[0]
        else:
            return words[0] + ' ' + words[1]

    return words
