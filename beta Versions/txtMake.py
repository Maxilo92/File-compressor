from random import randint
from time import time

def calibrate(bit):
    iter = 10000
    start = time()
    test = ""
    for i in range(iter):
       test += str(randint(0,1))
    
    print(f"{2 ** bit} Bit")
    print(f"{(time() - start) / iter} sek/bit")
    print(f"{(time() - start) * 2 ** bit / iter} Sekunden")
    print(f"{((time() - start) * 2 ** bit) / iter / 60} Minuten")
    print(f"{((time() - start) * 2 ** bit) / iter / 60 / 60} Stunden")

def getBit(last):
    bit = randint(0,2)
    if last == "0":
        if bit > 0:
            return "0"
        else:
            return "1"
    elif last == "1":
        if bit > 0:
            return "1"
        else:
            return "0"

def binGen(bit: int):
    print(f"{bit} Bit sind {2 ** bit} Stellen")
    code = "1"

    for i in range((2 ** bit)-1):
       if True: # true gut, false schlecht
        code += str(getBit(code[len(code)-1]))
       else:
        code += str(randint(0,1))
       if i % randint(100000,999999)  == 0:
           print(i)

    return code
       
def writeFile(payload: str):
    with open("original.txt", "w") as f:
        f.write(payload)

    # open and read the file after the overwriting:
    with open("original.txt", "r") as f:
        content = f.read()
        if content != payload:
            raise NotImplementedError("txt wurde nicht erfolgreich beladen")
        else:
            print("Fertig!")

bit = 8

calibrate(bit)

if input("y|n: ") == "y":
    writeFile(binGen(bit))
