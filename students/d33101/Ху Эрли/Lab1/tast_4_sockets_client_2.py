# -*- coding:utf-8 -*-
"""
作者:酷酷酷
日期:2021年09月21日
"""
import socket
import threading  #Импорт многопоточности


conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Создание сокетов， IPV4， TCP
server = '127.0.0.1', 8888  #Адрес
conn.connect(server) #Подключение к серверу

username = input('Выберите псевдоним: ')


def recv_msg():
    while True:
        msg = conn.recv(2048).decode()  #Получение информации
        if msg == 'username':
            conn.send(username.encode()) #Получение информации
        else:
            print(msg)


def print_msg():
    while True:
        msg = '{} says: {}'.format(username, input('')) #Модуль, который продолжает зацикливать это входное сообщение и отправляет его
        conn.send(msg.encode())


recv_thr = threading.Thread(target=recv_msg) #Instantiation
print_thr = threading.Thread(target=print_msg)
recv_thr.start() #Включение многопоточности
print_thr.start() #Включение многопоточности