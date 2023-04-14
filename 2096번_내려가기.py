import sys
input = sys.stdin.readline 

n = int(input())
INF = 10e9

#초기 max_graph, min_graph 만들기
max_graph = [[-INF,0,0,0,-INF] for _ in range(n)]
min_graph = [[INF,0,0,0,INF] for _ in range(n)]

for i in range(n):
    a, b, c = map(int,input().split())
    max_graph[i][1], max_graph[i][2], max_graph[i][3] = a, b, c
    min_graph[i][1], min_graph[i][2], min_graph[i][3] = a, b, c



for i in range(1,n):
    for j in range(1,4):
        max_graph[i][j] = max(max_graph[i][j]+max_graph[i-1][j-1], max_graph[i][j]+max_graph[i-1][j], max_graph[i][j]+max_graph[i-1][j+1])
        min_graph[i][j] = min(min_graph[i][j]+min_graph[i-1][j-1], min_graph[i][j]+min_graph[i-1][j], min_graph[i][j]+min_graph[i-1][j+1])

print(max(max_graph[-1]), min(min_graph[-1]))