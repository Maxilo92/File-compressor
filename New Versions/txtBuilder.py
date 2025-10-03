from time import time
from random import randbytes,randint

def readFile(filename: str):
    """returns the Content of the specified file"""
    with open(filename, "r") as f:
            return f.read()

def getBit(last,ver: int,bit):
    if ver == 1:
        if 'magicGlitter' not in globals():
            global magicGlitter
            magicGlitter = int(input(f"How good? (2-{int(2 ** bit) // 100}): ")) -1
            print("0.00%")
        bit = randint(0,magicGlitter)
    else:
        bit = randint(0,2)
    if last == "0":
        if bit > 0:
            return "0" if ver == 1 else "1"
        else:
            return "1" if ver == 1 else "0"
    elif last == "1":
        if bit > 0:
            return "1" if ver == 1 else "0"
        else:
            return "0" if ver == 1 else "1"
        
def bitGen(bit: int, ver: int):
    code = "1"
    for i in range((2 ** bit)-1):
       if True: # true gut, false schlecht
            code += str(getBit(code[len(code)-1],ver,bit))
       else:
            code += str(randint(0,1))
       if (2 ** bit)-1 > 100000 and i % randint(100000,999999) == 0 and i != 0:
            print(f"{i / 2 ** bit * 100:.2f}%")

    return code

def writeFile(filename: str, payload: str):
    with open(filename, "w") as f:
        f.write(payload)

def durchschnitt_folgenlaenge(s: str) -> float:
    if not s:
        return 0.0
    
    folgen = []
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            folgen.append(count)
            count = 1
    folgen.append(count)  # letzte Folge anhängen
    
    return sum(folgen) / len(folgen)

def wechsel_zaehlen(s: str) -> int:
    if not s:
        return 0
    
    wechsel = 0
    letzter = s[0]
    
    for c in s[1:]:
        if c != letzter:   # wenn sich der Wert ändert
            wechsel += 1
            letzter = c
    return wechsel

def getInfo(filename: str):
    code = readFile(filename)
    var0 = 0
    var1 = 0

    for i in code:
        if i == "0":
            var0 += 1
        elif i == "1":
            var1 += 1

    print("sammle Infos...")
    variation = wechsel_zaehlen(code)
    averageLenght = durchschnitt_folgenlaenge(code)

    print("---")
    print(f"0: {var0}")
    print(f"1: {var1}")
    print("")
    print(f"{var0/(var0+var1)*100:.2f}% Nullen")
    print(f"{var1/(var0+var1)*100:.2f}% Einsen")
    if wechsel_zaehlen(code) != 0:
        print("")
        print(f"{wechsel_zaehlen(code)} wechsel bei {var0 + var1} Zeichen (weniger gleich besser)") 
        print(f"wechsel alle {(var0 + var1) / variation:.3f} Zeichen (mehr gleich besser)") 
        print(F"durschnittlich {averageLenght:.3f} Zeichen pro Folge (mehr gleich besser)") 
        if (var0 + var1) / variation != averageLenght:
            print(f"{(var0 + var1) / variation:.3f} != {averageLenght:.3f} why?")
        else:
            print(f"{(var0 + var1) / variation:.3f} == {averageLenght:.3f} why?")

if __name__ == "__main__":

    bits = 24

    print(f"{bits} Bit sind {2 ** bits} Stellen")

    if input("good file? (y/n): ") == "y":
        writeFile("New Versions/original.txt",bitGen(bits,1))
    else:
        print("0.00%")
        writeFile("New Versions/original.txt",bitGen(bits,2))
    print("100.00%")
    getInfo("New Versions/original.txt")