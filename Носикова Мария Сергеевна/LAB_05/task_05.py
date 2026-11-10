#!/usr/bin/env python3

import argparse
import sys
import random
import string

MIN_LENGTH = 8
MAX_LENGTH = 64

def parse_args():
    """
    Разбирает аргументы командной строки.

    :return: Объект с разобранными аргументами.
    """
    parser = argparse.ArgumentParser(
        prog='password_generator',
        description='Утилита для генерации случайных паролей.',
        epilog='Используйте надежные пароли и не забывайте их!'
    )
    parser.add_argument('length', type=int, help='Длина пароля (от 8 до 64 символов)')
    parser.add_argument('count', type=int, help='Количество паролей для генерации')
    parser.add_argument('--no-digits', action='store_true', help='Исключить цифры из пароля')
    parser.add_argument('--no-special', action='store_true', help='Исключить специальные символы из пароля')
    parser.add_argument('-f', '--file', type=str, default=None, help='Файл для сохранения сгенерированных паролей')
    return parser.parse_args()


def generate_passwords(length, count, no_digits, no_special):
    """
    Генерирует список паролей и возвращает их в виде неизменяемого кортежа.

    :param length: Длина каждого пароля.
    :param count: Количество паролей.
    :param no_digits: Флаг исключения цифр.
    :param no_special: Флаг исключения специальных символов.
    :return: Кортеж сгенерированных паролей.
    """
    pool = string.ascii_letters
    if not no_digits:
        pool += string.digits
    if not no_special:
        pool += string.punctuation

    passwords = []
    for _ in range(count):
        password = ''.join(random.choice(pool) for _ in range(length))
        passwords.append(password)
    return tuple(passwords)


def save_to_file(filename, passwords):
    """
    Сохраняет кортеж паролей в файл.

    :param filename: Имя файла.
    :param passwords: Кортеж паролей.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for pwd in passwords:
                f.write(pwd + '\n')
        print(f"Пароли успешно сохранены в файл '{filename}'.")
    except IOError as e:
        print(f"Ошибка при записи в файл '{filename}': {e}")


if __name__ == '__main__':
    args = parse_args()

    if not (MIN_LENGTH <= args.length <= MAX_LENGTH):
        print(f"Ошибка! Длина пароля должна быть в диапазоне от {MIN_LENGTH} до {MAX_LENGTH}.")
        sys.exit(1)


    if args.count <= 0:
        print("Ошибка! Количество паролей должно быть больше нуля.")
        sys.exit(1)


    generated_passwords = generate_passwords(
        args.length, 
        args.count, 
        args.no_digits, 
        args.no_special
    )


    print(f"Сгенерировано {args.count} паролей длиной {args.length} символов:")
    for pwd in generated_passwords:
        print("-", pwd)

    if args.file:
        save_to_file(args.file, generated_passwords)
