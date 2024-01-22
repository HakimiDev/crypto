import src.ciphers.ciphers as ciphers;

file = open('paragraph.txt', '+r');
file2 = open('result.txt', '+w');

file2.write(ciphers.caesarCipher(file.read()));
print("Done!");