#!/usr/bin/env python3
# https://dsa.cs.tsinghua.edu.cn/oj/problem.shtml?id=32

if __name__ == '__main__':
    a, b = list(map(int, input().split()))
    # print(a, b)
    remainder = 1

    if a > b:
        num1, num2 = a, b
    else:
        num1, num2 = b, a

    while(remainder):
        remainder = num1 % num2
        num1, num2 = num2, remainder
    print(num1)
