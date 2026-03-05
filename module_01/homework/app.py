from datetime import datetime, timedelta
import random
import os
import re
from flask import Flask

app = Flask(__name__)


@app.route('/hello_world')
def hello_world():
    return f'Привет, мир!'


CARS_STRING = "Chevrolet, Renault, Ford, Lada"
CARS_LIST = CARS_STRING.split(", ")

@app.route('/cars')
def cars():
    return ", ".join(CARS_LIST)

CATS_STRING = "корниш-рекс, русская голубая, шотландская вислоухая, мейн-кун, манчкин"
CATS_LIST = CATS_STRING.split(", ")

@app.route('/cats')
def cats():
    return random.choice(CATS_LIST)


@app.route('/get_time/now')
def get_time_now():
    #Используется время сервера, на котором запущен процесс вероятно UTC+0
    now = datetime.now()
    # Форматируем его в строку (часы:минуты:секунды)
    current_time = now.strftime("%H:%M:%S")
    # Используем переменную при форматировании итоговой строки
    return f"Точное время: {current_time}"


@app.route('/get_time/future')
def get_time_future():
    now = datetime.now()
    # Вычисляем время через час
    future_time = now + timedelta(hours=1)
    # Форматируем результат в строку
    current_time_after_hour = future_time.strftime("%H:%M:%S")
    # Формируем итоговый ответ
    return f"Точное время через час будет {current_time_after_hour}"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')

#Напрашивается решение с листом и возможно оно стандартное, 
# но чтобы убрать формальное решение предлагаю немного улучшить 
# ситуацию с занимаемой памятью.
#Используем только уникальные значения, которые сохраним в нижнем регистре,
#так как это те же слова. 
# Даже при таком подходе мне не нравится возможные действия OOM killer
# возможно более правильным решением было передвигать позицию байта в чтении
#  и делать небольшой массив из 10-20 слов, чтобы проверять на уникальность 
# в последних ответах и пропускать
def get_words(file_path: str) -> list[str]:
    if not os.path.exists(file_path):
        return []
    
    with open(file_path, 'r', encoding='utf-8') as book:
        unique_set = {word.lower() for word in re.findall(r'\b\w+\b', book.read())}
        return list(unique_set)


ALL_WORDS = get_words(BOOK_FILE)

@app.route('/get_random_word')
def get_random_word():
    random_word = random.choice(ALL_WORDS)
    return random_word

@app.route('/counter')
def counter():
    counter.visits += 1
    return f'Эта страница открывалась <b>{counter.visits}</b> раз(а)'

counter.visits = 0


@app.route('/')
def index():
    # Список всех эндпоинтов
    links = []
    for rule in app.url_map.iter_rules():
        if "static" not in rule.endpoint:
            url = rule.rule
            links.append(f'<li><a href="{url}">{url}</a></li>')
    
    return f"""
    <h1>Навигация по модулю 01</h1>
    <ul>
        {"".join(links)}
    </ul>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
