import sys
input = sys.stdin.readline 

n = int(input())
INF = 10e9

#초기 max_graph, min_graph 만들기
max_dp = [-INF, 0, 0, 0, -INF]
min_dp = [INF, 0, 0, 0, INF]

max_tmp = [-INF, 0, 0, 0, -INF]
min_tmp = [INF, 0, 0, 0, INF]

for _ in range(n):
    X = list(map(int,input().split()))
    for i in range(1,4):
        max_tmp[i] = X[i-1] + max(max_dp[i-1], max_dp[i], max_dp[i+1])
        min_tmp[i] = X[i-1] + min(min_dp[i-1], min_dp[i], min_dp[i+1])
    
    for i in range(1,4):
        max_dp[i] = max_tmp[i]
        min_dp[i] = min_tmp[i]

print(max(max_dp[1:4]), min(min_dp[1:4]))