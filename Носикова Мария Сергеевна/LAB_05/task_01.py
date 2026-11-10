#!/usr/bin/env python3

import argparse

MIN_AGE = 0
MAX_AGE = 120

def parse_args():
    """
    Разбирает аргументы командной строки.

    :return: Оюъект с разобранными аргументами.
    """
    parser = argparse.ArgumentParser(
        prog='user_greeting',
        description='Скрипт, который приветсвует пользователя и выводит его возраст.',
        epilog='Всего хо-ро-ше-го!'
    )
    parser.add_argument('--name', nargs='+', type = str, help = 'Имя пользователя')
    parser.add_argument('age', nargs='?', type = int, default=None, help='Возраст пользователя (от 0 до 120 лет).')
    parser.add_argument('-w', '--welcome', action='store_true', help='Использовать официальное приветствие')
    return parser.parse_args()


def validate_age(age):
    """
    Проверяет корректность введнного возраста.

    :param age: проверяемый возраст.
    :return: Если возраст корректный - True, иначе False.
    """
    if age is None:
        return True
    if not isinstance(age, int):
        print("Ошибка! Возраст должен быть целым числом.")
        return False
    if age < MIN_AGE or age > MAX_AGE:
        print(f"Ошибка! Возраст должен быть целым числом от {MIN_AGE} до {MAX_AGE}.")
        return False


def user_greet(name, age, welcome):
    """
    Приветствует пользователя. ТАкже проверка на наличие имени.

    :param name: Имя пользователя.
    :param age: Возраст пользователя.
    :param welcome: Флаг официального приветствия.
    """
    if not args.name.strip():
        print("Ошибка! Имя не может быть пустым.")
        exit(2)
    if welcome:
        user_greeting = "Уважаемый(ая)"
    else:
        user_greeting = "Здравствуйте"

    if age is not None:
        print(f"{user_greeting}, {name}! Ваш возраст: {age} лет.")
    else:
        print(f"{user_greeting}, {name}!")


if __name__ == '__main__':
    args = parse_args()

    if not validate_age(args.age):
        exit(2)

    user_greet(args.name, args.age, args.welcome)
