def caesarCipher (plaintext, key = 3):
    ALPHABET = "abcdefghijklmnopqrstuvwxyz";
    ALPHABET_LEN = len(ALPHABET);

    if key % ALPHABET_LEN == 0: return plaintext;

    result = '';
    for c in plaintext:
        to = c.lower();
        if to in ALPHABET:
            to = ALPHABET[ (ALPHABET.index(to) + key) % ALPHABET_LEN ];

        result += to.upper() if c.isupper() else to;
    
    return result;
