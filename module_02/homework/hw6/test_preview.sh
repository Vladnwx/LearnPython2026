#!/bin/bash

# Настройки
URL="http://localhost:5000/head_file"
TEST_DIR="test_docs"
TEST_FILE="$TEST_DIR/test.txt"

# 1. Подготовка: создаем тестовый файл
mkdir -p $TEST_DIR
echo -n "hello world!" > $TEST_FILE

echo "--- ЗАПУСК ТЕСТОВ PREVIEW ---"

# Тест 1: Чтение части файла (8 символов)
echo -n "Тест 1 (чтение 8 симв.): "
response=$(curl -s "$URL/8/$TEST_FILE")
if echo "$response" | grep -q "hello wo" && echo "$response" | grep -q "8"; then
    echo "✅ OK"
else
    echo "❌ FAIL (Ожидали 'hello wo' и размер 8)"
fi

# Тест 2: Чтение больше, чем есть в файле (100 символов)
echo -n "Тест 2 (чтение 100 симв.): "
response=$(curl -s "$URL/100/$TEST_FILE")
if echo "$response" | grep -q "hello world!" && echo "$response" | grep -q "12"; then
    echo "✅ OK"
else
    echo "❌ FAIL (Ожидали полный текст и размер 12)"
fi

# Тест 3: Проверка жирного шрифта в пути
echo -n "Тест 3 (проверка <b> в пути): "
curl -s "$URL/8/$TEST_FILE" | grep -q "<b>/.*$TEST_FILE</b>" && echo "✅ OK" || echo "❌ FAIL"

# Тест 4: Файл не существует
echo -n "Тест 4 (404 Not Found): "
curl -s -o /dev/null -w "%{http_code}" "$URL/10/no_exists.txt" | grep -q "404" && echo "✅ OK" || echo "❌ FAIL"

echo "------------------------------"
echo "Очистка временных файлов..."
rm -rf $TEST_DIR

echo "--- ТЕСТИРОВАНИЕ ЗАВЕРШЕНО ---"
