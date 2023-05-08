'''
문제
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

N개의 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
고른 수열은 비내림차순이어야 한다.
길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.
입력
첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.
'''

'''
Ideation 
1. 우선은 data를 정렬을 한 뒤, combination을 수행한다.
2. 중복 combination을 제거하는 방법을 구현해내기 위해선, combination을 직접 정의해야 할 것 같다.
3. 기존의 combination을 사용하는 방법을 먼저 생각해보자.
'''
from itertools import combinations_with_replacement
N,M = map(int, input().split())
data = sorted(list(map(int, input().split())))
data_cand = sorted(set(list(combinations_with_replacement(data, M))))

for i in data_cand:
    print(*i)

'''
# Authored by : tony9402
# Co-authored by : -
# Link : http://boj.kr/dbd389b484d4468990a877b205126f0f
import sys

def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
arr  = sorted(list(map(int, input().split())))
choose = [ 0 for _ in range(10) ]

def dfs(idx, cnt):
    global N, M
    if cnt == M:
        for idx in range(cnt):
            print(arr[choose[idx]], end=' ')
        print()
        return

    pre = -1
    for i in range(idx, N):
        if pre == arr[i]:
            continue
        pre = arr[i]
        choose[cnt] = i
        dfs(i, cnt + 1)

dfs(0, 0)
'''

