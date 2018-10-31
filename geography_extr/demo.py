#encoding:utf-8
import time

import main

raw =[[[0, u'nanjing'], [4, u'shenzhen'], [7, u'hongkong'], [31, u'Russia']],
 [[5, u'Helsinki'], [10, u'U.S.']],
 [],
 [[1, u'Washington'], [3, u'Helsinki']],
 [[15, u'Arctic']],
 [[6, u'U.S.'], [16, u'U.S.'], [22, u'Baltic Sea']],
 [[6, u'Russia']],
 [],
 [[18, u'Baltic Sea'], [22, u'Kaliningrad']],
 [[0, u'Estonia']],
 [[1, u'United States'],
  [11, u'Russia'],
  [19, u'Baltic Sea'],
  [23, u'Finland'],
  [25, u'Sweden'],
  [27, u'Estonia'],
  [29, u'Latvia'],
  [46, u'Russia'],
  [50, u'U.S.']],
 [[3, u'Helsinki'], [24, u'Russia']],
 [],
 [[9, u'Russia'], [12, u'Finland']],
 [[2, u'Finland'], [4, u'Sweden'], [14, u'Britain']]]

#ps:这个demo中目前第二个East Jerusalem【只找到East】和倒数第四个Israeli是查询不到的

# 初始化
time_s = time.time()
rec = main.LocationRecoganizer()

out = rec.recoganize(raw)
import pprint
# print(len(out))

pprint.pprint(out)
time_e = time.time()
print time_e-time_s
####################
'''
输出格式：{
	'ufi': Decimal('-1900673'),
	'offset': 19, 
	'lat': Decimal('35.000000'), 
	'adm2': '00', 
	'level': 0, 
	'geoname': 'China', 
	'long': Decimal('105.000000'), 
	'adm1': 'CHN'
}

数据库配置在data.py中。localhost，用户名root，密码空，数据库名loc

'''
