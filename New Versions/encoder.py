def readFile(filename: str):
    """returns the Content of the specified file"""
    with open(filename, "r") as f:
        return f.read()
    
def encode(compressed):
    clear = ""
    for i in range(len(compressed) // 2):
        if i < (len(compressed) // 2):
            count = int(compressed[2*i+1])
            for _ in range(count):
                clear += compressed[2*i]
    return clear

if __name__ == "__main__":   
    compressed = readFile("compressed.txt")
    clear = encode(compressed)

    # print(compressed)
    # print(clear)
    # print(clear == readFile("original.txt"))
    print(f"Die Datei wurde{"" if clear == readFile("original.txt") else "nicht"} Erfolgreich encodet")