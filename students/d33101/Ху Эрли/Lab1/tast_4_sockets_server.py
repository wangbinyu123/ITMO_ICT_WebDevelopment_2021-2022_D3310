# -*- coding:utf-8 -*-
"""
作者:酷酷酷
日期:2021年09月21日
"""
import socket, threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Создание сокетов， IPV4， TCP
host = '127.0.0.1'
port = 8888                        #Адрес
server.bind((host, port))          #Привязка адреса и порта
server.listen()                  #Настройка слушателя

clients = []
users = []


def broadcast(msg, client):
    for each in clients:
        if each != client:      #Отправьте сообщение каждому второму клиенту
            each.send(msg)


def handle(client):
    while True:
        msg = client.recv(2048)  #Получение информации
        broadcast(msg, client)


def receive():
    while True:
        client, addr = server.accept()      # Принимает запрос на соединение от клиента и возвращает новый сокет и адрес
        client.send('username'.encode())    # Отправить байтовую строку ’username‘
        user = client.recv(2048).decode()    # Получение байтовых строк
        clients.append(client)          # Добавление клиентов в список клиентов
        users.append(user)              # Добавить пользователя в список пользователей
        client.send('Connection established'.encode())      # Отправка байтовых строк
        thread = threading.Thread(target=handle, args=(client,))    #Внедрение многопоточности
        thread.start()    #Включение многопоточности


receive()
