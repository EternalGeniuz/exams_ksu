import os
import sys
import time

import psutil

special_chars = "This is \"a new line\nThis is a tab\tEnd of the string"
print(special_chars)

list1 = ["apple", "banana", "cherry"]
list2 = [1, 2, 3]
print("-".join(list1))  # apple, banana, cherry


def func(a: int, b: str) -> int:
    c = len(b) * a
    return c


print(func(10, 'str'))

c = lambda x: x / 10

print(c(10))


def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


display_info(name="Alice", age=30)


def print_list(lst):
    if not lst:  # Базовый случай: пустой список
        return
    else:
        print(lst[0])  # Печать первого элемента
        print_list(lst[1:])  # Рекурсивный вызов с остатком списка


print_list([1, 2, 3, 4, 5])

# Вызов функции
process = psutil.Process(os.getpid())
start_time = time.perf_counter()


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


end_time = time.perf_counter()

execution_time = end_time - start_time
print(f"Время выполнения рекурсии: {execution_time:.4f} секунд")
memory_info = process.memory_info()
print(f"Использованная память для рекурсии: {memory_info.rss / 1024 ** 2:.2f} MB")

process = psutil.Process(os.getpid())
start_time = time.perf_counter()


def factorial_cycle(n):
    fct = 1
    for i in range(1, n + 1):
        fct *= i
    return fct


execution_time = end_time - start_time
print(f"Время выполнения цикла: {execution_time:.4f} секунд")
memory_info = process.memory_info()
print(f"Использованная память для цикла: {memory_info.rss / 1024 ** 2:.2f} MB")

sys.setrecursionlimit(2000)
# print(factorial(2000))
print(factorial_cycle(1500))

a = 2
try:
    a /= 1
except ZeroDivisionError:
    print("Bad calculus!")
finally:
    print(a)

t = dict([(1, 'ggg'), (2, 2), (3, 3)])
print(t[1])

x = lambda y: y + 5
print(x(3))


class Slack:
    def __init__(self):
        self.exists = True

    def __getattr__(self, name):
        print('Вызов __getattr__({})'.format(name))
        value = 'Значение для {}'.format(name)
        setattr(self, name, value)
        return value


data = Slack()
print(data.foo)
data.foo = 13
print(data.foo)


class Stranger:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return str(self.x)

    def __call__(self, n=5):
        print('Вызов метода __call__')
        return (self.x * n)

    @classmethod
    def z(self, n=7):
        return self(n)


s = Stranger(3)
z = s()
print(f"Объект класса Stranger: {z}")
name = 5
Name = 6
print(name, Name)

print([] or {} or 0)

print("good" if 2 > 1 else "bad")

a = 2
b = 4
x = lambda c: a if a > c else c

print(x(4))
b = '4'
print(x(1))

int

list

