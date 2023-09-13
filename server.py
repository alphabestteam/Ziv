import socket

# Establishing communication between the server and client
server_side_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_side_address = ("localhost", 12345)
server_side_socket.bind(server_side_address)
server_side_socket.listen(1)
client_side_socket, client_address = server_side_socket.accept()

# Receives message and turns to upper case
received_message = (client_side_socket.recv(1024).decode("utf-8")).upper()

client_side_socket.send(received_message.encode("utf-8"))

client_side_socket.close()
server_side_socket.close()
