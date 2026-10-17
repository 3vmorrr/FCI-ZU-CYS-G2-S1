Fc = 60000
Cv = 9
P = 25

v = int(input("Enter The Volume : "))

TR = v * P
TC = Fc + (v * Cv)
Z = TR - TC

BEP_V = Fc / (P - Cv)

print (f"The TOtal Cost : {TC}.")
print (f"The TOtal Revinue : {TR}.")
print (f"The Profit : {Z}.")
print (f"The Volume That Make The BEP Is : {BEP_V} Reteread Tire.")