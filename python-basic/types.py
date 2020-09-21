#!/usr/bin/python3

'''
python 数据类型
'''
# 1:数字类型Number有四种类型 int float bool complex
age = 26
weight = 75.6
ifOpen = True
distance = 8+9j
print("type(age)={} type(weight)={} type(ifOpen)={} type(distance=)={}".format(\
    type(age), type(weight), type(ifOpen), type(distance)))

print("age is instance of int ? {} \r\ndistance is instance of complex?{}"
      .format(isinstance(age, int), isinstance(distance, complex)))

# 连续赋值
# a = b = c = 'hello world'
# print("a={} b={} c={}".format(a, b, c))
