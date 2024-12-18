def sum_nums(a, b):
    return a + b

def sub_nums(a, b):
    return a - b

def multiply_nums(a, b):
    return a * b

def divide_nums(a, b):
    if b == 0:
        raise ZeroDivisionError('Ошибка деления на ноль.')
    return a / b

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка ввода, введите корректное число!")

while True:
    print('Выберите операцию:\n1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление\nQ - Выход')
    choice = input('Введите номер действия: ').strip().lower()
    if choice not in ('1', '2', '3', '4', 'q'):
        print('Введена неверная операция')
        continue
    if choice == 'q':
        print('Выход из программы!')
        break

    num1 = get_number('Введите первое число: ')
    num2 = get_number('Введите второе число: ')

    if choice == '1':
        print(sum_nums(num1, num2))
    elif choice == '2':
        print(sub_nums(num1, num2))
    elif choice == '3':
        print(multiply_nums(num1, num2))
    elif choice == '4':
        try:
            print(divide_nums(num1, num2))
        except ZeroDivisionError as zde:
            print(zde)
            continue
