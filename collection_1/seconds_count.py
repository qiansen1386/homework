#!/usr/bin/env python3
# https://dsa.cs.tsinghua.edu.cn/oj/problem.shtml?id=34
# case: 00:00:03 00:00:06
import functools


def readtime(s):
    def split_colon(str): return str.split(":")

    def add_list(list1, list2): return list1 + list2

    def process(s): return map(
        int,
        functools.reduce(
            add_list,
            map(
                split_colon,
                s.split()
            )))
    return process(s)


def hmsToSec(h, m, s):
    return h*3600+m*60+s


if __name__ == '__main__':
    h1, m1, s1, h2, m2, s2 = readtime(input())
    # print("{}:{}:{} => {}:{}:{}".format(h1, m1, s1, h2, m2, s2))
    # print((h2-h1)*3600+(m2-m1)*60+(s2-s1))
    timestamp2 = hmsToSec(h2, m2, s2)
    timestamp1 = hmsToSec(h1, m1, s1)
    diff = timestamp2-timestamp1
    print(diff if diff > 0 else 24*3600 + diff)
