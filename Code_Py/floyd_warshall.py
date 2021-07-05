import random
import math
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
        graph_data[i][j] = graph_data[j][i] = 1
    return graph_data, edge_set


def all_pairs_shortest_paths(W):
    # 頂点の数
    n = len(W)
    # 結果を格納する行列を用意する
    res = [[0] * n for i in range(n)]
    # 用意した行列を初期化する
    for i in range(n):
        for j in range(i, n):
            if i == j:
                val = 0
            elif W[i][j]:
                val = W[i][j]
            else:
                val = math.inf
            res[i][j] = res[j][i] = val
    # 動的計画法ですべての頂点間の最短距離を求める
    for k in range(n):
        for u in range(n):
            for v in range(n):
                res[u][v] = min(res[u][v], res[u][k] + res[k][v])
    return res


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
    return visited


random.seed(6)
node_num = 16
edge_num = 20
my_graph, edge_set = generate_graph(node_num, edge_num)
print(all_pairs_shortest_paths(my_graph))

result = depth_first_search(10, my_graph)

graph = nx.Graph()
for edge in edge_set:
    if set(edge).issubset(result):
        graph.add_edge(edge[0], edge[1])
nx.draw_networkx(graph)
