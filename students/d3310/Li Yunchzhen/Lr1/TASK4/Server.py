#server.py
import json
import socket
from threading import Thread


ADDRESS = ('localhost', 12321)
CONNECTION = None
SERVERNAME = "SOCKETER-SERVER"
CONNECTION_POOL = {}
init_msg = """
    ______   ___   ____ _  _______ _____ _____ ____      __
   / / ___| / _ \ / ___| |/ / ____|_   _| ____|  _ \    / /
  / /\___ \| | | | |   | ' /|  _|   | | |  _| | |_) |  / / 
 / /  ___) | |_| | |___| . \| |___  | | | |___|  _ <  / /  
/_/  |____/ \___/ \____|_|\_\_____| |_| |_____|_| \_\/_/   
                                                           

"""


def init():
    global CONNECTION
    CONNECTION = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    CONNECTION.bind(ADDRESS)
    CONNECTION.listen(5)
    print(init_msg)

def send_msg(socket1, username, cmd, data, target):
    jdata = {}
    jdata['cmd'] = cmd
    jdata['target'] = target
    jdata['from'] = username
    jdata['data'] = data
    jstr = json.dumps(jdata)
    socket1.sendall(jstr.encode('utf-8'))


def connection_control():
    while True:
        client, client_address = CONNECTION.accept()
        newThread = Thread(target=msg_control,args=(client,))
        newThread.setDaemon(True)
        newThread.start()

def msg_control(client):
    client.sendall((init_msg + "\n Connect to chat-server successfully!").encode('utf-8'))
    while True:
        try:
            data = client.recv(1024).decode('utf-8')
            jdata = json.loads(data)
            user = jdata['from']
            target = jdata['target']
            if jdata['cmd'] == "act_connect":
                CONNECTION_POOL[user] = client
            if jdata['cmd'] == "act_send_msg":
                if jdata['target'] not in CONNECTION_POOL:
                    send_msg(client,SERVERNAME,"ERROR",f"ERROR:User{jdata['target']} does not online!",user)
                else:
                    target_connection = CONNECTION_POOL[target]
                    send_msg(target_connection,user,"act_send_msg",jdata['data'],target)
            elif jdata['cmd'] == "act_req_list":
                print(user + " req_list")
                userlist = str(CONNECTION_POOL.keys())
                send_msg(client,SERVERNAME,"return_list",userlist,user)
        except Exception:
            remove_client(user)
            break

def remove_client(user):
    connection = CONNECTION_POOL[user]
    if None != connection:
        connection.close()
        CONNECTION_POOL.pop(user)
        print(f"{user} Offline.")



if __name__ == "__main__":
    init()
    t1 = Thread(target=connection_control)
    t1.setDaemon(True)
    t1.start()
    while True:
        cmd = input("[SOCKETER-SERVER]:")
        if cmd == "list":
            print(CONNECTION_POOL.keys())
        if cmd == "exit":
            break
        if cmd == "list1":
            print(CONNECTION_POOL)

