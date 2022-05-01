'''
https://www.geeksforgeeks.org/graph-and-its-representations/

graph representation:

- finite set of vertices called nodes
- finite set of ordered pair forms called edge which may have weight, value, etc.
- adjacency matrix is a 2d matrix of size V where V is the number of vertices in a graph.
    - let adj[][] be the 2d matrix; adj[i][j] =1 indicates an edge between i and j

        0   1   2   3   4
    0   0   1   0   0   1
    1   1   0   1   1   1
    2   ...
    3
    4

    - in a case above there is an edge between node 0 and 1
    - pros is this method allows queries between nodes to be done in O(1)
    - cons is this method takes more space and adding a vertex is done in O(V^2)
- adjacency list is similar but an array of lists/arrays are used
    [0,_] -> [1,_] -> [4,/]
    [1,_] -> [0,_] -> [4,_] -> [2,_] -> [3,/]
    ...
    - when looking at this consider it from the perspective of a given node
    - in the above we can see that 0 leads to 1 and 1 leads to 4
    - / being the return to the original node
        - so 1 can go to 0 which in turn can go to 4, and 1 can go to 2 which in turn can go 3 and we return to 1 (/)
    - pros of this method is that it saves space O(|V|+|E|) (v is nodes and e is edges); adding a vertix is easier
    - cons is that queries can take up to O(V)
'''
from typing import Union, TypeVar, List, Optional, Callable, Dict
from collections import defaultdict
import math

from custom_queue import Queue, PriortyQueue
from stack.stack import Stack

import matplotlib.pyplot as plt
import numpy as np


T = TypeVar('T')


class Node:
    def __init__(self, id: str,x:Union[None,int] = None,y:Union[None,int] = None):
        self.id = id

        # for visualizing
        self.x = x
        self.y = y

    def __repr__(self):
        return f'{self.id}'


class Graph:
    def __init__(self, nodes: list, repr: str = 'matrix'):

        self.nodes = {n.id: i for i, n in enumerate(nodes)}
        self._repr_type = repr
        self._repr = self._create_matrix_or_list(repr, nodes)

    @property
    def repr(self):
        return self._repr

    def add_edge(self, n1: Node, n2: Node, cost: Union[int, float, None] = None):
        n1_pos = self.nodes[n1.id]
        if self._repr_type == 'matrix':
            n2_pos = self.nodes[n2.id]
            self._repr[n1_pos][n2_pos] = cost
        else:
            if cost:
                self._repr[n1_pos].append((n2.id, cost))
            else:
                self._repr[n1_pos].append(n2.id)

    def _create_matrix_or_list(self, repr: str, nodes: list):
        m = []
        if repr == 'matrix':
            m = []
            for _ in nodes:
                nested_m = []
                for _ in nodes:
                    nested_m.append(0)
                m.append(nested_m.copy())
                del nested_m
        else:
            m = [[] for _ in nodes]
        return m

    def __repr__(self):
        node_ids = list(self.nodes.keys())
        s = '   ' + '  '.join(node_ids) + '\n' if self._repr_type == 'matrix' else ''
        for i, row in enumerate(self._repr):
            s += f'{node_ids[i]} {row}\n'
        return s


# https://www.youtube.com/watch?v=7fujbpJ0LB4&list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P&index=4
class DFS:
    def __init__(self, graph: Graph):
        self.graph = graph
        self.nodes = len(self.graph.nodes.keys())
        self.adj_list = graph.repr
        self.visited = [False] * self.nodes

    # todo so far just tells you if a node is reachable or not
    def dfs(self, at):
        if self.visited[at]:
            return
        self.visited[at] = True

        neighbors = self.adj_list[at]
        for i, _ in enumerate(neighbors):
            self.dfs(i + 1)


class BFS:
    def __init__(self, graph):
        self.nodes = graph.nodes
        self.graph = graph
        self.adj_list = graph.repr

    def bfs(self, start, end):
        q = Queue()

        visited = []
        parents = {}

        q.push(start.id)
        while q._q:
            node = q.pop()
            if node == end:
                break
            visited.append(node)
            for item in self.adj_list[self.nodes[node]]:
                if item not in visited and item not in q._q:
                    q.push(item)
                    parents[item] = node

        next_item = end.id
        path = [next_item]
        while True:
            next_item = parents[next_item]
            path.append(next_item)
            if next_item == start.id:
                break
        return list(reversed(path))

# https://www.youtube.com/watch?v=pSqmAO-m7Lk&list=PLDV1Zeh2NRsDGO4--qE8yH72HFL1Km93P&index=18
class Dijkstras:
    def __init__(self):
        ...

i


if __name__ == '__main__':
    # test 1 ***********************************************************************************************************
    # a = Node('a')
    # b = Node('b')
    # c = Node('c')
    # d = Node('d')
    # e = Node('e')
    #
    # g = Graph([a, b, c, d, e], 'list')
    #
    # g.add_edge(a, b, 4)
    # g.add_edge(a, c, 1)
    # g.add_edge(a, d, 9)
    #
    # g.add_edge(b, a, 3)
    # g.add_edge(b, c, 6)
    # g.add_edge(b, d, 11)
    #
    # g.add_edge(c, a, 4)
    # g.add_edge(c, b, 1)
    # g.add_edge(c, d, 2)
    #
    # g.add_edge(d, a, 6)
    # g.add_edge(d, b, 5)
    # g.add_edge(d, c, -4)
    #
    # print(g)
    #
    # dfs = DFS(g)
    # dfs.dfs(0)
    # print(dfs.visited)
    #
    # test 2 ***********************************************************************************************************
    import random



    a = Node('0')
    b = Node('1')
    c = Node('2')
    d = Node('3')
    e = Node('4')
    f = Node('5')
    g = Node('6')
    h = Node('7')
    i = Node('8')
    j = Node('9')
    k = Node('10')
    l = Node('11')
    m = Node('12')

    nodes = [a, b, c, d, e, f, g, h, i, j, k, l, m]
    xs = []
    ys = []

    def get_random_unique(items:list)->int:
        x = None
        while True:
            x = random.randint(0, 20)
            if x not in items:
                break
        return x

    for _ in range(len(nodes)):
        xs.append(get_random_unique(xs))
        ys.append(get_random_unique(ys))

    for index,node in enumerate(nodes):
        node.x = xs[index]
        node.y = ys[index]


    graph = Graph(nodes, 'list')

    # todo may want to look at creating bulk edges
    edges_to_add = {
        a: [j, h, l],
        b: [k, i],
        c: [m, d],
        d: [c, e, h],
        e: [d],
        f: [g],
        g: [f, h],
        h: [g, l, a, d],
        i: [b, m, j],
        j: [k, a, i],
        k: [b, j],
        l: [a, h],
        m: [c, i]
    }
    for key in edges_to_add.keys():
        for v in edges_to_add[key]:
            graph.add_edge(key, v)

    adj_list = graph.repr


    bfs = BFS(graph).bfs(start=k, end=b)
    print(graph)
    print(bfs)

    # visualizer ***********************************************************

    fig, ax = plt.subplots()
    ax.scatter(xs, ys)
    for index, node in enumerate(nodes):
        x = node.x
        y = node.y

        ax.text(node.x, node.y, node.id)
        for adj_node in adj_list[index]:
            ax.plot([x, nodes[int(adj_node)].x], [y, nodes[int(adj_node)].y], 'blue', alpha=0.2)

    pathx = []
    pathy = []
    for index,node in enumerate(bfs):
        pathx.append(nodes[int(node)].x)
        pathy.append(nodes[int(node)].y)

    ax.plot(pathx,pathy,'red')

    plt.show()


