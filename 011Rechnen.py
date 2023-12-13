
#1
print("Substraktion zweier Zahlen")
wert1=int(input("Zahl1: "))
wert2=int(input("Zahl2: "))
ergebnis=wert1-wert2
print("Das Ergebnis der Substraktion", wert1, "-", wert2, "ist", ergebnis)
print("Programmende Substraktion")

#2
print("Division zweier Zahlen")
wert1=int(input("Zahl1: "))
wert2=int(input("Zahl2: "))
ergebnis=wert1/wert2
print("Das Ergebnis der Division", wert1, "/", wert2, "ist", ergebnis)


#3
print("Ganzzahlige Division mit Rest")
dividend=int(input("Dividend: "))
divisor=int(input("Divisor: "))
ergebnis=dividend/divisor
rest=dividend%divisor
print("Das Ergebnis der Division", dividend, ":", divisor, "ist", ergebnis, "Rest:", rest)
print("Programmende Ganzzahldivision")

#4
print("Widerstands-Parallelschaltung")
r1=int(input("R1 in Ohm: "))
r2=int(input("R2 in Ohm: "))
rg=(r1*r2)/(r1+r2)
print("Der Gesamtwiderstand ist", rg, "Ohm")
print("Programmende ParallelR")

#5
import math
print("Punktabstand")
x1=int(input("1. Punkt x: "))
y1=int(input("1. Punkt y: "))
x2=int(input("2. Punkt x: "))
y2=int(input("2. Punkt y: "))
d=math.sqrt(((x2-x1)**2)+((y2-y1)**2))
print("Der Punkteabstand: ", d)
print("Programmende Punktabstand")

#6