import math;

def isPrime (n):
    n = float(n);
    if n < 2:
        return False;

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False;

    return True;

def getInverse (n, m):
    for i in range(1, m):
        if (n * i) % m == 1:
            return i;

    return None;

def getInput (msg, validator = None, errorMsg = None):
    while True:
        try:
            data = input(msg);
            if validator == None or validator(data): break;
            elif errorMsg != None: print(errorMsg);
        except Exception as e:
            print(e);
    
    return data;