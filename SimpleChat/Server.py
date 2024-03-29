from socket import *

s = socket(AF_INET, SOCK_STREAM)
print("Socket successfully created")

host = '127.0.0.1'
port = 40675

s.bind((host, port))
print("Socket binded to", port)

s.listen(5)
print("Socket is listening")

c, addr = s.accept()
print('Got connection from', addr)

while True:
    x = c.recv(2048)
    if not x:
        break
    print("Client:", x.decode())
    server_message = input("Server: ").encode()

    # Calculate the length of the message
    message_length = len(server_message)

    # Send the message in chunks if its size is larger than the buffer size
    if message_length > 2048:
        # Calculate the number of chunks needed
        num_chunks = message_length // 2048 + 1

        # Send each chunk iteratively
        for i in range(num_chunks):
            start_index = i * 2048
            end_index = min((i + 1) * 2048, message_length)
            c.send(server_message[start_index:end_index])

    else:
        # If message fits within buffer size, send it as is
        c.send(server_message)

    # To leave while loop, write "end"
    if server_message.decode() == "end":
        break

c.close()
s.close()
