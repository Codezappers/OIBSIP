import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    try:
        while True:
            client_msg = input("Client message here: ")
            if not client_msg:
                break
            client_socket.send(client_msg.encode('utf-8'))
            server_msg = client_socket.recv(1024)
            if server_msg:
                print(f"Server: {server_msg.decode('utf-8')}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()