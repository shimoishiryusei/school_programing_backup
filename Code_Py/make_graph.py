import random


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


random.seed(6)
node_num = 16
edge_num = 20
my_graph, edge_set = generate_graph(node_num, edge_num)
print(edge_set)
