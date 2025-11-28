class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def prepend(self, value):
        new_node = Node(value, next=self.head)
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self._size += 1

    def insert(self, idx, value):
        if idx < 0 or idx > self._size:
            raise IndexError(f"Index {idx} out of bounds for size {self._size}")
        if idx == 0 or idx == self._size:
            self.prepend(value)
            return
        cur = self.head
        for n in range(idx - 1):
            cur = cur.next
        new_node = Node(value, next=cur.next)
        cur.next = new_node
        self._size += 1

    def remove(self, value):
        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return

        cur = self.head
        while cur.next is not None:
            if cur.next.value == value:
                if cur.next == self.tail:
                    self.tail = cur

                cur.next = cur.next.next
                self._size -= 1
                return
            cur = cur.next

        raise ValueError(f"{value} not in list")

    def __len__(self):
        return self._size

    def __iter__(self):
        cur = self.head
        while cur is not None:
            yield cur.value
            cur = cur.next

    def __repr__(self):
        values = list(self)
        return f"SinglyLinkedList({values})"


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    # Добавил repr для Node, чтобы при отладке было видно, что внутри
    def __repr__(self):
        return f"Node({self.value})"


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def prepend(self, value):
        new_node = Node(value, next=self.head)
        self.head = new_node
        if self.tail is None:
            self.tail = new_node
        self._size += 1

    def insert(self, idx, value):
        if idx < 0 or idx > self._size:
            raise IndexError(f"Index {idx} out of bounds for size {self._size}")

        if idx == 0:
            self.prepend(value)
            return

        # ИСПРАВЛЕНИЕ: Если индекс равен размеру, это вставка в КОНЕЦ (append)
        if idx == self._size:
            self.append(value)
            return

        cur = self.head
        for n in range(idx - 1):
            cur = cur.next
        new_node = Node(value, next=cur.next)
        cur.next = new_node
        self._size += 1

    def remove(self, value):
        if self.head is None:
            raise ValueError(f"{value} not in list")

        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            self._size -= 1
            return

        cur = self.head
        while cur.next is not None:
            if cur.next.value == value:
                if cur.next == self.tail:
                    self.tail = cur

                cur.next = cur.next.next
                self._size -= 1
                return
            cur = cur.next

        raise ValueError(f"{value} not in list")

    def __len__(self):
        return self._size

    def __iter__(self):
        cur = self.head
        while cur is not None:
            yield cur.value
            cur = cur.next

    def __repr__(self):
        values = list(self)
        return f"SinglyLinkedList({values})"


#test SinglyLinkedList
# ll = SinglyLinkedList()
# print(f"1. Пустой список: {ll}")
# ll.append(10)
# ll.append(20)
# ll.append(30)
# print(f"2. Добавление в конец (10, 20, 30): {ll}")
# ll.prepend(5)
# print(f"3. Добавление в начало (5): {ll}")
# ll.insert(2, 15)
# print(f"4. Вставка 15 по индексу 2: {ll}")
# ll.insert(0, 1)
# print(f"5. Вставка 1 по индексу 0: {ll}")
# ll.insert(6, 100)
# print(f"6. Вставка 100 в конец: {ll}")
# ll.remove(15)
# print(f"7. Удаление 15 (середина): {ll}")
# ll.remove(1)
# print(f"8. Удаление 1 (голова): {ll}")
# ll.remove(100)
# print(f"9. Удаление 100 (хвост): {ll}")
# print(f"10. Размер: {len(ll)}")
# print(f"11. Пуст ли список? {len(ll) == 0}")