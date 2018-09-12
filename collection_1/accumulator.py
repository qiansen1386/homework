#!/usr/bin/env python3
# https://dsa.cs.tsinghua.edu.cn/oj/problem.shtml?id=1053
"""
demo:
    3
    10 30
    20 40
    15 22
Return
    40
    60
    37
"""

if __name__ == '__main__':
    n = int(input())
    s = []
    for i in range(n):
        int_arr = input().split()
        sum = int(int_arr[0])+int(int_arr[1])
        s.append(sum)
    print("\n".join(map(str,s)))
