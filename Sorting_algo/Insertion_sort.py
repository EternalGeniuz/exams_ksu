import random

lst = []
for i in range(10):
    lst.append(random.randint(1, 100))

N = len(lst)


def insertion_sort(lst):
    for i in range(1, N):
        t = lst[i]
        for j in range(i, 0, -1):
            k = lst[j]
            if lst[j] < lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
            else:
                break
    return lst


print(lst)
print(insertion_sort(lst))
