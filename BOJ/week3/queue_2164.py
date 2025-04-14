'''
https://www.acmicpc.net/problem/2164

q는 점점 길어지지만, 우리는 앞쪽은 건드리지 않고 그냥 무시
append()는 O(1)
head += 1은 O(1)
반복 횟수는 N - 1 정도
→ 전체적으로 O(n)
'''

import sys
input = sys.stdin.readline

N = int(input())
q = list(range(1, N+1))
head = 0  # 큐의 앞을 가리키는 인덱스

while head < len(q) - 1:
    head += 1  # 첫 번째 요소는 버림
    q.append(q[head])  # 두 번째 요소는 뒤로 보냄
    head += 1

print(q[head])