import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Server started. Waiting for the client to connect...")

    try:
        while True:
            client_socket, addr = server_socket.accept()
            print(f"Client address {addr}")

            while True:
                msg = client_socket.recv(1024).decode('utf-8')
                if not msg:
                    break
                print(f"Client: {msg}")
                response = input("Server message here: ")
                client_socket.send(response.encode('utf-8'))
    except KeyboardInterrupt:
        print("Server stopped.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if 'client_socket' in locals():
            client_socket.close()
        server_socket.close()

start_server()