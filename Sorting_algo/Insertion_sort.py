import random

lst = []
for i in range(2000000):
    lst.append(random.randint(1, 100))

N = len(lst)


def insertion_sort(lst):
    for i in range(1, N):
        for j in range(i, 0, -1):
            if lst[j] < lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
            else:
                break
    return lst


print(lst)
print(insertion_sort(lst))
