from src.utilities.tools import isPrime, getInverse;

def affineCipher (plaintext, a, b, decrypt = False):
    ALPHABET = "abcdefghijklmnopqrstuvwxyz";
    ALPHABET_LEN = len(ALPHABET);

    aInverse = getInverse(a, ALPHABET_LEN);

    if not isPrime(a) or aInverse == None:
       raise ValueError("'a' Argement must be a prime number.");

    result = '';
    for c in plaintext:
        to = c.lower();
        if to in ALPHABET:
            if not decrypt:
                to = ALPHABET[ ( ALPHABET.index(to) * a + b) % ALPHABET_LEN ];
            else:
                to = ALPHABET[ ( aInverse * (ALPHABET.index(to) - b ) ) % ALPHABET_LEN ];

        result += to.upper() if c.isupper() else to;
    
    return result;
