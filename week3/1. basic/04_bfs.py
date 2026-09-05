"""
[BFS - 너비 우선 탐색 (Breadth-First Search)]

문제 설명:
- BFS로 그래프를 탐색합니다.
- 가까운 정점부터 방문합니다.
- 큐(Queue)를 사용합니다.

입력:
- graph: 그래프 (인접 리스트)
- start: 시작 정점

출력:
- 방문 순서

예제:
그래프:
  0 ─── 1
  │     │
  └─ 2 ─┘
      │
      3

시작: 0
BFS:ㅑ [0, 1, 2, 3]

힌트:
- Week2의 큐 사용
- 방문 체크 필요
- 가까운 것부터 방문
"""

from collections import deque

# graph: (dictionary) adjacency list
# start: (integer) initial node
def bfs(graph, start):   
    
    visited = []    # final return value (exact order, which nodes are popped and processed.)
    discovered = {start}    # hash set. start node. read in O(1). 
    

    # 큐 생성 및 시작 정점 추가
    ## 방문한 정점 집합
    queue = deque([start])  # FIFO data structure, wave-like spread of BFS

    # TODO: 큐가 빌 때까지 반복
    ## 큐에서 정점 꺼내기
    ## 인접한 정점들 확인
    ## 방문하지 않은 정점이면 큐에 추가
    while queue:    # discovered 된 neighbor 가 queue 에 남아 있는 한, 
        # O(1) constant time, avoiding the heavy O(N) memory-shifting penalty of standard lists.
        current = queue.popleft() # 'start'가 가장 먼저 pop 된다. # node 를 level 별로 처리
        visited.append(current) # 현재 노드를 visited 에 추가 ('start'가 먼저 visited 에 추가됌)

        for neighbor in graph[current]:     # current 노드를 조회, 모든 neighbor 를 가져온다
            if neighbor not in discovered:  
                discovered.add(neighbor)
                queue.append(neighbor)
    
    return visited  ## queue 가 완전히 pop 되면 (for문에서 모든 노드가 탐색된 경우) return

# 테스트 케이스
if __name__ == "__main__":
    # graph initialization (adjency list)
    graph = {   
        # vertex(integer): (list) neighbor vertices
        0: [1, 2],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2]
    }
    
    print("=== BFS (너비 우선 탐색) ===")
    result = bfs(graph, 0)  # start node: 0  # 함수 호출: 큐 및 탐색 로직이 실행된다
    print(f"시작 정점: 0")
    print(f"방문 순서: {result}") # start node 를 0 으로 줬으니, 당연히 result 첫 인수는 0 이다.

