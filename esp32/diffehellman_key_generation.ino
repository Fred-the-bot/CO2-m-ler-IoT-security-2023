// Define the prime number and generator for Diffie-Hellman
const long long P = 178543959809;
const long long G = 20428414636;

// Generate a random number between 1 and P-1
long long random_number() {
    return (rand() % (P-1)) + 1;
}

// Calculate the modular exponentiation of base^exp mod modulus
long long modular_pow(long long base, long long exp, long long modulus) {
    long long result = 1;
    base = base % modulus;
    while (exp > 0) {
        if (exp % 2 == 1) {
            result = (result * base) % modulus;
        }
        exp = exp >> 1;
        base = (base * base) % modulus;
    }
    return result;
}

// Generate a private and public Diffie-Hellman key pair
// Returns true on success, false on failure
bool generate_dh_keypair(long long &private_key, long long &public_key) {


    // Generate a random private key
    private_key = random_number();

    // Calculate the public key
    public_key = modular_pow(G, private_key, P);

    return true;
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);

  long long private_key, public_key;

  if (generate_dh_keypair(private_key, public_key)) {
    Serial.println("Private key: " + String(private_key));
    Serial.println("Public key: " + String(public_key));
  }
  else {
    Serial.println("Failed to generate key pair.");
  }
}

void loop() {
  // put your main code here, to run repeatedly:

}
