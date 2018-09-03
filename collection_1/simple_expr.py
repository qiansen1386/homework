#!/usr/bin/env python3
# https://dsa.cs.tsinghua.edu.cn/oj/problem.shtml?id=31


def plus(num1, num2):
    return num1+num2


def minus(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


if __name__ == '__main__':
    num1, op, num2 = map(lambda s: s.strip(), input().strip().split())
    op_dict = {"+": plus, "-": minus, "*": multiply}
    if op in op_dict.keys():
        print("{0:.0f}".format(op_dict[op.strip()](float(num1), float(num2))))
