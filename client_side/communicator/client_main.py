import socket
import pygame
import sys

# Настройки сервера
HOST = "127.0.0.1"  # Имя хоста или IP-адрес сервера
PORT = 65432        # Порт, используемый сервером

# Инициализация Pygame
pygame.init()
size = width, height = (640, 480)
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

# Настройки клиента
client_position = [width // 2, height // 2]

# Создаем TCP/IP сокет
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            client_position[1] -= 1
        if keys[pygame.K_s]:
            client_position[1] += 1
        if keys[pygame.K_a]:
            client_position[0] -= 1
        if keys[pygame.K_d]:
            client_position[0] += 1

        # Отправляем координаты на сервер
        s.sendall(f"{client_position[0]},{client_position[1]}".encode())

        # Получаем данные от сервера (необязательно)
        data = s.recv(1024)
        print(f"Received {data!r}")

        # Отрисовываем белую плоскость и точку
        screen.fill(black)
        pygame.draw.circle(screen, (255, 255, 255), client_position, 10)
        pygame.display.flip()
        pygame.time.delay(10)

