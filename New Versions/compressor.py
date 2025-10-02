import os

def readFile(filename: str):
    """returns the Content of the specified file"""
    with open(filename, "r") as f:
            return f.read()
            
def writeFile(filename: str,payload: str):
    with open(filename, "w") as f:
        f.write(payload)
    
def compress(bits):
    lastBit = ""
    counter = 0
    compressed = ""
    # print(bits)

    for bit in bits:
        if lastBit != "":
            counter += 1
            # print(f"{lastBit}|{counter}")
            if counter >= 9:
                compressed += f"{lastBit}{counter}"
                counter = 0
            else:
                match lastBit,bit:
                    case "0","0":
                        #just count
                        ...
                    case "0","1":
                        #print(f"{lastBit}{counter}")
                        compressed += f"{lastBit}{counter}"
                        counter = 0
                    case "1","0":
                        #print(f"{lastBit}{counter}")
                        compressed += f"{lastBit}{counter}"
                        counter = 0
                    case "1","1":
                        #just count
                        ...
        lastBit = bit
    counter += 1
    # print(f"{lastBit}|{counter}")
    compressed += f"{lastBit}{counter}"

    return compressed

if __name__ == "__main__": 
    bits = readFile("New Versions/original.txt")
    compressed = compress(bits)

    # print(bits)
    # print(compressed)
    print(f"Die Komprimierte Datei ist {(1 - len(compressed) / len(bits)) * 100:.3f}% kleiner als vorher")

    writeFile("New Versions/compressed.txt",compressed)