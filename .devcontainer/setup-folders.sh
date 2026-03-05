#!/bin/bash

echo "--- Инициализация сложной структуры проекта ---"

# 1. Создание уникальных подпапок для каждого модуля
echo "Создание специфических директорий..."

# Модуль 1
mkdir -p module_01/{homework,materials/first_application}

# Модуль 2
mkdir -p module_02/{homework/hw{1..7},materials/test}

# Модуль 3
mkdir -p module_03/{homework/hw{1..5},materials/{previous_hw_test/tests,testing_age/tests}}

# Модуль 4
mkdir -p module_04/{homework/{hw1_3,hw4,hw5},materials}

# Модуль 5
mkdir -p module_05/{homework/hw{1..5},materials/{context_managers,linux_process,working_with_processes_from_python}}

# Модуль 6 (Web-structure)
mkdir -p module_06/{homework/new_year_application/{static/{css/overlays,images/overlays,js},templates},materials}

# 2. Создание файлов задач (task_n.py)
echo "Проверка файлов задач..."

declare -A task_counts=( [1]=7 [2]=7 [3]=5 [4]=5 [5]=5 [6]=1 )

'''
for i in {1..6}; do
    module_dir="module_$(printf "%02d" $i)"
    count=${task_counts[$i]}
    
    for j in $(seq 1 $count); do
        file="$module_dir/task_$j.py"
        if [ ! -f "$file" ]; then
            echo "# Task $j" > "$file"
        fi
    done
done
'''

echo "--- Синхронизация завершена успешно ---"