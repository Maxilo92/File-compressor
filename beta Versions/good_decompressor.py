def loadBits():
    with open("compressed.txt", "r") as f:
            return f.read()
    
def loadOriginal():
    with open("original.txt", "r") as f:
        return f.read()
    
smallCode = loadBits()

print(f"{int(len(smallCode) / 9)} Chunks gefunden")

chunks = []

for i in range(int(len(smallCode) / 2)):
    print(smallCode[i*2:(i+1)*2])
    chunks.append(smallCode[i*2:(i+1)*2])

print(chunks)

bigCode = ""

for chunk in chunks:
    bit = chunk[:1]
    count = chunk[1:]
    print(bit,int(count))
    for i in range(int(count)):
        bigCode += bit

print(bigCode)

print(loadOriginal() == bigCode)