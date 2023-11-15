a = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypted(text,rotation): #define burtu e un enkode tekstu
  rotation = ""
  for c in text: #cikls kas pamen katru burtu no teksta
    if (a.find(c) == -1): #Ja atrod c tad tiek nonemts viens burts
      rotation += c
    else: # Ja neatrod c tad tiek pievienots viens burts
      rotation += (a[(a.find(c) + o) % len(a)])
  return rotation

def decrypted(text, rotation): #define butru d un dekode tekstu
  rotation = ""
  for c in text: #Cikls kas tiek izmantots lai parveidotu burtus
    if (a.find(c) == -1): #Ja atrod c tad tiek nonemts viens burts
      rotation += c
    else: #Ja neatrod c tad tiek nonemts viens burts
      rotation += (a[(a.find(c) - o) % len(a)])
  return rotation

w = """
1. Encrypt text
2. Decrypt text
3. Bruteforce all rotations
Choose mode: """
mode = int(input(w))

if mode == 1:#Ja ievada 1 tad tiek printets teksts un prasa ievadit rotaciju
  text = input("Enter the text: ")
  rotation = int(input("Enter the rotation: "))
  print("Encrypted: " + encrypted(text, rotation))
  
elif mode == 2:#Ja ievada 2 tad tiek printets teksts un prasa ievadit rotaciju
  text = input("Enter the text: ")
  rotation = int(input("Enter the rotation: "))
  print("Decrypted: " + decrypted(text, rotation))
  
elif mode == 3:#Ja ievada 3 tad tiek printets teksts un prasa ievadit rotaciju
  print("Bruteforcing...")
  print("But I don't know how to do it, sorry ¯\_(ツ)_/¯")
