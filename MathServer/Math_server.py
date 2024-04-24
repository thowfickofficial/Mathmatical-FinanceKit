import socket

def handle_client(client_socket):
    try:
        while True:
            # Receive the mathematical expression from the client
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break

            # Evaluate the mathematical expression
            try:
                result = str(eval(data))
            except Exception as e:
                result = "Error: " + str(e)

            # Send the result back to the client
            client_socket.send(result.encode('utf-8'))
    except:
        pass

    # Close the client socket
    client_socket.close()

def math_server(host, port):
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(5)
    print(f"Math server is listening on {host}:{port}")

    try:
        while True:
            # Accept a client connection
            client_socket, addr = server_socket.accept()
            print(f"Accepted connection from {addr}")

            # Handle the client in a separate thread
            client_handler = threading.Thread(target=handle_client, args=(client_socket,))
            client_handler.start()
    except KeyboardInterrupt:
        pass
    finally:
        # Close the server socket
        server_socket.close()

if __name__ == '__main__':
    import threading

    # Set the host and port
    host = '0.0.0.0'  # Listen on all available interfaces
    port = 12345

    # Start the math server
    math_server(host, port)
