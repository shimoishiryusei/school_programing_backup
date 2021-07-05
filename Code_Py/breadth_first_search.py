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
    paths = []
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
                paths.append([here, i])
    return visited, paths


random.seed(6)
node_num = 16
edge_num = 20
my_graph, edge_set = generate_graph(node_num, edge_num)
_, paths = breadth_first_search(10, my_graph)
print(paths)

g = nx.Graph()
for u, v in paths:
    g.add_edge(u, v)
nx.draw_networkx(g)