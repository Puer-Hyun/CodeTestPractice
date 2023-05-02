'''
N×N크기의 땅이 있고, 땅은 1×1개의 칸으로 나누어져 있다. 각각의 땅에는 나라가 하나씩 존재하며, r행 c열에 있는 나라에는 A[r][c]명이 살고 있다. 인접한 나라 사이에는 국경선이 존재한다. 모든 나라는 1×1 크기이기 때문에, 모든 국경선은 정사각형 형태이다.

오늘부터 인구 이동이 시작되는 날이다.

인구 이동은 하루 동안 다음과 같이 진행되고, 더 이상 아래 방법에 의해 인구 이동이 없을 때까지 지속된다.

국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
연합을 해체하고, 모든 국경선을 닫는다.
각 나라의 인구수가 주어졌을 때, 인구 이동이 며칠 동안 발생하는지 구하는 프로그램을 작성하시오.
'''

# 반복문이 돌아야 할 것 같은데, 그 기준은 연결된 것이 있는지이다.
# 연결된 상태를 나타낼 수 있는 것이 필요할 것 같다. 
# 동시 업데이트가 진행되야된다는 점에서 순차적으로 bfs, dfs를 진행하면 안 될 것 같다.
# 연결된 것이 있는지를 확인하는 함수의 input은 행렬이고 확인하는 과정에서 연결된 것이 있으면 output으로 해당 위치들, total을 받아야한다.
# 이중반복문을 여러 번 돌려도 된다고 판단했는데 그 이유는 1<=N<=50이고, 일수가 2000보다 작거나 같기 때문이다.
# 4*4 행렬과 같은 경우는 구역이 여러 개 있을 수도 있다. 따라서 영역의 개수를 체크해주는 것이 필요할 것 같기도 하다.


from collections import deque
import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())
matrix = []

for _ in range(N):
    matrix.append(list(map(int, input().split())))

dx = [0,0,-1,1]
dy = [1,-1,0,0]


def bfs(a:int, b:int) -> list:
    '''
    시작점 a,b 좌표를 입력받아서, 기존의 matrix를 탐색한 후 연결되는 좌표들의 리스트를 반환한다. bfs를 수행해가면서 지나가는 점들은 visited 표시한다.
    '''
    q = deque()
    coordinate_list = []
    q.append([a,b])
    coordinate_list.append([a,b])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny]==0:
                if L<=abs(matrix[nx][ny]-matrix[x][y])<=R:
                    visited[nx][ny]=1 #여기에서 visited[nx][ny]==1 로 적어서 틀림
                    q.append([nx,ny])
                    coordinate_list.append([nx,ny])
    return coordinate_list
        

answer = 0

while True :
    visited = [[False]*(N+1) for _ in range(N+1)]
    flag = 0    
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 :
                visited[i][j] == 1               
                target_country = bfs(i,j) 
                if len(target_country) > 1 :
                    flag = 1 
                    average_population = sum([matrix[x][y] for x,y in target_country]) // len(target_country)
                    for x,y in target_country:
                        matrix[x][y] = average_population
    if flag==0:
        break
    answer += 1 
print(answer)








'''
def link_check(matrix : list, x : int, y : int) -> list :
    result = []
    for i in range(4):
        dx, dy = x_list[i], y_list[i]
        if 0 <= x+dx <= N-1 and 0<= y+dy <= N-1:
            if L<=abs(matrix[x][y]-matrix[x+dx][y+dy])<=R:
                result.append([x+dx, y+dy])
def check(matrix : list) -> tuple :
    total = 0
    position = []
    for i in range(N):
        for j in range(N):
            if 
'''
