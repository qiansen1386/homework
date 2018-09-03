#!/usr/bin/env python3
# https://dsa.cs.tsinghua.edu.cn/oj/problem.shtml?id=33
import re

if __name__ == '__main__':
    letter_count = {}
    s = input().upper()
    for c in s:
        if c == " ":
            continue
        if c in letter_count:
            letter_count[c] += 1
        else:
            letter_count[c] = 1
    letter = list(letter_count.keys())
    letter.sort()
    letter_filter = re.compile(r'^[A-Z]{1}$')
    for c in letter:
        if letter_filter.match(c):
            print("{}: {}".format(c, letter_count[c]))
