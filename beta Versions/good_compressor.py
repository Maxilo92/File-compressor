import os


def loadBits():
    with open("original.txt", "r") as f:
            return f.read()
    
def saveBits(payload):
    with open("compressed.txt", "w") as f:
        f.write(payload)
        # print("Fertig!")

def checkSize():
    groesse_org = os.path.getsize("original.txt")
    groesse_com = os.path.getsize("compressed.txt")

    if groesse_org == 0:
        print("Originaldatei ist leer.")
        return
    if groesse_com == 0:
        print("Komprimierte Datei ist leer oder wurde nicht erzeugt.")
        return

    reduction = (1 - groesse_com / groesse_org) * 100
    if reduction >= 0:
        print(f"die komprimierte Datei ist um {reduction:.2f}% kleiner als das Original")
    else:
        print(f"die komprimierte Datei ist um {abs(reduction):.2f}% größer als das Original")
    
bits = loadBits()

smallList = []
lastBit = ""
counter = 1

for i in range(len(bits)):
    if lastBit == "":
        lastBit = bits[i]
    elif i == len(bits) - 1:
        counter += 1
        smallList.append([lastBit,counter])
    else:
        if lastBit == bits[i]:
            if counter <= 7: # 254
                counter += 1
            else:
                smallList.append([lastBit,counter])
                counter = 1
                lastBit = bits[i]
        elif lastBit != bits[i]:
            smallList.append([lastBit,counter])
            counter = 1
            lastBit = bits[i]

# print(smallList)

smallCode = ""

for i in smallList:
    smallCode += f"{i[0]}{i[1]}"
    print(f"{i[0]}{i[1]}")

smallCode = smallCode.strip()    

print("-")
print(f"original:   {bits}")
print("-")
print(f"compressed: {smallCode}")
print("-")

saveBits(smallCode)

checkSize()