import socket
from dataclasses import dataclass

class Map:
    def update_position(self):

@dataclass
class Package:
    cl_id: int
    cl_pos_x: int
    cl_pos_y: int

class Client:


HOST = "127.0.0.1"  # Стандартный интерфейс обратной петли (localhost)
PORT = 65432        # Порт для прослушивания (не привилегированные порты > 1023)


def start_server():
    # Создаем TCP/IP сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Привязываем сокет к порту
    server_address = (HOST, PORT)
    print(f'starting up on {server_address[0]} port {server_address[1]}')
    server_socket.bind(server_address)

    # Слушаем входящие соединения
    server_socket.listen(1)

    while True:
        print('waiting for a connection')
        connection, client_address = server_socket.accept()

        try:
            print(f'connection from {client_address}')

            while True:
                data = connection.recv(1024)
                print(f'received "{data}"')

                if data:
                    print('processing data')
                else:
                    print('no data from', client_address)
                    break

        finally:
            connection.close()


start_server()  # Запускаем сервер
