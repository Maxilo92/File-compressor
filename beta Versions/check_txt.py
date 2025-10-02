from random import randint

def loadBits():
    with open("original.txt", "r") as f:
            return f.read()
    
def varianz_von_muster(s: str, start=1) -> float:
    n = len(s)
    if n == 0:
        return 0.0
    
    sum_x = 0       # Summe der Abweichungen
    sum_x2 = 0      # Summe der Quadrate der Abweichungen
    
    for i, c in enumerate(s):
        wert = int(c)
        erwartet = (i % 2) ^ (1 - start)  # erwartetes Muster (alternierend)
        abw = wert - erwartet
        abw2 = abw * abw                  # 0 oder 1
        sum_x += abw
        sum_x2 += abw2
    
    mean_x = sum_x / n
    return (sum_x2 / n) - (mean_x ** 2)

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

code = loadBits()

var0 = 0
var1 = 0

for i in code:
    if i == "0":
        var0 += 1
    elif i == "1":
        var1 += 1

print(f"0: {var0}")
print(f"1: {var1}")
print(f"{var0/(var0+var1)*100:.2f}% Nullen")
print(f"{var1/(var0+var1)*100:.2f}% Einsen")

print(f"Varianz: {varianz_von_muster(code, start=int(code[0]))*100:.4f}% perfekt")

print(f"{wechsel_zaehlen(code)} wechsel (weniger gleich besser)") 

print(F"durschnittlich {durchschnitt_folgenlaenge(code):.3f} Zeichen pro Folge (mehr gleich besser)") 