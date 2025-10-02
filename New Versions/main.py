from compressor import compress
from encoder import encode

def readFile(filename: str):
    """returns the Content of the specified file"""
    with open(filename, "r") as f:
            return f.read()
            
def writeFile(filename: str,payload: str):
    with open(filename, "w") as f:
        f.write(payload)

compressed = compress(readFile("original.txt"))
print(compressed)

print("-")

clear = encode(compressed)
print(clear)