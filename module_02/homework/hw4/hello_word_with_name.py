"""
Реализуйте endpoint /hello-world/<имя>, который возвращает строку «Привет, <имя>. Хорошей пятницы!».
Вместо хорошей пятницы endpoint должен уметь желать хорошего дня недели в целом, на русском языке.

Пример запроса, сделанного в субботу:

/hello-world/Саша  →  Привет, Саша. Хорошей субботы!
"""

from flask import Flask
from datetime import datetime
import sys

weekdays_list = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
weekdays_tuple = tuple(weekdays_list)
weekdays_dict = {i: day for i, day in enumerate(weekdays_list)}

print(sys.getsizeof(weekdays_list))
print(sys.getsizeof(weekdays_tuple))
print(sys.getsizeof(weekdays_dict))

app = Flask(__name__)

# Используем кортеж
WEEKDAYS = (
    'понедельника',
    'вторника',
    'среды',
    'четверга',
    'пятницы',
    'субботы',
    'воскресенья'
)

@app.route('/hello-world/')
@app.route('/hello-world/<name>')
def hello_world(name: str = "Аноним"):
    # Получаем индекс текущего дня недели (0-6)
    weekday_index = datetime.today().weekday()
    # Правильное склонение прилагательного
    if weekday_index in (2, 4, 5):
        prefix = "Хорошей"
    else:
        prefix = "Хорошего"
        
    day_name = weekdays_tuple[weekday_index]
    return f"Привет, {name}. {prefix} {day_name}!"


@app.route('/')
def index():
    # Список всех эндпоинтов
    links = []
    for rule in app.url_map.iter_rules():
        if "static" not in rule.endpoint:
            url = rule.rule
            links.append(f'<li><a href="{url}">{url}</a></li>')
    
    return f"""
    <h1>Навигация по модулю 02</h1>
    <ul>
        {"".join(links)}
    </ul>
    """


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)