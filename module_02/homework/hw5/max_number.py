"""
Реализуйте endpoint, начинающийся с /max_number, в который можно передать список чисел, разделённых слешем /.
Endpoint должен вернуть текст «Максимальное переданное число {number}»,
где number — выделенное курсивом наибольшее из переданных чисел.

Примеры:

/max_number/10/2/9/1
Максимальное число: 10

/max_number/1/1/1/1/1/1/1/2
Максимальное число: 2

"""

from flask import Flask

app = Flask(__name__)


@app.route("/max_number/<path:numbers_path>")
def max_number(numbers_path: str):
    # Разделяем строку по слешу
    raw_numbers = list(filter(None, numbers_path.split('/')))
    
    if not raw_numbers:
        return "Вы не передали ни одного числа.", 400

    try:
        # Преобразуем строки в числа
        numbers = [int(n) for n in raw_numbers]
        
        maximum = max(numbers)
        
        # Используем тег <i> для курсива, как в условии
        return f"Максимальное переданное число: <i>{maximum}</i>"
        
    except ValueError:
        return "Ошибка: переданы некорректные данные. Пожалуйста, вводите только числа.", 400


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
