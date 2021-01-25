import random
import time 

print(time.strftime("%H:%M"))
numere = input("How many passwords: ")
numere = int(numere)
lungime = input("What lenght: ")
lungime = int(lungime)
char = 'zxcvbnm,./asdfghjkl;qwertyuiop[]\1234567890-=QWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+{}:"<>?'
password = ""
f = open("passwords.txt","a")
for y in range(numere):
    for x in range(lungime):
        password+=random.choice(char)
    print(password)
    f.write(password)
    f.write("\n")
    password = ""
f.close()
input("Press any key to continue...")
