from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape


# Поиск HTML-шаблона
env = Environment(
    loader=FileSystemLoader('.'), # Шаблон нужно искать в текущем каталоге
    autoescape=select_autoescape(['html', 'xml']) # Стандартные настройки для работы с HTML
)
# В переменную template загружается шаблон из файла template.html
template = env.get_template('template.html')

# Значения аргументов
# В переменной rendered_page лежит новый HTML, с подставленными значениями
rendered_page = template.render(
    cap1_title="Красная кепка",
    cap1_text="$ 100.00",
    cap2_title="Чёрная кепка",
    cap2_text="$ 120.00",
    cap3_title="Ещё одна чёрная кепка",
    cap3_text="$ 90.00",
)

# Сохранение строки HTML в файл index.html
with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

# Запуск веб-сервера
server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
