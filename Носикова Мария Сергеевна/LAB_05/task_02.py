#!/usr/bin/env python3

import argparse

OPTIONAL_ARG =  ['add', 'sub', 'mul', 'div']
PRECISION_ARG = 2

def parse_args():
    """
    Разбирает аргументы командной строки.

    :return: Объект с разобранными аргументами.
    """
    parser = argparse.ArgumentParser(
        prog='calculator',
        description='Калькулятор, выполняющий операции над двумя числами и сохраняет результат.',
    )

    parser.add_argument('x', type=float, help='Первое число')
    parser.add_argument('y', type=float, help='Второе число')
    parser.add_argument('-o', '--operation', type=str, choices=OPTIONAL_ARG, default=None, help='Операция: add, sub, mul, div. Если не указана - просто выводим числа.')
    parser.add_argument('-p', '--precision', type=int, default=PRECISION_ARG, help=f'Количество знаков после запятой (по умолчанию {PRECISION_ARG})')
    parser.add_argument('-f', '--file', type=str, default=None, help='Название файла для сохранения результата')
    return parser.parse_args()


def my_best_calculate(x, y, operation, precision):
    """
    Выполняет математические операции над 2мя числами.

    :param x: Первое число.
    :param y: Второе число.
    :param operation: Операция (add, sub, mul, div).
    :param precision: Количество знаков после запятой.
    :return: Результат вычисления или None при ошибке.
    """
    if operation == 'add':
        result = x + y
    elif operation == 'sub':
        result = x-y
    elif operation == 'mul':
        result = x * y
    elif operation == 'div':
        if y == 0:
            print("Ошибка! Делить на ноль нельзя.")
            return None
        result = x / y
    else: 
        return None
    return round(result, precision)


def save_to_file(filename, text):
    """
    Сохраняет текст в файл, добавляя в конец, но не перезаписывает.

    :param filename: Имя файла.
    :param text: Текст для записи.
    """
    try:
        with open(filename, 'a', encoding='utf-8') as f:
            f.write(text + '\n')
        print(f"Результат осхранен в файл '{filename}'.")
    except IOError as e:
        print(f"Ошибка при записи в файл: {e}")


if __name__ == '__main__':
    args = parse_args()
    if args.operation is None:
        print(f"Число 1: {args.x}")
        print(f"Число 2: {args.y}")
        if args.file:
            save_to_file(args.file, f"Число 1: {args.x}, Число 2: {args.y}")
    else: 
        result = my_best_calculate(args.x, args.y, args.operation, args.precision)
        if result is None:
            exit(1)
        print(f"результат: {args.x} {args.operation} {args.y} = {result}")
        if args.file:
            save_to_file(args.file, f"{args.x} {args.operation} {args.y} = {result}")
