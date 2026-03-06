"""
Реализуйте endpoint, который показывает превью файла, принимая на вход два параметра: SIZE (int) и RELATIVE_PATH —
и возвращая первые SIZE символов файла по указанному в RELATIVE_PATH пути.

Endpoint должен вернуть страницу с двумя строками.
В первой строке будет содержаться информация о файле: его абсолютный путь и размер файла в символах,
а во второй строке — первые SIZE символов из файла:

<abs_path> <result_size><br>
<result_text>

где abs_path — написанный жирным абсолютный путь до файла;
result_text — первые SIZE символов файла;
result_size — длина result_text в символах.

Перенос строки осуществляется с помощью HTML-тега <br>.

Пример:

docs/simple.txt:
hello world!

/preview/8/docs/simple.txt
/home/user/module_2/docs/simple.txt 8
hello wo

/preview/100/docs/simple.txt
/home/user/module_2/docs/simple.txt 12
hello world!
"""

import os
from flask import Flask

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route("/head_file/<int:size>/<path:relative_path>")
def head_file(size: int, relative_path: str):
    abs_path = os.path.abspath(os.path.join(BASE_DIR, relative_path))
    print(abs_path)
    # Проверяем существование файла
    if not os.path.exists(abs_path):
        return f"Файл по адресу <b>{abs_path}</b> не найден", 404
    
    try:
        with open(abs_path, 'r', encoding='utf-8') as file:
            result_text = file.read(size)
            result_size = len(result_text)
            
        return (
            f"<b>{abs_path}</b> {result_size}<br>"
            f"{result_text}"
        )
    except Exception as e:
        return f"Ошибка при чтении файла: {e}", 500


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
