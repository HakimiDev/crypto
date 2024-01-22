import src.ciphers.ciphers as ciphers;
from src.utilities.tools import *;

plaintext = getInput("Enter the plaintext: ");
algorithm = int(getInput("Choose the algorithm:\n1- Caesar\n2- Affine\nChoose: ", lambda x : int(x) in [1, 2]));

def algorithm_switch (case):
    ciphertext = '';
    if case == 1:
        key = int(getInput("Enter the key: ", lambda x : int(x)));
        funcType = int(getInput("Choose the type:\n1- Encrypt\n2- Decrypt\nChoose: ", lambda x : int(x) in [1, 2]));
        ciphertext = ciphers.caesarCipher(plaintext, key if funcType == 1 else -key);
    elif case == 2:
        key1 = int(getInput("Enter the key1 (must be a prime number): ", isPrime));
        key2 = int(getInput("Enter the key2: ", lambda x : int(x)));
        funcType = int(getInput("Choose the type:\n1- Encrypt\n2- Decrypt\nChoose: ", lambda x : int(x) in [1, 2]));
        ciphertext = ciphers.affineCipher(plaintext, key1, key2, funcType == 2);
    
    print("Ciphertext is:", ciphertext);


algorithm_switch(algorithm);
