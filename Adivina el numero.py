import random
import os
clear = lambda: os.system("cls")
clear()
print("Juguemos, pensare en un numero y tu lo tendras que adivinar en tres intentos")
print("  ")
bot = random.randint(1,10)
print(bot)
i=0
i= int()
while i<3:
    num = int(input("Adivina el numero del 1 al 10: "))
    if num < bot:
        print("...............................")
        print("Muy chico")
        print("...............................")
        i= i+1
    if num > bot:
        print("...............................")
        print("Muy grande")
        print("...............................")
        i= i+1
    if num == bot:
       print("  ")
       print("Felicidades ganaste!")
       print("  ")
       i= 4
    if i==3:
        print("  ")
        print("Perdiste")
        print("  ")