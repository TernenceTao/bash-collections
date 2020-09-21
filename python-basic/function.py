#!/usr/bin/python3

target = 10


def showVar(a, b):
    global target
    target = target + b
    print('访问taget:{}'.format(target))
    return target


def insert(sql, values):
    print("exec sql : {}".format(sql))
    print("insert into values:{}".format(values))
    return True


showVar(12, 12)
print('全局范围内的target:{}'.format(target))

if __name__ == "__main__":
    print("我来自自身主程序执行")
else:
    print("我来自其他程序执行:{}".format(__name__))
