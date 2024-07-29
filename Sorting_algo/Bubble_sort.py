import os
import random
import time

import psutil

process = psutil.Process(os.getpid())
start_time = time.perf_counter()
lst = []
for i in range(4000000):
    lst.append(random.randint(1, 100))

N = len(lst)


def Bubble_sort(lst):
    for i in range(0, N - 1):
        for j in range(0, N - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return (lst)


print(lst)
print(sorted(lst))

end_time = time.perf_counter()

execution_time = end_time - start_time
print(f"Время выполнения: {execution_time:.4f} секунд")
memory_info = process.memory_info()
print(f"Использованная память: {memory_info.rss / 1024 ** 2:.2f} MB")


