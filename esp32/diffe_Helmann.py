import random

# Define the prime number and generator for Diffie-Hellman
P = 65027
G = 12098

# Generate a random number between 1 and p-1
def random_number():
    return (random.randint(1,P) % (P-1)+1)


# Calculate the modular exponentiation of base^exp mod modulus
def modular_pow(base, exp, modulus):
    result= 1
    base= base% modulus
    while (exp > 0):
        if (exp % 2 ==1):
            result = (result * base) % modulus
            
        exp = exp >> 1
        base = (base * base) %modulus
    
    return result

# Generate a private and public Diffie-Hellman key pair
# Returns true on success, false on failure
class test:
    private_key =0 
    public_key =0
    def generate_dh_keypair():
        print("DEBUG")
        #generate a random private key
        private_key = random_number()

        #calculate the public key
        public_key = modular_pow(G, private_key, P)

        print(public_key)
        return True , private_key, public_key




if (test.generate_dh_keypair()):
    print("private key: ", str(test.private_key))
    print("public key: ", str(test.public_key))
    
else:
    print("failed to compute")





