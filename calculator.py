class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b


calc = Calculator
print('Введите 2 числа:')
a, b = map(int, input().split())
while a != 5:
    print('1.Сложить числа', '2. Вычесть числа', '3. Умножить числа', "4. Поделить числа", '5. Заново ввести числа', sep='\n')
    op = int(input())
    if op == 1:
        print('a + b = ', calc().add(a, b))
    elif op == 2:
        print('a - b = ', calc().subtract(a, b))
    elif op == 3:
        print('a * b = ', calc().multiply(a, b))
    elif op == 4:
        print('a / b = ', calc().divide(a, b))
    elif op == 5:
        print('Введите 2 числа через пробел:')
        a, b = map(int, input().split())
    else:
        break
