from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape


# Поиск HTML-шаблона
env = Environment(
    loader=FileSystemLoader('.'), # Шаблон нужно искать в текущем каталоге
    autoescape=select_autoescape(['html', 'xml']) # Стандартные настройки для работы с HTML
)
# В переменную template загружается шаблон из файла template.html
template = env.get_template('template.html')

# Список кепок
caps = [
    {
        "title": "Красная кепка",
        "price": "$ 100.00",
        # "image": "https://dvmn.org/filer/canonical/1569333143/329/"
    },
    {
        "title": "Чёрная кепка",
        "price": "$ 120.00",
        "image": "https://dvmn.org/filer/canonical/1569333143/330/"
    },
    {
        "title": "Ещё одна чёрная кепка",
        "price": "$ 90.00",
        "image": "https://dvmn.org/filer/canonical/1569333144/331/"
    },
    {
        "title": "Камуфляжная кепка",
        "price": "$ 100.00",
        "image": "https://dvmn.org/filer/canonical/1569943835/350/"
    },
    {
        "title": "Джинсовая кепка",
        "price": "$ 100.00",
        "image": "https://dvmn.org/filer/canonical/1569943835/351/"
    },
    {
        "title": "Плоская кепка",
        "price": "$ 100.00",
        "image": "https://dvmn.org/filer/canonical/1569943836/352/"
    }
]

# Значения аргументов
# В переменной rendered_page лежит новый HTML, с подставленными значениями
rendered_page = template.render(caps=caps)

# Сохранение строки HTML в файл index.html
with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

# Запуск веб-сервера
server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
