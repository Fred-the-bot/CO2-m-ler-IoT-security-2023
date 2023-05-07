
import urandom


# The modulus and generator for the Diffie-Hellman key exchange
p = 29807
g = 3

# Generate a random secret key for the client
client_secret_key = urandom.getrandbits(16)

# Calculate the public key to send to the server
client_public_key = pow(g, client_secret_key, p)

# Send the public key to the server
print("Client public key:", client_public_key)

# Wait for the server's public key
server_public_key = int(input("Enter the server's public key: "))

# Calculate the shared secret key
shared_secret_key = pow(server_public_key, client_secret_key, p)

11
print("Shared secret key:", shared_secret_key)


