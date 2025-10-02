import os

def readFile(filename: str):
    """returns the Content of the specified file"""
    with open(filename, "r") as f:
            print("lade Datei...")
            return f.read()
            
def writeFile(filename: str,payload: str):
    with open(filename, "w") as f:
        print("speichern...")
        f.write(payload)
        print("Gespeichert!")
    
code = readFile("original.txt")
print("geladen!")

writeFile("compressed.txt","abc")