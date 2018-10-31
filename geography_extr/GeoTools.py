#-*- coding:utf-8 -*-

class GeoTools:

    #list这样类型的数据：
    # list=[
    #     {"a":"a1","b":"b1"},
    #     {"a":"a2","b":"b2"}
    # ]
    #筛选出list中特定属性名等于特定值的item并返回
    #eg：print tools.GeoFilter(list,"b","b2")
    #>>>[{'a': 'a2', 'b': 'b2'}]
    def GeoFilter(self,list,featureName,featureValue):
        result= []
        for item in list:
            if item[featureName] == featureValue:
                result.append(item)
        return result

    #list的格式是：
    #list=[
    #   {"lat":12,"long":35},
    #   {"lat":36,"long":75},
    #]
    #粗略计算质心，将经纬度看成平面上的xy坐标，平面计算质心就是算平均数[long-x,lat-y]
    #这里的除法不需要考虑除数为零的情况，因为传入的list长度一定大于0，否则就不会调用这个方法了。当然如果你在别处调用这个函数，那么
    #这个函数是不安全的
    def GeoCentroid(self,list):
        x_sum = 0
        y_sum = 0
        for i in xrange(0,len(list)):
            x_sum += self.decimal2float5(list[i]['long'])
            y_sum += self.decimal2float5(list[i]['lat'])
        avar_x = x_sum/len(list)
        avar_y = y_sum/len(list)
        result =[]
        result.append(avar_x)
        result.append(avar_y)
        return result

    #计算一个list中所有点和某个点的距离
    def GeoDistance(self,list,center):
        for i in xrange(0,len(list)):
            # s_long = "{0:.5f}".format(list[i]["long"])
            # long = float(s_long)
            # s_center_long = '{0:.5f}'.format(center[0])
            # center_long = float(s_center_long)
            # s_lat = '{0:.5f}'.format(list[i]['lat'])
            # lat = float(s_lat)
            # s_center_lat = '{0:.5f}'.format(center[1])
            # center_lat = float(s_center_lat)
            dis = ((self.decimal2float5(list[i]['long'])-self.decimal2float5(center[0]))**2+
                   (self.decimal2float5(list[i]['lat'])-self.decimal2float5(center[1]))**2)**0.5
            list[i]['dis'] = dis
        return list

    #计算list的标准差和平均值
    def GeoSigma(self,list):
        sum = 0
        for i in list:
            sum += i['dis']
        avar = sum/len(list)
        n_sum = 0
        for i in list:
            n_sum += (i['dis']-avar)**2
        sigma = (n_sum/len(list))**0.5
        result = []
        result.append(sigma)
        result.append(avar)
        return result

    #保留list中dis在[u-2σ,u+2σ]区间的
    def GeoExcept2Sigma(self,list,index,avar):
        result = []
        left = avar-2*index
        right = avar+2*index
        for i in list:
            if i['dis'] <= right and i['dis'] >= left:
                result.append(i)
        return result

    #将decimal转换成保留5位小数的float
    def decimal2float5(self,decimal_value):
        s_float = '{0:.5f}'.format(decimal_value)
        return float(s_float)