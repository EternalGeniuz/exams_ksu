import random

lst = []
for i in range(20):
    lst.append(random.randint(1, 30))

N = len(lst)


def selection_sort(lst):
    for i in range(N - 1):
        t = lst[i]
        index = i

        for j in range(i + 1, N):

            if lst[j] < t:
                t = lst[j]
                index = j

        if index != i:
            temp = lst[i]
            lst[i] = lst[index]
            lst[index] = temp

    return lst


print(lst)
print(selection_sort(lst))
