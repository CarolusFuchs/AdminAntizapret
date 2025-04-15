from http.server import HTTPServer, BaseHTTPRequestHandler
import socketserver

class RedirectHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Получаем хост из заголовков запроса
        host = self.headers['Host']
        # Формируем URL для редиректа
        # Добавляем порт 5050 в URL, так как он не включается автоматически
        new_url = f'https://{host}:5050{self.path}'
        # Отправляем код ответа 301 (постоянный редирект)
        self.send_response(301)
        self.send_header('Location', new_url)
        self.end_headers()

if __name__ == '__main__':
    # Создаем сервер, слушающий все интерфейсы на порту 5050
    httpd = socketserver.TCPServer(('0.0.0.0', 5050), RedirectHandler)
    print("HTTP Redirect Server running on port 5050...")
    httpd.serve_forever()