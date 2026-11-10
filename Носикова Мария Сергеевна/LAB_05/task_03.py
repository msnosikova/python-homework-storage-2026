#!/usr/bin/env python3

import argparse
import sys

def parse_args():
    """
    Разбирает аргументы кмоандной строки.

    :return: Объект с разобранными аргументами.
    """
    parser = argparse.ArgumentParser(
        prog='string_processor',
        description='Скрипт для обработки, фильтрации и сортировки строк.', 
        epilog='Будьте, пожалуйста, очень внимательны при вводе аргументов!'
    )

    parser.add_argument('strings', nargs = '*', type = str, help='Одна или несколько строк для обработки')
    parser.add_argument('-c', '--count', action='store_true', help='Вывести только количество строк после фильтрации')
    parser.add_argument('-u', '--unique', action = 'store_true', help ='Оставить только уникальные строки')
    parser.add_argument('-l', '--min-length', type=int, default=0, help='Минимальная длина строки для выввода(по умолчанию 0)')
    parser.add_argument('-s', '--sort', type=str, default='none', help='Сортировка: asc (по возрастанию), desc (по убыванию), none (без сортировки)')

    return parser.parse_args()


def work_on_str(strings, min_length, unique, sort_mode):
    """
    Фильтрует и сортирует список строк, возвращая кортеж.

    :param strings: Исходный список строк.
    :param min_length: Минимальная лопустимая длина.
    :param unique: Флаг уникальность.
    :param sort_mode: Режим сортировки ('asc', 'desc', 'none').
    :return: Обработанный кортеж строк.
    """
    result = [s for s in strings if len(s) >= min_length]

    if unique:
        result = list(dict.fromkeys(result))

    if sort_mode == 'asc':
        return tuple(sorted(result))
    elif sort_mode == 'desc':
        return tuple(sorted(result, reverse=True))
    return tuple(result)


if __name__ == '__main__':
    args = parse_args()
    if not args.strings:
        print("Ошибка! Вы не передали ни одной строки. Пожалуйста!! Укажите хотя бы одну!!")
        sys.exit(1)

    if args.sort not in ('asc', 'desc', 'none'):
        print(f"Ошибка! Неизвестное значение для --sort: '{args.sort}'. Допустимые значения: asc, desc, none")
        sys.exit(1)

    processing = work_on_str(args.strings, args.min_length, args.unique, args.sort)

    if args.count:
        print(f"Количество строк: {len(processing)}")
    else: 
        for line in processing:
            print(line)
