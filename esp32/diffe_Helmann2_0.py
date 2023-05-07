import socket
import urandom

import network
def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('<SSID>', '<pass>')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())


do_connect()




s = socket.socket()




# The modulus and generator for the Diffie-Hellman key exchange
p = 29807
g = 3

# Generate a random secret key for the client
client_secret_key = urandom.getrandbits(16)

# Calculate the public key to send to the server
client_public_key = pow(g, client_secret_key, p)

# Send the public key to the server
print("Client public key:", client_public_key)
client_public_key = str(client_public_key)

s.connect(('192.168.1.206',8090))
s.send(client_public_key)



# Wait for the server's public key

server_public_key = s.recv(32)
print(server_public_key)
server_public_key = int(server_public_key)


# Calculate the shared secret key
shared_secret_key = pow(server_public_key, client_secret_key, p)


print("Shared secret key:", shared_secret_key)

s.close()
