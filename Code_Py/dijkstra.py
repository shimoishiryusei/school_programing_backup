import math
import heapq
import random


def dijkstra(start, W):
    """
    スタートの頂点と隣接行列を受け取り，
    到達できるすべての頂点への最短距離を返す．
    """
    # 仮の最短距離を∞に設定
    distance_list = [math.inf] * len(W)
    # スタートの頂点だけ距離を0にする
    distance_list[start] = 0
    # 最短距離が確定した頂点
    done_list = []
    # 次に処理する頂点を決めるためのヒープ
    wait_heap = []
    for i, d in enumerate(distance_list):
        # (スタートからの距離，頂点) のタプルを作る
        heapq.heappush(wait_heap, (d, i))

    # ヒープが空っぽになるまで処理を続ける
    while wait_heap:
        p = heapq.heappop(wait_heap)
        i = p[1]
        if i in done_list:
            continue
        # この時点でスタートからiへの移動距離が確定
        done_list.append(i)
        # iに隣接するすべての頂点に対する処理
        for j, x in enumerate(W[i]):
            if x == 1 and j not in done_list:
                # 緩和
                d = min(distance_list[j], distance_list[i] + x)
                distance_list[j] = d
                # jへの仮の最短距離をdとしてヒープに追加
                heapq.heappush(wait_heap, (d, j))
    return distance_list


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

print(dijkstra(10, my_graph))
