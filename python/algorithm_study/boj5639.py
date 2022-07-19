import sys

sys.setrecursionlimit(10 ** 6)


# dfs 탐색
def dfs(start, end):
    # 시작과 끝 값이 역전시 리턴
    if start > end:
        return

    # 아래서 서브트리가 안찾아질 경우를 대비해서 탐색 대상을 end + 1로 초기화
    mid = end + 1

    # 서브 트리 찾기
    for i in range(start + 1, end + 1):
        # 루트 보다 크면 오른쪽 서브 트리
        if graph[start] < graph[i]:
            mid = i
            break

    dfs(start + 1, mid - 1)  # 왼쪽 서브 트리 재귀적으로 탐색
    dfs(mid, end)  # 오른쪽 서브 트리 재귀적으로 탐색

    print(graph[start])


graph = []
while True:
    try:
        graph.append(int(sys.stdin.readline()))
    except:
        break

dfs(0, len(graph) - 1)
