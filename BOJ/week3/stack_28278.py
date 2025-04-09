"""
https://www.acmicpc.net/problem/28278

"""
import sys

input = sys.stdin.readline
n = int(input())
stack = []
for _ in range(n):
    input_list = input().split()
    cnt = ''
    x = 0
    if (len(input_list) > 1):
        cnt = input_list[0]
        x = int(input_list[1])
    else:
        cnt = input_list[0]

    if (cnt == '1'):
        stack.append(x)
    elif (cnt == '2'):
        if (len(stack) > 0):
            print(stack.pop())
        else:
            print(-1)
    elif (cnt == '3'):
        print(len(stack))
    elif (cnt == '4'):
        if (len(stack) == 0):
            print(1)
        else:
            print(0)
    else:
        if (len(stack) > 0):
            print(stack[-1])
        else:
            print(-1)


