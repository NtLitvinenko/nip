import socket

def start_client():
    # Создаем сокет IPv6
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Подключаемся к серверу
    client_socket.connect(('127.0.0.1', 42))

    print("Соединение с сервером установлено")

    # Отправляем запрос серверу
    request = input("Request: ").encode()
    client_socket.send(request)

    # Принимаем ответ от сервера
    response = client_socket.recv(1024)
    print(f"Ответ от сервера: {response.decode()}")

    # Закрываем соединение
    client_socket.close()

if __name__ == "__main__":
    start_client()
