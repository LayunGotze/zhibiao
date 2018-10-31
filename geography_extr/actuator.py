# encoding:utf-8
from decimal import Decimal

import data
import time
from GeoTools import GeoTools

__DEBUG__ = False

#美国州表:
#注意，key使用了去掉空格全小写的格式
US_STATE={
	'alabama':{
		'ufi': '158174.0',
		'lat': Decimal('33.5206608'),
		'adm2': '01',
		'level': 1,
		'geoname': 'Alabama',
		'long': Decimal('-86.80249'),
		'adm1': 'US'
	},
	'alaska':{
		'ufi': '1398242.0',
		'lat': Decimal('61.2180556'),
		'adm2': '02',
		'level': 1,
		'geoname': 'Alaska',
		'long': Decimal('-149.9002778'),
		'adm1': 'US'
	},
	'arizona':{
		'ufi': '44784.0',
		'lat': Decimal('33.4483771'),
		'adm2': '04',
		'level': 1,
		'geoname': 'Arizona',
		'long': Decimal('-112.0740373'),
		'adm1': 'US'
	},
	'arkansas':{
		'ufi': '76914.0',
		'lat': Decimal('36.0625795'),
		'adm2': '05',
		'level': 1,
		'geoname': 'Arkansas',
		'long': Decimal('-94.1574263'),
		'adm1': 'US'
	},
	'california':{
		'ufi': '1662328.0',
		'lat': Decimal('34.0522342'),
		'adm2': '06',
		'level': 1,
		'geoname': 'California',
		'long': Decimal('-118.2436849'),
		'adm1': 'US'
	},
	'colorado':{
		'ufi': '201738.0',
		'lat': Decimal('39.7391536'),
		'adm2': '08',
		'level': 1,
		'geoname': 'Colorado',
		'long': Decimal('-104.9847034'),
		'adm1': 'US'
	},
	'connecticut':{
		'ufi': '213160.0',
		'lat': Decimal('41.7637111'),
		'adm2': '09',
		'level': 1,
		'geoname': 'Connecticut',
		'long': Decimal('-72.6850932'),
		'adm1': 'US'
	},
	'delaware':{
		'ufi': '217882.0',
		'lat': Decimal('39.158168'),
		'adm2': '10',
		'level': 1,
		'geoname': 'Delaware',
		'long': Decimal('-75.5243682'),
		'adm1': 'US'
	},
	'florida':{
		'ufi': '288240.0',
		'lat': Decimal('28.5383355'),
		'adm2': '12',
		'level': 1,
		'geoname': 'Florida',
		'long': Decimal('-81.3792365'),
		'adm1': 'US'
	},
	'Georgia':{
		'ufi': '351615.0',
		'lat': Decimal('33.7489954'),
		'adm2': '13',
		'level': 1,
		'geoname': 'Georgia',
		'long': Decimal('-84.3879824'),
		'adm1': 'US'
	},
	'hawaii':{
		"ufi": '359331.0',
		'lat': Decimal('19.5541667'),
		'adm2': '15',
		'level': 1,
		'geoname': 'Hawaii',
		'long': Decimal('-154.89'),
		'adm1': 'US'
	},
	'idaho':{
		"ufi": '400590.0',
		'lat': Decimal('43.6135002'),
		'adm2': '16',
		'level': 1,
		'geoname': 'Idaho',
		'long': Decimal('-116.2034505'),
		'adm1': 'US'
	},
	'illinois':{
		'ufi': '426595.0',
		'lat': Decimal('39.8017171'),
		'adm2': '17',
		'level': 1,
		'geoname': 'Illinois',
		'long': Decimal('-89.6437107'),
		'adm1': 'US'
	},
	'indiana':{
		'ufi': '452890.0',
		'lat': Decimal('39.7683765'),
		'adm2': '18',
		'level': 1,
		'geoname': 'Indiana',
		'long': Decimal('-86.1580423'),
		'adm1': 'US'
	},
	'iowa':{
		'ufi': '465961.0',
		'lat': Decimal('41.6005448'),
		'adm2': '19',
		'level': 1,
		'geoname': 'Iowa',
		'long': Decimal('-93.6091064'),
		'adm1': 'US'
	},
	'kansas':{
		'ufi': '473862.0',
		'lat': Decimal('37.6922361'),
		'adm2': '20',
		'level': 1,
		'geoname': 'Kansas',
		'long': Decimal('-97.3375448'),
		'adm1': 'US'
	},
	'kentucky':{
		'ufi': '496343.0',
		'lat': Decimal('37.9886892'),
		'adm2': '21',
		'level': 1,
		'geoname': 'Kentucky',
		'long': Decimal('-84.4777153'),
		'adm1': 'US'
	},
	'louisiana':{
		'ufi': '1629985.0',
		'lat': Decimal('29.9546482'),
		'adm2': '22',
		'level': 1,
		'geoname': 'Louisiana',
		'long': Decimal('-90.075072'),
		'adm1': 'US'
	},
	'maine':{
		'ufi': '573692.0',
		'lat': Decimal('43.661471'),
		'adm2': '23',
		'level': 1,
		'geoname': 'Maine',
		'long': Decimal('-70.2553259'),
		'adm1': 'US'
	},
	'maryland':{
		'ufi': '597040.0',
		'lat': Decimal('39.2903848'),
		'adm2': '24',
		'level': 1,
		'geoname': 'Maryland',
		'long': Decimal('-76.6121893'),
		'adm1': 'US'
	},
	'massachusetts':{
		'ufi': '617565.0',
		'lat': Decimal('42.3584308'),
		'adm2': '25',
		'level': 1,
		'geoname': 'Massachusetts',
		'long': Decimal('-71.0597732'),
		'adm1': 'US'
	},
	'michigan':{
		'ufi': '1617959.0',
		'lat': Decimal('42.331427'),
		'adm2': '26',
		'level': 1,
		'geoname': 'Michigan',
		'long': Decimal('-83.0457538'),
		'adm1': 'US'
	},
	'minnesota':{
		'ufi': '655030.0',
		'lat': Decimal('44.9799654'),
		'adm2': '27',
		'level': 1,
		'geoname': 'Minnesota',
		'long': Decimal('-93.2638361'),
		'adm1': 'US'
	},
	'mississippi':{
		'ufi': '711543.0',
		'lat': Decimal('32.2987573'),
		'adm2': '28',
		'level': 1,
		'geoname': 'Mississippi',
		'long': Decimal('-90.1848103'),
		'adm1': 'US'
	},
	'missouri':{
		'ufi': '716133.0',
		'lat': Decimal('38.9517053'),
		'adm2': '29',
		'level': 1,
		'geoname': 'Missouri',
		'long': Decimal('-92.3340724'),
		'adm1': 'US'
	},
	'montana':{
		'ufi': '803919.0',
		'lat': Decimal('46.4615982'),
		'adm2': '30',
		'level': 1,
		'geoname': 'Montana',
		'long': Decimal('-112.2472323'),
		'adm1': 'US'
	},
	'nebraska':{
		'ufi': '835483.0',
		'lat': Decimal('41.2586096'),
		'adm2': '31',
		'level': 1,
		'geoname': 'Nebraska',
		'long': Decimal('-95.937792'),
		'adm1': 'US'
	},
	'nevada':{
		'ufi': '847272.0',
		'lat': Decimal('40.7138067'),
		'adm2': '32',
		'level': 1,
		'geoname': 'Nevada',
		'long': Decimal('-116.1039663'),
		'adm1': 'US'
	},
	'newhampshire':{
		'ufi': '868243.0',
		'lat': Decimal('42.9956397'),
		'adm2': '33',
		'level': 1,
		'geoname': 'New hampshire',
		'long': Decimal('-71.4547891'),
		'adm1': 'US'
	},
	'newjersey':{
		'ufi': '881466.0',
		'lat': Decimal('39.4862267'),
		'adm2': '34',
		'level': 1,
		'geoname': 'New jersey',
		'long': Decimal('-75.0257313'),
		'adm1': 'US'
	},
	'newmexico':{
		'ufi': '928679.0',
		'lat': Decimal('35.0844909'),
		'adm2': '35',
		'level': 1,
		'geoname': 'New mexico',
		'long': Decimal('-106.6511367'),
		'adm1': 'US'
	},
	'newyork':{
		'ufi': '975772.0',
		'lat': Decimal('40.7142691'),
		'adm2': '36',
		'level': 1,
		'geoname': 'New york',
		'long': Decimal('-74.0059729'),
		'adm1': 'US'
	},
	'northcarolina':{
		'ufi': '1020557.0',
		'lat': Decimal('36.0726355'),
		'adm2': '37',
		'level': 1,
		'geoname': 'North carolina',
		'long': Decimal('-79.7919754'),
		'adm1': 'US'
	},
	'northdakota':{
		'ufi': '1035849.0',
		'lat': Decimal('46.8083268'),
		'adm2': '38',
		'level': 1,
		'geoname': 'North dakota',
		'long': Decimal('-100.7837392'),
		'adm1': 'US'
	},
	'ohio':{
		'ufi': '1080996.0',
		'lat': Decimal('39.9611755'),
		'adm2': '39',
		'level': 1,
		'geoname': 'Ohio',
		'long': Decimal('-82.9987942'),
		'adm1': 'US'
	},
	'oklahoma':{
		'ufi': '1095903.0',
		'lat': Decimal('35.2225668'),
		'adm2': '40',
		'level': 1,
		'geoname': 'Oklahoma',
		'long': Decimal('-97.4394777'),
		'adm1': 'US'
	},
	'oregon':{
		'ufi': '1137914.0',
		'lat': Decimal('44.0581728'),
		'adm2': '41',
		'level': 1,
		'geoname': 'Oregon',
		'long': Decimal('-121.3153096'),
		'adm1': 'US'
	},
	'pennsylvania':{
		'ufi': '1213649.0',
		'lat': Decimal('40.2737002'),
		'adm2': '42',
		'level': 1,
		'geoname': 'Pennsylvania',
		'long': Decimal('-76.8844179'),
		'adm1': 'US'
	},
	'rhodeisland':{
		'ufi': '1219851.0',
		'lat': Decimal('41.8239891'),
		'adm2': '44',
		'level': 1,
		'geoname': 'Rhode island',
		'long': Decimal('-71.4128343'),
		'adm1': 'US'
	},
	'southcarolina':{
		'ufi': '1247113.0',
		'lat': Decimal('34.2465393'),
		'adm2': '45',
		'level': 1,
		'geoname': 'South carolina',
		'long': Decimal('-80.6070238'),
		'adm1': 'US'
	},
	'southdakota':{
		'ufi': '1266887.0',
		'lat': Decimal('44.3683156'),
		'adm2': '46',
		'level': 1,
		'geoname': 'South dakota',
		'long': Decimal('-100.3509665'),
		'adm1': 'US'
	},
	'tennessee':{
		'ufi': '1652484.0',
		'lat': Decimal('36.1658899'),
		'adm2': '47',
		'level': 1,
		'geoname': 'Tennessee',
		'long': Decimal('-86.7844432'),
		'adm1': 'US'
	},
	'texas':{
		'ufi': '1380947.0',
		'lat': Decimal('32.725409'),
		'adm2': '48',
		'level': 1,
		'geoname': 'Texas',
		'long': Decimal('-97.3208496'),
		'adm1': 'US'
	},
	'utah':{
		'ufi': '1431487.0',
		'lat': Decimal('32.725409'),
		'adm2': '49',
		'level': 1,
		'geoname': 'Utah',
		'long': Decimal('-97.3208496'),
		'adm1': 'US'
	},
	'vermont':{
		'ufi': '1461834.0',
		'lat': Decimal('44.2600593'),
		'adm2': '50',
		'level': 1,
		'geoname': 'Vermont',
		'long': Decimal('-72.5753869'),
		'adm1': 'US'
	},
	'virginia':{
		'ufi': '1390022.0',
		'lat': Decimal('37.2279279'),
		'adm2': '51',
		'level': 1,
		'geoname': 'Virginia',
		'long': Decimal('-77.4019267'),
		'adm1': 'US'
	},
	'washington':{
		'ufi': '531871.0',
		'lat': Decimal('38.8951118'),
		'adm2': '11',
		'level': 1,
		'geoname': 'Washington',
		'long': Decimal('-77.0363658'),
		'adm1': 'US'
	},
	'westvirginia':{
		'ufi': '1558347.0',
		'lat': Decimal('38.3498195'),
		'adm2': '54',
		'level': 1,
		'geoname': 'West virginia',
		'long': Decimal('-81.6326235'),
		'adm1': 'US'
	},
	'wisconsin':{
		'ufi': '1576325.0',
		'lat': Decimal('44.9591352'),
		'adm2': '55',
		'level': 1,
		'geoname': 'Wisconsin',
		'long': Decimal('-89.6301221'),
		'adm1': 'US'
	},
	'wyoming':{
		'ufi': '1586424.0',
		'lat': Decimal('42.866632'),
		'adm2': '56',
		'level': 1,
		'geoname': 'Wyoming',
		'long': Decimal('-106.313081'),
		'adm1': 'US'
	},
	'unitedstates':{
		'ufi': '12145993.0',
		'lat': Decimal('39.216667'),
		'adm2': '00',
		'level': 0,
		'geoname': 'United States of America',
		'long': Decimal('-98.55'),
		'adm1': 'USA'
	},
	#可以从这里开始尝试手工添加一个白名单以纠正数据库缺陷
	'england':{
		'ufi': '-1766525.0',
		'lat': Decimal('52.216667'),
		'adm2': '07',
		'level': 5,
		'geoname': 'England',
		'long': Decimal('0.033333'),
		'adm1': 'GBR'
	}
}





# 获取候选结果
# def recognize(txt, capPrbDic, locNameDic):
#参数为：输入文本，数据库句柄，大写字母出现概率，23表，32表
def recognize(txt, locNameDic, capPrbDic, two_thr_code, thr_two_code):
	time1 = time.time()
	if __DEBUG__:
		_last_time_stamp = time.time()

	# 预处理，整理一下格式
	locations = []
	import Geo_dic

	for i in range(0, len(txt)):
		for x in txt[i]:
			# #查询是否是黑名单的词
			# sql = "SELECT COUNT(black_name) FROM blacklist WHERE black_name = '" + x[1].upper()+"'"
			# try:
			# 	# 执行SQL语句
			# 	locNameDic.cur.execute(sql)
			# 	# 获取所有记录列表
			# 	black_num = locNameDic.cur.fetchall()[0][0]
			# 	#如果确实在黑名单中
			# 	if black_num > 0:
			# 		continue
			# except:
			# 	print "Error: unable to query blacklist correctly"
			locations.append({
				'word': x[1],
				'offset': x[0],
				'centence_id': i
			})
			#检测是否为美国州名,是的话直接从美国州表中获得数据
			str = x[1].replace(" ","")
			str = str.lower()
			if str in US_STATE.keys():
				index = len(locations)
				us_cnds = []
				us_cnds.append(US_STATE[str])
				locations[index-1]['cnds'] = us_cnds



	# 获取信息
	for i in xrange(0, len(locations)):
		# 因为有可能会从location中删除词语，所以每次循环都要多个判断
		if i == len(locations):
			break
		cnds = []
		#不理解，感觉此处while可以去掉
		while len(cnds) == 0:
			words = locations[i]['word']
			try:
				# cnds = locNameDic.get( data.list2string(words) )
				cnds = locNameDic.direct_get(words, two_thr_code, thr_two_code)
			except Exception as e:
				cnds = []
			if len(cnds) != 0:
				# 如果能查到结果
				# locations[i][ 'word' ] = data.list2string(words)
				locations[i]['word'] = words
				#如果美国州名，则已有cnds，不要覆盖
				if locations[i].has_key('cnds'):
					cnds = locations[i]['cnds']
				else:
					locations[i]['cnds'] = cnds
				break
			# continue
			#如果没有查询到结果就尝试分割words，用空格
			words = locations[i]['word'].split(' ')
			#list长度大于1说明words有多于1个单词
			while len(words) > 1:
				if len(cnds) != 0:
					# 如果能查到结果
					# locations[i]['word'] = data.list2string(words)
					# locations[i]['cnds'] = cnds
					break
				else:
					#留下大写概率最高的
					#注意大小写统计表中都是小写，所以我们查询的时候也是需要使用小写.lower()
					if capPrbDic.getPrb(words[0].lower()) < capPrbDic.getPrb(words[-1].lower()):
						locations[i]['offset'] += len(words[0]) + 1
						#从第二个元素开始截取
						words = words[1:]
					else:
						#截取到倒数第一个元素
						words = words[:-1]
				cnds = locNameDic.direct_get(data.list2string(words), two_thr_code, thr_two_code)

			if len(cnds) != 0:
				break
			#执行到这里的时候意味着words只剩一个单词且仍可能没结果，或者提前找到了结果（此时words可能不为一个单词）
			try:
				#如果直接查找、分割单词后查找都没有找到，那么尝试模糊查询
				#尝试查询word的地理位置并把结果合并到cnds（暂时理解为总结果集）中去
				cnds.extend(locNameDic.get(locations[i]['word']))
				break
			except Exception as e:
				break
		if len(cnds) != 0:
			#这里的含义就是：location集合对应所有的地理名词的集合，每个地理名词有一个cnd（查询数据库看有没有的结果的集合）
			locations[i]['cnds'] = cnds
			#words可能是分割后的，所以更新下
			locations[i]['word'] = data.list2string(words)

	# 过滤(把有查询结果的过滤出来，删除过滤没有结果的
	locations = filter(lambda x: x.has_key('cnds'), locations)

	# 消歧,即消除含有多个结果的
	res = []


	#old
	# 标记出来不需要消歧的地名，包括只有一个候选结果的、和大城市

	# for i in xrange(0, len(locations)):
	#     # 如果有大城市候选项的化，放弃小城市
	#     bigCndsNum = 0
	#     for j in xrange(0, len(locations[i]['cnds'])):
	#         if locations[i]['cnds'][j]['isBigCity'] == True:
	#             bigCndsNum += 1
	#     if bigCndsNum >= 1:
	#         locations[i]['cnds'] = filter(lambda x: x['isBigCity'] == True, locations[i]['cnds'])
	#
	#     # 只有一个候选结果的
	#     if len(locations[i]['cnds']) == 1:
	#         locations[i]['isDisamb'] = True
	#     else:
	#         locations[i]['isDisamb'] = False


	############################################################
	#--------------------------消歧部分--------------------------
	############################################################
	#1、确定是否是国家的分歧，是的话单独处理，不是国家的话->2
	#主要思路：【如果黑名单希望屏蔽国家等级的区域，屏蔽DSG=pcli即可】
	#2、筛选fc=A的地区，如果消歧不完全->2.5【ps：如果结果有fc=A，但是全是美国的，则依旧回滚并执行->2.5，即无视】
	#2.5、选取level在某个阈值[50]之上的地名,没有->3，有一个->消岐结束，如有多个->回滚，3
	#3、通过行政区划之间的关系评分score，筛选出最高分，如果存在多个最高分，选取level最高的，如果有多个最高的执行第四->4
	#4、执行地理空间距离的消歧算法
	############################################################

	#初始化工具
	geoTools = GeoTools()
	#无歧义的词语有两种，一开始就是无歧义的和消歧之后无歧义的
	#首先确定不需要消歧的词语：context-所有目前已确认的词语，范围是整段话
	context = []
	for i in xrange(0,len(locations)):
		if len(locations[i]['cnds']) == 1:
			locations[i]['needDisamb'] = False
			context.append(locations[i]['cnds'][0])

	#遍历location，查看是否有需要消歧的（即结果集len大于1）
	for i in xrange(0,len(locations)):
		cnds = locations[i]['cnds']
		if len(cnds) > 1:
			#需要消歧
			locations[i]['needDisamb'] = True
			#消歧的最终结果,应该为一个对象，这里为了全局变量，初始化为list
			tmp_result = cnds[0]
			#消歧第一步，判断是否是国家的消歧，如果是（type=PCLI是国家），找到PCLI那个即可，有多个任选（或者选level最高的）
			#国家消歧
			tmp_result={}
			#遍历cnds查看是否是国家消岐
			for j in cnds:
				if j.has_key('type'):
					if j['type'] == "PCLI":
						tmp_result = j
						break
			#如果遍历到了就是国家消岐
			if len(tmp_result.keys())!=0:
				#消歧结束，更新数据,注意，这里保持数据结构的一致性，格式为[{}]
				tmp = []
				tmp.append(tmp_result)
				locations[i]['cnds'] = tmp
				# locations[i]['cnds'] = list(tmp_result)
				locations[i]['needDisamb'] = False
				context.append(tmp_result)
				continue
			#消歧第二步：判断歧义集中是否包含fc=A的（即行政区域类型的地名），有的话保留这些删除其他，没有的话跳过此步
			#ERROR:【这种思路是错误的，我们仍需要使用fc，默认gnis.admLevel1、2等价于fc=A】但是gnis没有fc属性，为了统一，
			# 我们使用了admLevel来代替，在gns中，admLevel：1~4等价于fc=A；在gnis中，admLevel：1、2等价于fc=A
			#并且，如果结果只有美国的（来自gnis）的，那么跳过第二步
			tmp_cnds = []
			for j in cnds:
				#规范格式，因为从gnis搜索到的结果没有type字段，会在下面的if报错，所以这里人为添加上
				if j.has_key('type') == False:
					j['type'] = 'NULL'
				if j['fc']=='A':
					tmp_cnds.append(j)

			#如果筛选过后什么都没有了就不令 cnds = tmp_cnds，或者只又gnis查询的结果也不令 cnds = tmp_cnds
			only_gnis = False
			for j in tmp_cnds:
				if j.has_key("nt") == True:
					only_gnis = True
					break
			if len(tmp_cnds) > 0 and only_gnis:
				cnds = tmp_cnds

			#2.5
			level_50_cnds=[]
			for j in cnds:
				if j['level'] >= 50:
					level_50_cnds.append(j)
			if len(level_50_cnds) == 1:
				cnds = level_50_cnds


			#取cnds中level最大的作为消岐结果，如果有多个最大结果就继续消岐
			#首先求最大值level是多少
			# max_level = int(cnds[0]['level'])
			# if len(cnds)>1:
			#     for level in cnds:
			#         if int(level['level']) > max_level:
			#             max_level = int(level['level'])
			# #然后筛选掉比最大值小的
			# re=[]
			# for flag in xrange(0,len(cnds)):
			#     if int(cnds[flag]['level']) == max_level:
			#         re.append(cnds[flag])
			# cnds = re
			#是否消歧完成
			if len(cnds) == 1:
				locations[i]['cnds'] = cnds
				locations[i]['needDisamb'] = False
				context.append(cnds[0])
			#第二步消歧完成
			else:
				#无论是否消歧完成，保留现阶段的消歧成果
				locations[i]['cnds'] = cnds

	#如果已确定的词的数量等于已查询出来的词的数量，说明消歧工作已经完成，没有必要进行下一步消歧工作了
	if len(context)!=len(locations):
		#完成第一轮初步消歧后，进行第二轮进一步消歧；这样做是为了尽可能的获得最大且准确的context上下文
		for i in xrange(0,len(locations)):
			cnds = locations[i]['cnds']
			if len(cnds) > 1:
				#如果仍需要消歧，那么检查cnds中有没有fc=L的，如果有就加入黑名单（我们判断经过前两次消歧且fc=L的为区域性名词），
				# 然后进行第三步消歧：根据行政区划等级进行消歧，要求context上下文至少有一个
				#如果context为空（即目前为止一个确认下来的词都没有），则我们取level最大的词

				#检查并加入黑名单
				# for black in cnds:
				# 	if black['fc'] == 'L':
				# 		sql = "SELECT COUNT(black_name) FROM blacklist WHERE black_name = '"+ locations[i]['word'] +"'"
				# 		try:
				# 			# 执行SQL语句
				# 			locNameDic.cur.execute(sql)
				# 			# 获取所有记录列表
				# 			black_num = locNameDic.cur.fetchall()[0][0]
				# 			#如果还不在黑名单中，那么添加进去
				# 			if black_num == 0:
                #
				# 				#转义单词，把单词从"L a s   V e g a s"转义成Las Vegas.修正data.list2string之后就废弃了
				# 				# tmp_words=locations[i]["word"].split(" ")
				# 				# tmp_word = tmp_words[0]
				# 				# for x in xrange(1,len(tmp_words)):
				# 				#     if tmp_words[x].isupper():
				# 				#         tmp_word+=" "
				# 				#     tmp_word+=tmp_words[x]
				# 				tmp_word = locations[i]['word']
                #
				# 				sql = "INSERT INTO blacklist(black_name) VALUES('"+tmp_word.upper()+"')"
				# 				# 执行SQL语句
				# 				locNameDic.cur.execute(sql)
				# 				locNameDic.conn.commit()
				# 				#跳出for检查用循环
				# 				break
				# 		except:
				# 			print "Error: unable to insert new black_name into blacklist"

				#继续执行消歧逻辑
				tmp_result = cnds[0]
				if len(context)==0:
					for j in cnds:
						if j['level'] > tmp_result['level']:
							tmp_result = j
					tmp = []
					tmp.append(tmp_result)
					locations[i]['cnds'] = tmp
					# locations[i]['cnds'] = list(tmp_result)
					locations[i]['needDisamb'] = False
					context.append(tmp_result)
				else:
					#将歧义词集cnds中的每一个词与context中的每一个词进行比对，如果国籍（adm1）相同+100分，二级行政相同+1分。ps：两者计分至少差2个数量级
					for m in xrange(0,len(cnds)):
						cnds[m]['score']=0
						for n in context:
							if cnds[m]['adm1']==n['adm1']:
								cnds[m]['score'] +=100
							if cnds[m]['adm2']==n['adm2']:
								cnds[m]['score'] +=1
					#取得最大值score
					max_score = 0
					for j in cnds:
						if j['score'] > max_score:
							max_score = j['score']
					#获取score为最大值的歧义词
					tmp_result = cnds[0]
					for j in cnds:
						if j['score']==max_score:
							tmp_result=j
					#如果只有唯一的最高分
					if len(tmp_result)==1:
						tmp = []
						tmp.append(tmp_result)
						locations[i]['cnds'] = tmp
						# locations[i]['cnds'] = list(tmp_result)
						locations[i]['needDisamb'] = False
						context.append(tmp_result)
					else:
						#如果有多个最高分的项，那么cnds只保留这做个最高分的歧义词
						tmp_re = []
						for n in cnds:
							if n['score'] == tmp_result['score']:
								tmp_re.append(n)
						#如果有多个最高分说明消歧依旧不彻底，需要进行第四步消歧。不过也要保留目前的消歧成果
						for k in xrange(0,len(tmp_re)):
							del tmp_re[k]['score']
						#如果结果有多个的话，选去level最高的，如果level最高的还有很多，那么执行第四步消岐
						#首先求最大值level是多少
						max_level = int(tmp_re[0]['level'])
						if len(tmp_re)>1:
							for level in tmp_re:
								if int(level['level']) > max_level:
									max_level = int(level['level'])
						#然后筛选掉比最大值小的
						re=[]
						for flag in xrange(0,len(tmp_re)):
							if int(tmp_re[flag]['level']) == max_level:
								re.append(tmp_re[flag])
						locations[i]['cnds'] = re


	#完成第二轮进一步消歧后，进行第三轮最终消歧；这样做是为了尽可能的获得最大且准确的context上下文
	#最终消歧的思路：
	# Pc是上下文，在这里就是location中除了当前需要确认的歧义词之外的全部cnds，T是当前需要确认的词的歧义词集合
	# 1）计算Pc的质心c,其实就是求期望
	# 2）计算Pc 的标准差σ,这里的标准差应该是距离的标准差
	# 3）依次计算ci（0≤i≤n）与c的距离，将距离大于2σ的ci 从Pc中移出，新集合记为P′c
	# 4）计算新集合P′c的质心c′
	# 5）对于歧义地名t的每一个候选地理位置tr（0≤r≤k），计算tr与c′的距离
	# 6）选择距离最小的候选地理位置tj作为歧义地名t对应的地理位置。
	#如果已确定的词的数量等于已查询出来的词的数量，说明消歧工作已经完成，没有必要进行下一步消歧工作了
	if len(context)!=len(locations):
		for i in xrange(0,len(locations)):
			#如果需要消歧
			if len(locations[i]['cnds'])>1:
				#构建Pc和T
				Pc = []
				T = []
				for j in xrange(0,len(locations)):
					if j!=i:
						for m in locations[j]['cnds']:
							Pc.append(m)
				for n in locations[i]['cnds']:
					T.append(n)
				#计算质心
				center = geoTools.GeoCentroid(Pc)
				#计算所有的点到质点的距离
				Pc = geoTools.GeoDistance(Pc,center)
				#计算标准差
				result_list = geoTools.GeoSigma(Pc)
				sigma = result_list[0]
				avar = result_list[1]
				#在上下文只有1或者2个的时候计算sigma是没有意义的，此时sigma=0，意味着dis1=dis2=disE，所以不需要删除偏离的点和计算新的质点
				# if sigma == 0:
				#     T = geoTools.GeoDistance(T,center)
				# else:
				#删除Pc中与质点距离大于u+2σ和小于u-2σ的点
				Pc2 = geoTools.GeoExcept2Sigma(Pc,sigma,avar)
				#计算新的质心
				center2 = geoTools.GeoCentroid(Pc2)
				#计算T的每个点到新质点的距离
				T = geoTools.GeoDistance(T,center2)
				#取dis最小的t
				tmp_result = T[0]
				for t in T:
					if t['dis']-tmp_result['dis']<0:
						tmp_result = t
				tmp = []
				tmp.append(tmp_result)
				locations[i]['cnds'] = tmp
				locations[i]['needDisamb'] = False
				context.append(tmp_result)
			#本歧义地名的消歧完成


			# old
			# 对剩下需要消歧的地名进行消歧
			# for i in range(0, len(locations)):
			#     if locations[i]['isDisamb']:
			#         continue
			#
			#     # 找到离这个词最近的已消歧地名
			#     tmpId = -1
			#     for j in xrange(i + 1, len(locations)):
			#         if locations[j]['isDisamb']:
			#             tmpId = j
			#             break
			#     for j in xrange(i - 1, -1):
			#         if locations[j]['isDisamb']:
			#             tmpId = j
			#             break

			# 给各个候选词评分
			# 100 ：和最近已消歧地名二级行政区划相同的
			# 10  ：和最近已消歧地名一级行政区划相同的
			# 1   ：地理位置等级
			# 0.1 ：词条的创建时间，如果实在没办法，词条创建时间越早，就说明这个地方可能越有名
			# tmpMaxScore = -1
			# for j in xrange(0, len(locations[i]['cnds'])):
			#     locations[i]['cnds'][j]['score'] = 0
			#     if tmpId != -1 and locations[i]['cnds'][j]['adm1'] == locations[tmpId]['cnds'][0]['adm1']:
			#         if locations[i]['cnds'][j]['adm2'] == locations[tmpId]['cnds'][0]['adm2']:
			#             locations[i]['cnds'][j]['score'] += 100
			#         else:
			#             locations[i]['cnds'][j]['score'] += 10
			#
			#     locations[i]['cnds'][j]['score'] += locations[i]['cnds'][j]['level']
			#
			#     if tmpMaxScore < locations[i]['cnds'][j]['score']:
			#         tmpMaxScore = locations[i]['cnds'][j]['score']
			#
			# locations[i]['cnds'] = filter(lambda x: x['score'] == tmpMaxScore, locations[i]['cnds'])
			# locations[i]['cnds'] = locations[i]['cnds'][0:1]

	# 实体链接
	# 如果一个地理位置的多种表述方式都被SQL语句通过SearchName查询出来过，那么其官方表述一定比其非官方表述具有更高的优先级；
	# 因此，如果此时Locations中还存在某个词条不是官方表述，那么其官方表述肯定没有被抽取出来
	# for i in xrange(0, len(locations)):
	#     if locations[i]['cnds'][0]['adm1'] != 'US' or (
	#             locations[i]['cnds'][0]['adm1'] == 'US' and locations[i]['cnds'][0]['adm2'] == '00'):
	#         if locations[i]['cnds'][0]['nt'] != 'C':
	#             #再次尝试抽取官方表述
	#             tmp = locNameDic.getByUfi(locations[i]['cnds'][0]['feature_id'])
	#             if len(tmp) != 0:
	#                 locations[i]['cnds'][0] = tmp[0]
	#             del locations[i]['cnds'][0]['nt']

	# 整理格式，删除我们不需要显示出来的字段
	for i in xrange(0, len(locations)):
		locations[i].update(locations[i]['cnds'][0])
		# del locations[i]['isDisamb']
		if locations[i].has_key('isBigCity'):
			del locations[i]['isBigCity']
		if locations[i].has_key('word'):
			del locations[i]['word']
		if locations[i].has_key('cnds'):
			del locations[i]['cnds']
		#new
		if locations[i].has_key('fc'):
			del locations[i]['fc']
		if locations[i].has_key('needDisamb'):
			del locations[i]['needDisamb']
		if locations[i].has_key('type'):
			del locations[i]['type']
		if locations[i].has_key('dis'):
			del locations[i]['dis']
		if locations[i].has_key('nt'):
			del locations[i]['nt']

	if __DEBUG__:
		_last_time_stamp = time.time()
		print("Time recoganize: " + str(time.time() - _last_time_stamp))

	# DONE!
	return locations
