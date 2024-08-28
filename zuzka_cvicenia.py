#chapter 1
""" celociselne delenie
print(22//7)
"""
""" zvysok po deleni
print(23.0 % 3.0)"""
""" umocnovanie 
print(3 ** 2)"""
""" premenne
ab = 13
ab = ab + 7
print(ab)"""    
""" input 
meno = input("zadaj svoje meno")
print(f'volas sa {}.)
"""
""" nasobenie int a float 
print(52 * 0.23)"""

"""NAPIS PROGRAM KTORY PREVEDIE EURA A CENTY NA KORUNY

retazec = input('zadaj eura: ')
suma = float(retazec)             
koruny = suma * 26
print(suma, 'euro je', koruny, 'korun') # print(f'{suma}, euro je, {koruny}, korun.)
"""

""" funkcia abs()
print(abs(-23.44))
""" 
""" funkcia round()  
print(round(1))
print(round(3.14))
print(round(3.14,1)) canvas.create_oval(x,y,x,y, fill = )
print(round(2534, -2))
"""
""" dvojica znakov (\n)
print("bob\nthe\nbuilder") """
""" ako funguje f'{a} je mensie ako {b}'
meno, x, y = 'A', 180, 225
r = f'bod {meno} je na suradniciach ({x},{y})'
print(r)
"""
""" paralelne priradenie
a = 5
b = 10
a,b = b, a

print(b)
print(a)
"""
"""NAPIS PROGRAM KTORY VYPOCITA TRETIE ODMOCNINU Z CISLA ZADANEHO PRIKAZOM INPUT A ZAOKRUHLI HO NA 2 DESATINE MIESTA

cislo = float(input("zadaj cislo"))
tretia_odmocnina = cislo ** (1/3)
zaokruhlenie = round(tretia_odmocnina, 2)
print(zaokruhlenie)

"""

"""V PREMENNYCH meno A preizvisko SU PRIRADENE NEJAKE DVA ZNAKOVE RETAZCE. DO PREMENEJ desat PRIRAD RETAZEC KTORY OBSAHUJE DESATKRAT MENO A PREIZVISKO ODDELENE CIARKOU 

meno = "Zuzana"
priezvisko = "Kolencikova"
desat = (meno + " " + priezvisko + ", ") * 9 + meno + " " + priezvisko
print(desat) 
"""

# chapter 2 

""" for-cyklus 
for i in range(10):
    print("python")    
"""
""" indentacie vo for cykle
for i in range(10):
    print("a")
    print("b")
print("koniec"):
"""
""" co znamena premenna i vo forcikle 
for i in range(10):
    print(i)
print("============")

for i in range(1,10 + 1):
    print(i)
print("============")
for i in range(1,11,2):
    print(i)
print("============")
"""

""" NAPIS PROGRAM ,PUZI FOR CYKLUS, KTORYM OINDEXUJES PORADIE RIADKOV POCET DOSTANES POUZITIM FUNKCIE INPUT(), zacinas nultym riadkom 

pocet_riadkov = int(input("zadaj pocet riadkov: "))
for i in range(pocet_riadkov):
    print(i, "riadok")
"""

""" vypocty v tele for-cyklu 

n = int(input("zadaj n: "))
counter = 0

for i in range(n):
    counter += 1
print("pocet prechodov cyklu =", counter)
"""
""" pre for-cyklus vieme vymenovat hodnoty int ale aj str
for i in 1,2,3,4,5:
    print(i)
print(" ")
for i in "python":
    print(i)
"""
""" zakoncovanie funkcie print()
for i in range(100,200):
    print(i, end=" ") """ 
"""
import math

for i in range(0, 361, 10):
    uhol_v_radianoch = math.radians(i)
    sin_uhla = math.sin(uhol_v_radianoch)
    stlpec = int(sin_uhla * 35 + 40)
    print(" " * stlpec + "#")

"""
""" modul random

import random

for i in range(100):
    n = random.randrange(1,7)
    print(n,end=" ")
print("\n")

for i in range(100):
    n =  random.choice("abcdefghijklmnopqrstuvwxyz")
    print(n,end= " ")
"""
""" vnorene for-cykly 
for i in range(10):
    for j in range(10):
        print("*", end=" ")
    print("")
"""

""" NAPIS PROGRAM, KTORY PRECITA CELE CISLO (MAX 8 CIFERNE) A POTOM V CYKLE (8 KRAT) POSTUPNE CISLO SKRACUJE O POSLEDNU CIFRU, ZAROVEN VYPISUJE SKRATENE CISLO AJ POSLEDNU CIFRU, O KTORU BOLO SKRATENE.

n = (input("zadaj cislo (8 cifier): "))
m = n

for i in n:
    n = int(n)
    m = int(n)
    x = n % 10 
    n = (n-x) / 10
    print(int(n)," ",x)
"""

# chapter 3

""" modul tkinter a otvaranie kresliacej plochy

import tkinter
canvas = tkinter.Canvas(height = 500, width = 500, bg = "white",)
canvas.pack()

canvas.create_text(250,250,text="bob",fill= "black")

tkinter.mainloop()
"""

""" pisanie na graficku plochu
import tkinter

canvas = tkinter.Canvas(height=500,width=500,bg = "white")
canvas.pack()

canvas.create_text(250,250,text = "python",font = "calibri",fill = "blue")

tkinter.mainloop()
"""
""" kreslenie na graficku plochu stvorec/ obdlznik
import tkinter

canvas = tkinter.Canvas(height=500,width=500,bg = "white")
canvas.pack()

canvas.create_rectangle(50,50,150,150,width= 8,outline= "green", fill = "light green")

tkinter.mainloop()
"""
""" kreslenie na graficku plochu kruh/ oval
import tkinter

canvas = tkinter.Canvas(height=500,width=500,bg = "white")
canvas.pack()

canvas.create_oval(50,50,150,150,width= 8,outline= "green", fill = "light green")

tkinter.mainloop()
"""
""" kreslenie na graficku plochu ciara
import tkinter

canvas = tkinter.Canvas(height=500,width=500,bg = "white")
canvas.pack()

canvas.create_line(50,50,450,450,width= 8, fill = "black", arrow= "both")

tkinter.mainloop()
"""
""" hexadecimal colours
import tkinter

canvas = tkinter.Canvas(height=500,width=500,bg = "white")
canvas.pack()

r,g,b = 205, 92, 9
colour = f'#{r:02x}{g:02x}{b:02x}'

canvas.create_rectangle(100,100,400,400,outline= "black",fill = colour)

tkinter.mainloop()
"""
""" random colours 

import tkinter
import random 

canvas = tkinter.Canvas(height=500,width=500,bg = "white")
canvas.pack()

r = random.randrange(256)
g = random.randrange(256)
b = random.randrange(256)
colour = f'#{r:02x}{g:02x}{b:02x}'

canvas.create_rectangle(100,100,400,400,outline= "black",fill = colour)

tkinter.mainloop()

"""

""" POUZI VNORENY FOR CYKLUS NA OKACHLICKOVANIE GRAFICKEJ PLOCHY STVORCAMI S NAHODNYMI FARBAMI 10 * 10 

import tkinter
import random

canvas = tkinter.Canvas(height = 500, width = 500, bg = "white")
canvas.pack()

x = 70
y = 0

for i in range(10):
    y += 45
    x = 70
    for j in range(10):
        r = random.randrange(256)
        g = random.randrange(256)
        b = random.randrange(256)
        colour = f'#{r:02x}{g:02x}{b:02x}'
       
        canvas.create_rectangle(x - 20,y - 20,x + 20,y + 20,outline = "black", fill = colour)
        x += 45

tkinter.mainloop()

"""

# chapter 4

""" napis program, ktory zafarbi stvorceky na modro v pomere 1:50 
import tkinter
import random

canvas = tkinter.Canvas(bg='white', width=300, height=300)
canvas.pack()

for i in range(1000):
    x = random.randrange(300)
    y = random.randrange(300)
    if random.randrange(50):             
        farba = 'red'
    else:
        farba = 'blue'
    canvas.create_rectangle(x-5, y-5, x+5, y+5, fill=farba, outline='')


tkinter.mainloop()

"""
""" zafarbi lavu polku plochy na cerveno a pravu na modro
import tkinter
import random

canvas = tkinter.Canvas(height = 400, width = 400, bg = "white")
canvas.pack()

for i in range(5000):

    x = random.randrange(400)
    y = random.randrange(400)

    if x < 200:
        colour = "red"
    else:
        colour = "blue"
    canvas.create_oval(x - 5, y - 5,x + 5 ,y + 5, outline = colour, fill = colour)

tkinter.mainloop()
"""

""" ZMEN PODMIENKY TAK ABY SA KRIZ ZAFARBIL NA + A POTOM X 

import tkinter

canvas = tkinter.Canvas(height= 400,width=400,bg = "white")
canvas.pack()

n = 9
for i in range(n):
    for j in range(n):
        x = j * 20 + 100
        y = i * 20 + 10 + 50
        if i == j or i + j == n-1:                    #if i == 4 or j == 4:
            farba = 'red'
        else:
            farba = 'white'
        canvas.create_oval(x-8, y-8, x+8, y+8, fill=farba)

tkinter.mainloop()
"""
""" ZISTI KTORYMI VSETKIMI CISLAMI JE CISLO DELITELNE  
number = 23

"""

import tkinter

canvas = tkinter.Canvas(height = 500, width = 500, bg = "white")
canvas.pack()

n = 5
x = 250
y = 90

def petri_dish():
    x = 250
    y = 400
    canvas.create_oval(x-120,y-30,x+120,y+30, outline= "black",width= 2)
    y -= 40
    canvas.create_oval(x-120,y-30,x+120,y+30, outline= "black",width= 2)
    canvas.create_line(x-120,y,x-120,y+40,width=2,fill="black")
    canvas.create_line(x+120,y,x+120,y+40,fill="black", width= 2)

petri_dish()

counter = 0

for i in range(1,n+1):
    while y < 400:
        if counter != n:
            canvas.delete("drop")
            canvas.create_oval(x-10,y-10,x+10,y+10,outline="blue",fill="blue",tag="drop")
            canvas.update()
            y += 5
            if y == 400:
                counter += 1
                canvas.delete("drop")
                x_increment= (240/n)/2
                y_increment= (60/n)/2
                canvas.create_oval(x - x_increment * counter, y - y_increment * counter, x + x_increment * counter, y + y_increment * counter, outline= "blue",fill="blue")
                petri_dish()
                canvas.delete("txt")
                canvas.create_text(375,175,text=f'number of\n drops: {counter}',fill="black",tag="txt")
                canvas.update()
                y = 90
        else:
            break
                





canvas.mainloop()


# chapter 5

""" syntax pisania vlastnej funkcie

def meno_funkcie(x)
    print(str(x))


""" 

""" NAPIS FUNKCIU, KTORA TI PO VOLANI VIGENERUJE NAHODNU FARBU TUTO FUNKCIU POUZI NA ZAFARBENIE PIRAMIDI O VYSKE 3 KVADROV S ROMSERMI 30 A 50

import random
import tkinter

def random_colour():
    r = random.randrange(256)
    g = random.randrange(256)
    b = random.randrange(256)

    return f'#{r:02x}{g:02x}{b:02x}'

canvas = tkinter.Canvas(height= 500, width= 500, bg = "white")
canvas.pack()

x = 200
y = 280
f = -1
for i in reversed(range(1,4)):
    y -= 30
    x = 200
    f += 1
    x -= 25 * f
    for j in range(i):
        canvas.create_rectangle(x-25,y-15,x+25,y+15,outline="black",fill=random_colour())
        x -= 50
tkinter.mainloop()


print(random_colour())
"""
# chapter 6

""" napis funkciu ktora ti po zadani pismena a slova zisti ci slovo obsahuje pismeno

def zisti(znak, retazec):
    for z in retazec:
        if z == znak:
            return True
    return False

        
print(zisti("y", "Mydlo"))
print(zisti("f", "jablko"))
"""
""" indexovanie 


x, y = 'Bratislava', 'Praha'

print(x[5:8] + 3 * x[3] + y[2:])
print(x[10::-1])

"""
