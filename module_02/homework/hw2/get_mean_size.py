"""
Удобно направлять результат выполнения команды напрямую в программу с помощью конвейера (pipe):

$ ls -l | python3 get_mean_size.py

Напишите функцию get_mean_size, которая на вход принимает результат выполнения команды ls -l,
а возвращает средний размер файла в каталоге.
"""

import sys


def get_mean_size(ls_output: str) -> float:
    total_size = 0
    file_count = 0
    for line in ls_output:
        columns = line.split()
        # В стандартном выводе ls -l информация о файле содержит как минимум 9 столбцов
        if len(columns) >= 9:
            try:
                print(f"DEBUG: учитываю файл {columns[-1]}") 
                # Размер файла — это 5-й столбец (индекс 4)
                file_size = int(columns[4])
                total_size += file_size
                file_count += 1
            except (ValueError, IndexError):
                # Пропускаем строки, где 5-й столбец не является числом
                continue

    # Обрабатываем случай, когда файлов нет, чтобы избежать деления на ноль
    if file_count == 0:
        return 0.0

    return total_size / file_count


#Оффтоп: ls -l > ls.txt Bash сначала очищает (обнуляет) файл ls.txt.
# Затем выполняется команда ls -l.
# В этот момент ls видит, что файл ls.txt существует, но он пустой (0 байт).
# Этот нулевой размер попадает в вывод и записывается в файл 
# Поэтому вывод из файла python3 get_mean_size.py < ls.txt и 
# cat ls.txt | python3 get_mean_size.py 1566.00 байт 
# а ls -l | python3 get_mean_size.py - значение больше, 
# т.к. он уже учитывает заполненный ls.txt

if __name__ == '__main__':
    data: str = sys.stdin.readlines()[1:]
    if not data:
        print("Данные не получены или каталог пуст.")
    else:
        mean_size = get_mean_size(data)
        if mean_size == 0:
            print("Файлы не найдены или их размер не определен.")
        else:
            print(f"Средний размер файла: {mean_size:.2f} байт")
