
def loadBits():
    with open("original.txt", "r") as f:
            return f.read()
    
def saveBits(payload):
    with open("compressed.txt", "w") as f:
        f.write(payload)
        print("Fertig!")
    
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
            if counter <= 254:
                counter += 1
            else:
                smallList.append([lastBit,counter])
                counter = 1
                lastBit = bits[i]
        elif lastBit != bits[i]:
            smallList.append([lastBit,counter])
            counter = 1
            lastBit = bits[i]

print(smallList)

smallCode = ""

for i in smallList:
    smallCode += f"{i[0]}{format(i[1],'08b')}"
    print(f"{i[0]}{format(i[1],'08b')}")

smallCode = smallCode.strip()    

print("-")
print(f"original:   {bits}")
print("-")
print(f"compressed: {smallCode}")
print("-")

saveBits(smallCode)
