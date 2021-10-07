#client.py
import socket
import json
import re
from threading import Thread

ADDRESS = ('127.0.0.1',12321)
USERNAME = ""

def init_connection():
    connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    connection.connect(ADDRESS)
    print(connection.recv(1024).decode('utf-8'))
    send_msg(connection,'act_connect','','s')
    return connection

def get_msg(socket1):
    while True:
        data = socket1.recv(1024).decode('utf-8')
        jdata = json.loads(data)
        print(f"\n{jdata['from']}:\n{jdata['data']}")

def send_msg(client, cmd, data, target):
    global USERNAME
    jdata = {}
    jdata['cmd'] = cmd
    jdata['target'] = target
    jdata['from'] = USERNAME
    jdata['data'] = data
    jstr = json.dumps(jdata)
    client.sendall(jstr.encode('utf-8'))

def get_username():
    global USERNAME
    while True:
        USERNAME = input("USERNAME:")
        if re.search(r'\w',USERNAME) is None:
            print("User NAME CAN NOT BE NONE!")
        else:
            break
    

if __name__ == "__main__":
    get_username()
    connection = init_connection()
    t1 = Thread(target=get_msg, args=(connection,))
    t1.setDaemon(True)
    t1.start()
    while True:
        cmd = input("[SOCKETER]:")
        if cmd == "list":
            send_msg(connection,'act_req_list','','s')
        if re.search(r'>',cmd) is not None:
            text, target_user = cmd.split(">")
            send_msg(connection,'act_send_msg',text,target_user)
