class Stack:
    def __init__(self):
        self._s = list()

    def push(self, item):
        self._s.append(item)

    def peek(self):
        return self._s[-1]

    def pop(self):
        return self._s.pop(-1)

    def items(self):
        return self._s

    def __repr__(self):
        return f'stack: {self._s}'