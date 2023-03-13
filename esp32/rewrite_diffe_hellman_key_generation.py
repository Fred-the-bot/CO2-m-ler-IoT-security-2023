import urandom

# Define the prime number and generator for Diffie-Hellman
P = 29807
G = 3

# Generate a random number between 1 and P-1
def random_number():
    return urandom.getrandbits(16) % (P-1) + 1

# Calculate the modular exponentiation of base^exp mod modulus
def modular_pow(base, exp, modulus):
    result = 1
    base = base % modulus
    while exp > 0:
        if exp & 1 == 1:
            result = (result * base) % modulus
        exp = exp >> 1
        base = (base * base) % modulus
    return result

# Generate a private and public Diffie-Hellman key pair
# Returns true on success, false on failure
def generate_dh_keypair():

    # Generate a random private key
    private_key = random_number()

    # Calculate the public key
    public_key = modular_pow(G, private_key, P)

    return private_key, public_key

private_key, public_key = generate_dh_keypair()

print("Private key:", private_key)
print("Public key:", public_key)
