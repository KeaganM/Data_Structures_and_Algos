import matplotlib.pyplot as plt
import numpy as np

from graph2 import Node, Graph, reconstruct_path
from custom_queue import Queue
import random


def visualize_graph(graph, nodes, p):
    fig, ax = plt.subplots()

    xs = [n.x for n in nodes]
    ys = [n.y for n in nodes]

    ax.scatter(xs,ys)

    for key, value in graph.graph.items():
        node = nodes[key.id]
        x, y, name = node.x, node.y, node.id
        ax.text(x, y, name)
        for adj_node in value:
            n = nodes[adj_node.id]
            adj_x, adj_y = n.x, n.y
            ax.plot([x, adj_x], [y, adj_y], 'blue', alpha=0.1)

    path_x = []
    path_y = []
    for p_node in p:
        n = nodes[p_node.id]
        path_x.append(n.x)
        path_y.append(n.y)
    ax.plot(path_x, path_y, 'red', linestyle='--')

    plt.show()


# if __name__ == '__main__':
#
#     nodes_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     ys = random.sample(range(1, 12), len(nodes_list))
#
#     nodes = [Node(id=x, x=x, y=y) for x, y in zip(nodes_list, ys)]
#     start_node = nodes[0]
#     end_node = nodes[10]
#
#     graph = Graph()
#
#     abs_path = [0, 3, 5, 8, 10]  # ensures there will be at least one path
#     for i, item in enumerate(abs_path):
#         try:
#             graph.add_edge(nodes[item], nodes[abs_path[i + 1]])
#         except Exception:
#             pass
#
#     graph.add_edge(nodes[0], nodes[1])
#     graph.add_edge(nodes[0], nodes[2])
#     graph.add_edge(nodes[0], nodes[3])
#     graph.add_edge(nodes[4], nodes[1])
#     graph.add_edge(nodes[5], nodes[7])
#     graph.add_edge(nodes[9], nodes[8])
#     graph.add_edge(nodes[1], nodes[9])
#
#     graph.print_graph()
#     print(f'start is: {start_node}')
#     print(f'end is: {end_node}')
#
#     a = graph.breadth_first_search(start_node)
#     p = reconstruct_path(a, start_node, end_node)
#     print(a)
#     print(p)
#
#     # visualization ****************************************************************************************************
#
#     visualize_graph(graph,nodes,p)