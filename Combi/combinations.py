from itertools import combinations

# Исходный список
data = [1, 2, 3]

# Генерация всех комбинаций размера 2
comb = combinations(data, 2)

# Вывод всех комбинаций
for c in comb:
    print(c)
