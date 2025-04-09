'''
https://www.acmicpc.net/problem/10773
'''
i = int(input())
n_list = []

for _ in range(i):
    n = int(input())
    if (n == 0 and len(n_list) == 0):
        continue
    elif (n == 0 and len(n_list) != 0):
        n_list.pop()
    else:
        n_list.append(n)

print(sum(n_list))



