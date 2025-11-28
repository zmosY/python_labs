from collections import deque

class Stack:
    def __init__(self, data: list = []):
        self._data = data

    def push(self, item):
        self._data.append(item)

    def pop(self):
        return self._data.pop()

    def peek(self):
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)


# test Stack
# q = Stack([])
# q.push(5)
# q.push(3)
# print(q.pop())
# print(q.peek())
# print(q.__len__())
# print(q.is_empty())
# q.pop()
# print(q.is_empty())


class Queue:
    def __init__(self, data: deque = []):
        self._data = data

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if self._data == []:
            raise IndexError("Queue is empty")
        else:
            return self._data.pop()

    def peek(self):
        if self._data == []:
            return None
        return self._data[-1]

    def is_empty(self):
        if self._data == []:
            return True
        else:
            return False

    def __len__(self):
        return len(self._data)

#test Qeque
# q = Queue()
# q.enqueue(1)
# q.enqueue(32)
# print(q.dequeue())
# print(q.peek())
# print(q.__len__())
# print(q.is_empty())
# q.dequeue()
# print(q.is_empty())