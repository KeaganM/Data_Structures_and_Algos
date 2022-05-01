'''
Why linked list of array/list:

- dynamic size
- ease of inseration/deletion

drawbacks:

- no random access allowed
- extra memory required (some sort of pointer-esque object required)
- not cache friendly; array elements are in contiguous locations (i.e. by each other in memory) while linked lists are
not

basic representation:

- pointer to the first node which is called the head
- each following node has a data attribute and a pointer to the next node


https://www.geeksforgeeks.org/linked-list-set-3-deleting-node/
'''
from typing import Union, TypeVar, List, Optional

T = TypeVar('T')


class Node:
    def __init__(self, data: T) -> None:
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return f'{self.data}'


class LinkedList:
    def __init__(self) -> None:
        self.head: Union[Node, None] = None

    def push(self, node: Node) -> None:
        node.next = self.head
        self.head = node

    def insert(self, prev_node: Node, next_node: Node) -> None:
        next_node.next = prev_node.next
        prev_node.next = next_node

    def append(self, node: Node) -> None:
        n = self.head
        while n.next:
            n = n.next
        n.next = node

    def remove(self, node: Node) -> None:
        ...

    def walk(self, node: Union[Node, None] = None) -> List[Node]:
        n = node if node else self.head
        print(n)
        l = [n]
        if n.next:
            l.extend(self.walk(n.next))
        return l


if __name__ == '__main__':
    print('Basics ' + '*' * 200)
    ll = LinkedList()
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)

    ll.head = n1
    n1.next = n2
    n2.next = n3

    ll.walk()
    print('Push ' + '*' * 200)

    n4 = Node(4)
    ll.push(n4)

    ll.walk()

    print('Insert ' + '*' * 200)

    n5 = Node(5)
    ll.insert(n2, n5)
    ll.walk()

    print('Append ' + '*' * 200)

    n6 = Node(6)
    ll.append(n6)
    ll.walk()

    quit()
