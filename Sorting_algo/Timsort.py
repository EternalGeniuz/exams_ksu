import random

MIN_RUN = 32

def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def create_runs(arr):
    n = len(arr)
    runs = []
    for start in range(0, n, MIN_RUN):
        end = min(start + MIN_RUN - 1, n - 1)
        insertion_sort(arr, start, end)
        runs.append((start, end))
    return runs


def merge(arr, left, mid, right):
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    len_left, len_right = len(left_part), len(right_part)
    i = j = 0
    k = left

    while i < len_left and j < len_right:
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    while i < len_left:
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len_right:
        arr[k] = right_part[j]
        j += 1
        k += 1


def timsort(arr):
    runs = create_runs(arr)

    while len(runs) > 1:
        new_runs = []
        for i in range(0, len(runs), 2):
            if i + 1 < len(runs):
                left, mid = runs[i]
                right = runs[i + 1][1]
                merge(arr, left, mid, right)
                new_runs.append((left, right))
            else:
                new_runs.append(runs[i])
        runs = new_runs


# Пример использования
arr = []
for i in range(10):
    arr.append(random.randint(-100, 101))

print(arr)
N = len(arr)
timsort(arr)
print(arr)  # Вывод: [1, 1, 2, 2, 2, 3, 3, 4, 5, 5, 5, 6, 7, 8, 9, 10]
