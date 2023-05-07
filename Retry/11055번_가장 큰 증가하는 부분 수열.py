'''
수열 A가 주어졌을 때, 그 수열의 증가하는 부분 수열 중에서 합이 가장 큰 것을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 인 경우에 합이 가장 큰 증가하는 부분 수열은 A = {1, 2, 50, 60} 이고, 합은 113이다.
'''

import sys

n = int(sys.stdin.readline().strip())
a = [int(x) for x in sys.stdin.readline().split()]
dp = a[:]

for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + a[i])

print(max(dp))

'''
시간이 걸렸던 이유
dp[i]를 계산할 때, dp[i-1]을 반드시 i-1 번째 인덱스까지의 증가수열 중 증가수열의 합의 최댓값을 dp[i-1]로 저장을 했었기 때문이다. dp[i-1]까지의 최장 증가수열의 합을 구하면 됐던 것인데....
'''