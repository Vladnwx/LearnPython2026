#!/bin/bash

echo "--- Создание структуры обучающих модулей ---"

# Массив с количеством задач для каждого из 6 модулей
tasks_per_module=(7 7 5 5 5 1)

for i in {1..6}; do
    # Форматируем имя папки (module_01, module_02...)
    dir_name="module_$(printf "%02d" $i)"
    
    # Создаем основную папку и подпапки
    mkdir -p "$dir_name/homework" "$dir_name/materials"
    
    # Количество задач для текущего модуля (берем из массива)
    num_tasks=${tasks_per_module[$((i-1))]}
    
    for j in $(seq 1 $num_tasks); do
        file_path="$dir_name/task_$j.py"
        # Создаем файл, только если он не существует
        if [ ! -f "$file_path" ]; then
            touch "$file_path"
            echo "print('Задание $j') # Заготовка" > "$file_path"
        fi
    done
done

echo "--- Структура готова ---"