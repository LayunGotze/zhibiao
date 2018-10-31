# encoding:utf-8

import os

import actuator
import data


class LocationRecoganizer():
    dictdir = os.path.dirname(os.path.realpath(__file__))
    countrycode_path = dictdir + "/data/country_code.txt"
    F_CAP_PRB_DIC = dictdir + "/data/d-cap-pro.txt"

    def __init__(self):

        self.two_thr_code = self.__read_countrycode(self.countrycode_path)  # key is two code
        #形成键值和two_thr_code正好相反的字典
        self.thr_two_code = {value: key for key, value in self.two_thr_code.items()}  # key is three code
        #大写字母出现的概率
        #在维基百科中，对首字母大写的词出现的频率进行的统计，因为首字母大写一般是专有名词，视为更重要
        self.capPrbDic = data.CapPrbDic(self.F_CAP_PRB_DIC)
        #获得连接到数据库的句柄
        self.locNameDic = data.LocNameDic()

    #将country_code.txt的内容转换为字典
    def __read_countrycode(self, countrycode_path):
        filein = open(countrycode_path, 'r')
        code_dict = {}
        for line in filein.readlines():
            line = line.strip()
            #\t -> tab
            codes = line.split('\t')
            code_dict[codes[0]] = codes[1]
        return code_dict

#识别
    def recoganize(self, data):
        locations = actuator.recognize(data, self.locNameDic, self.capPrbDic, self.two_thr_code, self.thr_two_code)

        re = []
        for i in xrange(0, len(data)):
            re.append([])

        for i in xrange(0, len(locations)):
            #centence_id?->sentence_id
            tmp = int(locations[i]['centence_id'])
            del locations[i]['centence_id']
            re[tmp].append(self.converter(locations[i]))
        return re

#转换器，对输出格式的转换
    def converter(self, loc):
        # if( loc['adm1'] in self.countryCodeConverter.keys() ):
        # 	loc['adm1'] = self.countryCodeConverter[ loc['adm1'] ]
        # else:
        # 	return None
        if loc['adm1'] in self.two_thr_code:
            loc['adm1'] = self.two_thr_code[loc['adm1']]
        loc['lat'] = (float)(loc['lat'])
        loc['long'] = (float)(loc['long'])
        if loc.has_key('full_name'):
            loc['geoname'] = loc['full_name']
            del loc['full_name']
        if loc.has_key('admLevel'):
            loc['level'] = loc['admLevel']
            del loc['admLevel']

        if loc.has_key('search_name'):
            del loc['search_name']
        if loc.has_key('id'):
            del loc['id']

        if loc.has_key('feature_id'):
            loc['ufi'] = (float)(loc['feature_id'])
            del loc['feature_id']

        return loc

#################################################
#################################################
