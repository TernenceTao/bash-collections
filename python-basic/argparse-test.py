#!/usr/bin/python3
# -*- coding:utf-8 -*-

import argparse
import logging

LOG_FORMAT = "%(levelname)s %(asctime)s %(thread)d %(name)s\r\n%(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

parser = argparse.ArgumentParser()
# 该方法用于指定程序能够接受哪些命令行选项
parser.add_argument("echo", help="echo the string you used here")

parser.add_argument(
    "square", help="display a square of a given number", type=int)

parser.add_argument(
    "-v", "--verbosity", help="increase output verbosity", action="store_true")

# 只有test可以被读取，args.t 无效
parser.add_argument(
    "-t", "--test", help="increase output verbosity", type=int, choices=[1, 2, 3])
# 解析参数
args = parser.parse_args()

logging.info(msg="echo="+args.echo)
logging.info(msg="test="+str(args.test))
logging.info(msg="square="+str((args.square ** 2)))
if args.verbosity:
    logging.info(msg=args.verbosity)
