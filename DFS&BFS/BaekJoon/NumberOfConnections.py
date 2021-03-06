'''
문제
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2)
둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v)
같은 간선은 한 번만 주어진다.

출력
첫째 줄에 연결 요소의 개수를 출력한다.

예제 입력 1
6 5
1 2
2 5
5 1
3 4
4 6
예제 출력 1
2
예제 입력 2
6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3
'''


def dfs(x):
    visited[x] = True
    for i in graph[x]:
        if not visited[i]:
            dfs(i)


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
count = 0
for i in arr:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])

for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)
