'''
https://www.acmicpc.net/problem/9012
'''
n = int(input())

for _ in range(n):
    str = input()
    tmp = []
    for s in str:
        if len(tmp) == 0:
            tmp.append(s)
        elif s == '(':
            tmp.append(s)
        elif s == ')' and tmp[-1] == ')':
            tmp.append(s)
        else:
            tmp.pop()
    if len(tmp) == 0:
        print('YES')
    else:
        print('NO')




