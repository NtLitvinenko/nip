# DNS by NTLDev (dns.service)
# DNS Server written in New Internet Protocol for New Internet Protocol

import socket
import threading
import pandas as pd
fp = open('dns.db', 'r')
lines = fp.readlines()
fp.close()
lines = [line.replace("\n", "") for line in lines]
db = [line.split(",") for line in lines]
df = pd.DataFrame(db, columns=["param", "value"])

class Server:
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('127.0.0.1', 42))
        self.server_socket.listen(24)

    def handle_client(self, client_socket, address):
        print(f"Соединение с {address} установлено")

        while True:
            try:
                query = client_socket.recv(1024)
                if not query:
                    break
                print(f"Запрос от клиента: {query.decode()}")

                if query:
                    query = query.decode()
                    query_data = query.split(" ")
                    if query_data[0] == "GET":
                        print(query_data)
                        print(query_data[1].replace("\n","").replace("\r",""))
                        result = df.loc[df["param"] == query_data[1].replace("\n","").replace("\r","")].values.tolist()
                        if result:
                            print(result)
                            answer = f"ANSWER dns.service {result[0][0]} {result[0][1]}\n"
                            client_socket.send(answer.encode())
                        elif result == []:
                            client_socket.send(b"ANSWER dns.service UNKNWN UNKNWN\n")
                        else:
                            client_socket.send(b"ANSWER NULL NULL NULL")
                    else: client_socket.send(b"EXCEPTION UNKNWN\n")
            except Exception as e:
                print(f"Ошибка: {e}")
                break

        client_socket.close()

    def start(self):
        print("DNS Server working. Waiting for connection(s)...")
        print("Port: 42")  # Standart NIP DNS port is 46

        while True:
            client_socket, address = self.server_socket.accept()
            client_thread = threading.Thread(target=self.handle_client, args=(client_socket, address))
            client_thread.start()


if __name__ == "__main__":
    server = Server()
    server.start()
