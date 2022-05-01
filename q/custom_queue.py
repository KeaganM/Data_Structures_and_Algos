from typing import Union, TypeVar, List, Optional
from collections import defaultdict

from heaps.heaps import MinHeap,MaxHeap

T = TypeVar('T')


class Queue:
    def __init__(self) -> None:
        self._q = []

    @property
    def q(self):
        return self._q

    def push(self, item: T) -> None:
        self._q.insert(0, item)

    def pop(self) -> T:
        return self._q.pop()

    def __repr__(self) -> str:
        return f'current Queue: {self._q} last item entered: {self._q[0] if self._q else None} next item to pop: {self._q[-1] if self._q else None}'


# class PriortyQueue:
#     def __init__(self) -> None:
#         self._q = []
#
#     @property
#     def q(self):
#         return [item['item'] for item in self._q]
#
#     def push(self, item: T) -> None:
#         self._q.insert(0, item)
#         q = sorted(self._q,key=lambda x:-x['cost']) # todo for now expects {item:Any,cost:int}
#         self._q = q.copy()
#
#     def pop(self) -> T:
#         return self._q.pop()['item']
#
#     def __repr__(self) -> str:
#         return f'current Queue: {self._q} next item to pop: {self._q[-1] if self._q else None}'


class PriortyQueue:
    def __init__(self,heap:Union[MinHeap,MaxHeap]):
        self.heap = heap()

    def push(self,item):
        self.heap.insert_key(item)
    def pop(self):
        return self.heap.pop()
    def __repr__(self):
        return f'Current Priority Queue:{self.heap.heap}'


if __name__ == '__main__':

    pq = PriortyQueue(MinHeap)
    pq.push(100)
    pq.push(200)
    pq.push(50)
    pq.push(75)
    i = pq.pop()
    print(pq)

    quit()
