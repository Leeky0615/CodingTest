'''
    서로소 집합을 활용한 사이클 판별
    서로소 집합은 무방향 그래프 내에서의 사이클을 판별할 때 사용할 수 있다.
      ㅇ 참고로 방향 그래프에서의 사이클 여부는 DFS를 이용하여 판별할 수 있다
    사이클 판별 알고리즘은 다음과 같다
      1. 각 간선을 하나씩 확인하며 두 노드의 루트 노드를 확인합니다.
         1) 루트 노드가 서로 다르다면 두 노드에 대하여 합집합 연산을 수행한다.
         2) 루트 노드가 서로 같다면 사이클이 발생한 것이다.
      2. 그래프에 포함되어 있는 모든 간선에 대하여 1번 과정을 반복한다
'''

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드를 찾을 때까지 재귀 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합을 찾기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드의 개수와 간선(union 연산)의 개수 입력 받기
v, e = map(int, input().split())
parent = [0] * (v + 1)  # 부모 테이블 초기화 하기

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

cycle = False # 사이클 발생 여부

# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    # 사이클이 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")