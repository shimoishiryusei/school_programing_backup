import random
from collections import deque
import networkx as nx



def generate_graph(n, m):
    """n個の頂点とm個の編を持つグラフを作る"""
    graph_data = [[0] * n for i in range(n)]
    # 同じ辺が同一視されるようにsetを用意
    edge_set = set()
    while len(edge_set) < m:
        i, j = random.sample(range(n), 2)
        if i > j:
            i, j = j, i
        edge_set.add((i, j))
        graph_data[i][j] = graph_data[j][i] = i
    return graph_data, edge_set


def breadth_first_search(start, W):
    """
    隣接行列Wで表現されるグラフについてstartから到達できるnodeの一覧を返す
    """
    # リストをキューにする
    work_queue = deque([])
    visited = set()
    # 初期化
    work_queue.append(start)
    visited.add(start)
    while work_queue:
        # いまいる頂点

        here = work_queue.popleft()
        # 今いる頂点に隣接する頂点すべてを処理する
        for i, node in enumerate(W[here]):
            # 隣接しなければ何もしない
            if node == 0:
                continue
            if i not in visited:
                work_queue.append(i)
                visited.add(i)
    return visited


def depth_first_search(start, W):
    # リストをスタックとして利用
    work_stack = []
    visited = set()
    work_stack.append(start)
    visited.add(start)
    while work_stack:
        here = work_stack.pop()
        for i, node in enumerate(W[here]):
            if node == 0:
                continue
            if i not in visited:
                work_stack.append(i)
                visited.add(i)
                print(visited)
    return visited


random.seed(6)
node_num = 16
edge_num = 20
my_graph, edge_set = generate_graph(node_num, edge_num)
breadth_first_search(1, my_graph)

result = depth_first_search(10, my_graph)

graph = nx.Graph()
for edge in edge_set:
    if set(edge).issubset(result):
        graph.add_edge(edge[0], edge[1])
nx.draw_networkx(graph)
