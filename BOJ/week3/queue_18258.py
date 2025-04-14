'''
https://www.acmicpc.net/problem/18258


이 문제의 핵심은 시간복잡도 줄이기!
q.pop(0)은 내부적으로 다음과 같이 동작해 시간 복잡도가 O(n)

q = [1, 2, 3, 4, 5]
q.pop(0)  # 1을 꺼냄

1. 2를 0번 자리에 복사
2. 3을 1번 자리에 복사
3. 4를 2번 자리에 복사
4. 5를 3번 자리에 복사
5. 마지막 4번 자리는 삭제

=> 이걸 여러번 반족하면 전체 시간은 O(n²)

**해결방법**
1. deque 사용하기
deque.popleft()는 앞에서 꺼내도 안 밀어되기 때문에 무조건 1초 만에 꺼내짐. (O(1))
2. 리스트 그대로 쓰되, 앞에서 꺼낸 건 지우지 않고 "넘기기". 실제로 삭제 안 하고, 앞 인덱스만 이동  O(1)
'''

import sys
input = sys.stdin.readline

n = int(input())
q = []
head = 0  # 큐의 시작 인덱스

for _ in range(n):
    w = input().split()
    if w[0] == "push":
        q.append(w[1])
    elif w[0] == "pop":
        if head == len(q):
            print(-1)
        else:
            print(q[head])
            head += 1
    elif w[0] == "size":
        print(len(q) - head)
    elif w[0] == "empty":
        print(1 if head == len(q) else 0)
    elif w[0] == "front":
        print(q[head] if head != len(q) else -1)
    elif w[0] == "back":
        print(q[-1] if head != len(q) else -1)