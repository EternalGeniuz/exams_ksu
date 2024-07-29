from itertools import permutations

# Исходный список
data = [1, 2, 3]

# Генерация всех перестановок
perm = permutations(data)

# Вывод всех перестановок
for p in perm:
    print(p)

print(' '.join(map(lambda x: ''.join(x), permutations('123'))))
