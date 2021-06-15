import networkx as nx
import matplotlib
graph = nx.Graph()
graph.add_edge(5, 6)
graph.add_edge(6, 7)
nx.draw_networkx(graph)
