import time
from collections import deque
from linked_list import SinglyLinkedList
from structures import Stack, Queue


def run_bench(name, func, n_iterations):
    start_time = time.time()
    func(n_iterations)
    end_time = time.time()
    print(f"{name:<35}: {end_time - start_time:.6f} сек")


def bench_stack_push(n):
    s = Stack()
    for i in range(n):
        s.push(i)


def bench_queue_enqueue(n):
    q = Queue()
    for i in range(n):
        q.enqueue(i)


def bench_ll_append(n):
    ll = SinglyLinkedList()
    for i in range(n):
        ll.append(i)


def bench_list_insert_0(n):
    l = []
    for i in range(n):
        l.insert(0, i)


def bench_deque_appendleft(n):
    d = deque()
    for i in range(n):
        d.appendleft(i)


def bench_ll_prepend(n):
    ll = SinglyLinkedList()
    for i in range(n):
        ll.prepend(i)


if __name__ == "__main__":
    N_APPEND = 100_000
    N_PREPEND = 30_000

    print(f"--- 1. Сравнение APPEND (Добавление в конец, N={N_APPEND}) ---")
    print("Ожидание: Все структуры работают за O(1), но List быстрее за счет реализации на C.")

    run_bench("Stack (List append)", bench_stack_push, N_APPEND)
    run_bench("Queue (Deque append)", bench_queue_enqueue, N_APPEND)
    run_bench("SinglyLinkedList (append)", bench_ll_append, N_APPEND)

    print(f"\n--- 2. Сравнение PREPEND (Добавление в начало, N={N_PREPEND}) ---")
    print("Ожидание: List работает за O(n) (медленно), остальные за O(1) (быстро).")

    run_bench("Python Standard List (insert 0)", bench_list_insert_0, N_PREPEND)
    run_bench("SinglyLinkedList (prepend)", bench_ll_prepend, N_PREPEND)
    run_bench("Standard Deque (appendleft)", bench_deque_appendleft, N_PREPEND)
