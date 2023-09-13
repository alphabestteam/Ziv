import socket

# Establishing communication between the server and client
client_side_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_side_address = ("localhost", 12345)
client_side_socket.connect(server_side_address)

# Sending an receiving the message on the client side
sending_message = input("Enter the message: ")
client_side_socket.send(sending_message.encode("utf-8"))
received_response = client_side_socket.recv(1024).decode("utf-8")
print(received_response)

client_side_socket.close()
