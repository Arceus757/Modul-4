#1 Gröna Lund (Längdcheck)

# print ("Du måste vara minst 160 cm lång för att få åka på attraktion 1")
# print ("Låt oss se om du är tillräcklig lång")

# Längd = float(input("Ange din längd: "))

# if Längd >= 160:
#     print ("Godkänd")

# elif Längd < 160:
#     print ("Stick härifrån")

# else:
#     print("man får bara skriva i siffror")

# #2 Förbättra välkomstprogrammet (nu med koll att man skriver in rätt typ av värden). Använd try
# while True:
#     try:
#         namn = input("Vad heter du? ")
#         if namn.isalpha():
#             break
#         else:
#             raise ValueError
#     except ValueError:
#         print("Felaktig inmatning. Var god och ange enbart bokstäver.")

# print("Hej " + namn + "! Välkommen till programmet!")

#3 Förbättra BMI-kalkylatorn (se till att stoppa användaren från att skriva in fel)
# from math import floor

# while True:
#    print("-------------------------------------------")
#    print("Welcome to the free BMI calculator")
#    try:
#        weight = float(input("Enter your weight(kg): "))
#    except ValueError:
#        print("'!!!Enter a number pls!!!")
#        continue

#    try:
#        height = float(input("Enter your height(m): "))
#    except ValueError:
#        print("'!!!Enter a number pls!!!\n")
#        continue
#    bmi = floor((weight / height ** 2) * 10) / 10

#    while True:
#      is_correct = input(f"\n(weight {weight}kg | height {height}m) is this correct? (Yes/No): ")
#      if is_correct == "No":
#         break
#      elif is_correct == "Yes":
#          print(f"Your BMI is: {bmi}")
#          if bmi < 18.5:
#              print("You are underweight.\n")
#              exit ()
#          elif bmi <= 24.9:
#              print("You are healthy.\n")
#              exit ()
#          elif bmi <= 29.9:
#              print("You are over weight.\n")
#              exit ()
#          elif bmi <= 34.9:
#              print("You are severely over weight.\n")
#              exit ()
#          elif bmi <= 39.9:
#              print("You are obese.\n")
#              exit ()
#          else:
#              print("You are severely obese.\n")
#              exit ()
#      else:
#          print("!!!Please enter (Yes) or (NO)!!!")
    
#4 Skapa ett program som beräknar arean på en cirkel (r*r*pi)
# import math

# def beräkna_area(r):
#     area = math.pi * r * r
#     return area

# radie = float(input("Ange radien på cirkeln: "))
# area = beräkna_area(radie)
# print("Arean på cirkeln är:", area)

# #5 Gör en miniräknare som kan räkna med alla fyra räknesätt
# def addition(a, b):
#     return a + b

# def subtraktion(a, b):
#     return a - b

# def multiplikation(a, b):
#     return a * b

# def division(a, b):
#     return a / b

# print("Välkommen till miniräknaren!")

# tal1 = float(input("Ange det första talet: "))
# tal2 = float(input("Ange det andra talet: "))

# summa = addition(tal1, tal2)
# print("Summan är:", summa)

# diff = subtraktion(tal1, tal2)
# print("Skillnaden är:", diff)

# produkt = multiplikation(tal1, tal2)
# print("Produkten är:", produkt)

# kvot = division(tal1, tal2)
# print("Kvoten är:", kvot)

# #6 Tärning med random.randint()
# import random

# def kasta_tarning():
#     return random.randint(1, 6)

# tarning_resultat = kasta_tarning()
# print("Tärningen visar:", tarning_resultat)

#7 Gör ett program som kastar så många tärningar som användaren väljer
import random

def kasta_tarning(antal_tarningar):
    resultat = []
    for _ in range(antal_tarningar):
        resultat.append(random.randint(1, 6))
    return resultat

antal = int(input("Hur många tärningar vill du kasta? "))
tarning_resultat = kasta_tarning(antal)
print("Tärningsresultat:", tarning_resultat)
             