from math import *
import math


print("Ruudu karakteristikud")
a=float(input("Sisesta ruudu külje pikkus => ")) #convert tp float
S=a**2
print("Ruudu pindala", S)
P=4*a
print("Ruudu ümbermõõt", P)
di=a*math.sqrt(2)
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud")
b=float(input("Sisesta ristküliku 1. külje pikkus => ")) #convert tp float
c=float(input("Sisesta ristküliku 2. külje pikkus => ")) #convert tp float
S=b*c
print("Ristküliku pindala", S)
P=2*(b+c) #umnozhenie
print("Ristküliku ümbermõõt", P)
di=math.sqrt(b*2+c*2)
print("Ristküliku diagonaal", round(di,2)) 
print()
print("Ringi karakteristikud")
r=float(input("Sisesta ringi raadiusi pikkus => ")) #convert tp float
d=2*r
print(f"Ringi läbimõõt {d}" )
S=pi*r**2
print("Ringi pindala", round(S,2)) #okruglenie
C=2*pi*r
print("Ringjoone pikkus", round(C,2)) #okruglenie
