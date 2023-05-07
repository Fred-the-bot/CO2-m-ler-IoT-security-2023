import socket
import random
import time

s = socket.socket()
s.bind(('0.0.0.0', 8090))
s.listen(0)

print("waiting for client")
client, addr = s.accept()
print(client)

content = client.recv(32)
# The modulus and generator for the Diffie-Hellman key exchange
p = 29807
g = 3

# Generate a random secret key for the server
server_secret_key = random.getrandbits(16)

# Calculate the public key to send to the client
server_public_key = pow(g, server_secret_key, p)

# Wait for the client's public key
print(server_public_key)
client_public_key = int(content)
# client_public_key = int(input("Enter the client's public key: "))

# Calculate the shared secret key
shared_secret_key = pow(client_public_key, server_secret_key, p)

print("Shared secret key:", shared_secret_key)
server_public_key = str(server_public_key)
server_public_key = server_public_key.encode('utf-8')

client.sendall(server_public_key)

print("Closing connection")
client.close()
