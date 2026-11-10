#!/usr/bin/env python3

import argparse
import sys
import os

def parse_args():
    """
    Разбирает аргументы командной строки.

    :return: Объект с разобранными аргументами.
    """
    parser = argparse.ArgumentParser(
        prog='file_copier',
        description='Утилита для копирования файлов с возможностью замены текста и добавления подвала.',
        epilog='Будьте внимательны при указании путей к файлам!'
    )
    parser.add_argument('--input', type=str, required=True, help='Путь к входному файлу')
    parser.add_argument('--output', type=str, required=True, help='Путь к выходному файлу')
    parser.add_argument('--replace', type=str, default=None, help='Замена текста в формате OLD=NEW (заменяет все вхождения OLD на NEW)')
    parser.add_argument('--append-footer', type=str, default=None, help='Строка, которая будет добавлена в конец выходного файла')
    parser.add_argument('--overwrite', action='store_true', help='Разрешить перезапись существующего выходного файла')
    return parser.parse_args()


def parse_replace(replace_str):
    """
    Разбирает строку замены формата OLD=NEW.

    :param replace_str: Строка в формате 'OLD=NEW'.
    :return: Кортеж (old, new) или None при ошибке.
    """
    if '=' not in replace_str:
        print("Ошибка! Аргумент --replace должен быть в формате OLD=NEW.")
        return None
    old, new = replace_str.split('=', 1)
    if not old:
        print("Ошибка! OLD в формате OLD=NEW не может быть пустым.")
        return None
    return old, new
    

if __name__ == '__main__':
    args = parse_args()

    if not os.path.exists(args.input):
        print(f"Ошибка! Входной файл '{args.input}' не существует.")
        sys.exit(1)


    if os.path.exists(args.output) and not args.overwrite:
        print(f"Ошибка! Выходной файл '{args.output}' уже существует. Используйте флаг --overwrite для перезаписи.")
        sys.exit(1)


    try:
        with open(args.input, 'r', encoding='utf-8') as f:
            content = f.read()
    except IOError as e:
        print(f"Ошибка при чтении файла '{args.input}': {e}")
        sys.exit(1)


    total_replacement = 0
    if args.replace is not None:
        parsed = parse_replace(args.replace)
        if parsed is None:
            sys.exit(1)
        old, new = parsed
        total_replacement = content.count(old)
        content = content.replace(old, new)
        print(f"Выполнено замен: {total_replacement}")


    if args.append_footer is not None:
        if content and not content.endswith('\n'):
            content += '\n'
        content += args.append_footer + '\n'


    try:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Содержимое успешно скопировано в '{args.output}'.")
    except IOError as e:
        print(f"Ошибка при записи в файл '{args.output}': {e}")
        sys.exit(1)
