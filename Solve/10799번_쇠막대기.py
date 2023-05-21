import sys 
from collections import deque
input = sys.stdin.readline

data = input().replace('()', 'R')
#print(data)
tmp = deque([])

que = deque(data)
answer = 0
while que:
    X = que.popleft()
    if X == '(':
        tmp.append(['(', 0])
    elif X == 'R':
        if len(tmp)==0:
            pass
        else:
            for i in range(len(tmp)):
                tmp[i][1] += 1 
    elif X == ')':
        complete = tmp.pop()
        answer += (complete[1]+1)
print(answer)


#######
import sys
input = sys.stdin.readline

data = input().rstrip()
stack = []
answer = 0

for i in range(len(data)):
    if data[i] == '(':
        stack.append(i)
    else:
        if stack[-1] + 1 == i:  # '(' 다음에 바로 ')'가 오는 경우는 레이저
            stack.pop()
            answer += len(stack)
        else:  # 쇠막대기의 끝
            stack.pop()
            answer += 1

print(answer)