from itertools import permutations

# Исходный список
data = [1, 2, 3]

perm = permutations(data, 2)

# Вывод всех размещений
for p in perm:
    print(p)
