"""
С помощью команды ps можно посмотреть список запущенных процессов.
С флагами aux эта команда выведет информацию обо всех процессах, запущенных в системе.

Запустите эту команду и сохраните выданный результат в файл:

$ ps aux > output_file.txt

Столбец RSS показывает информацию о потребляемой памяти в байтах.

Напишите функцию get_summary_rss, которая на вход принимает путь до файла с результатом выполнения команды ps aux,
а возвращает суммарный объём потребляемой памяти в человекочитаемом формате.
Это означает, что ответ надо перевести в байты, килобайты, мегабайты и так далее.
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_TO_OUTPUT_FILE = os.path.join(BASE_DIR, 'output_file.txt')

def get_summary_rss(ps_output_file_path: str) -> str:
    if not os.path.exists(ps_output_file_path):
        return f"Ошибка: файл '{ps_output_file_path}' не найден"
    
    total_rss_kib = 0

    with open(ps_output_file_path, 'r', encoding='utf-8') as file:
        # Пропускаем заголовок и читаем строки
        lines = file.readlines()[1:]
        for line in lines:
            columns = line.split()
            if len(columns) >= 6:
                total_rss_kib += int(columns[5])

    # Конвертация в человекочитаемый формат (байты)
    value = total_rss_kib * 1024
    
    # Список единиц измерения (бинарные префиксы)
    for unit in ['B', 'KiB', 'MiB', 'GiB', 'TiB']:
        if value < 1024.0:
            return f"{value:.2f} {unit}"
        value /= 1024.0
    return f"{value:.2f} PiB"

if __name__ == '__main__':
    path: str = PATH_TO_OUTPUT_FILE
    # Проверяем, передал ли пользователь путь через терминал
    if len(sys.argv) > 1:
        path = sys.argv[1]
    summary_rss: str = get_summary_rss(path)
    print(summary_rss)
