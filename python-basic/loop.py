#!/usr/bin/python3

array = [1, 2, 3, 'tao', 'jiang', True]
'''
for a in array:
    print("a = {}".format(a))
    if a == True:
        print("a == True")
        if a == 1:
            print("找到1 True")
        else:
            pass
    elif a == 'tao':
        print("找到我的姓")
    else:
        print("其他")
'''
'''
i = 0
while i < len(array):
    print('array['+str(i)+']={}'.format(array[i]))
    i = i+1
else:
    print("迭代结束 i={}".format(i))
    pass
'''
'''
i = 0
for i in range(len(array)):
    print('array['+str(i)+']={}'.format(i))
else:
    print('循环结束:i={}'.format(i))
    pass
'''
'''
i = 0
for i in array:
    if i == True:
        continue
    else:
        print('i={}'.format(i))
        pass
else:
    print('程序执行结束')
    pass
print('全流程结束')
'''

'''
i = 0
for i in array:
    if i == True:
        break
    else:
        print('i={}'.format(i))
        pass
else:
    print('程序执行结束')
    pass
print('全流程结束')
'''

'''
while True:
    pass  # 等待键盘中断
'''

dicts = {'name': 'tao jiang hang', 'age': 22, 'gender': '男'}
print(dicts.items())
for key, value in dicts.items():
    print("{}={}".format(key, value))
