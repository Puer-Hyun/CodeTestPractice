from collections import deque
import sys 
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


N,M = map(int, input().strip().split())
graph = []
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)] 

for _ in range(N):
    graph.append(list(map(int, input().strip())))

# 상하좌우 이동을 위한 설정을 해줘야할 것 같고
# 각 이동시 벽을 부쉈는지 아닌지를 저장하고 있는 상태가 있어야 할 것 같다.
dx = [1,-1,0,0]
dy = [0,0,1,-1]

print(graph)
print(visited)

def bfs(x, y, z):
    queue = deque()
    queue.append((x,y,z))

    while queue: # queue에 원소가 있는 동안
        a, b, c = queue.popleft() # 좌표를 하나씩 빼낼건데 a,b는 각각 x,y좌표이고 c는 벽파괴술 썼는지 아닌지

        if a == N-1 and b == M-1 : # 끝점에 도착하면 
            return visited[a][b][c] # visited[a][b][c]에 적혀 있는 이동거리를 내뱉는다.
        
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M : # nx,ny가 graph범위 벗어나면 아웃
                continue

            if graph[nx][ny] == 1 and c == 0 : # 다음 이동할 곳이 벽이고, 벽 파괴술을 아직 안썼다면
                visited[nx][ny][1] = visited[a][b][0] + 1 
                queue.append((nx, ny, 1))

            elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0 :
                visited[nx][ny][c] = visited[a][b][c] + 1 
                queue.append((nx, ny, c))
    return -1

print(bfs(0, 0, 0))


            

