from itertools import chain, combinations

def powerset(iterable):
    xs = list(iterable)
    return chain.from_iterable(combinations(xs, n) for n in range(len(xs) + 1))

# Пример использования
data = [1, 2, 3]
for subset in powerset(data):
    print(subset)
