from collections import deque

N,M = map(int,input().split())
# N -> 頂点
# M -> 辺

graph = [[] for _ in range(N+1)]
lists = [list(map(int,input().split())) for _ in range(N)]
distance = [-1 for _ in range(N+1)]
distance[0],distance[1] = 0,0

# 要素 繋がっている次の要素　となるように配列を作る
for i in range(N):
    a,b = lists[i]
    graph[a].append(b)
    graph[b].append(a)    
print(graph)

d = deque()
d.append(1)
while d:
    i = d.popleft()
    for j in graph[i]: # 幅優先探索
        if distance[j] == -1: # 未到達の場合
            distance[j] = distance[i] + 1
            d.append(j)
print(distance)

