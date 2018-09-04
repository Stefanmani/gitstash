#Verkefni 1
print("Massi í orku")
m_str = input('Input m: ')  # do not change this line
m_str = float(m_str)
c = 300000000 
e = m_str*(c**2)
print("e =", e)  # do not change this line

#Verkefni 2
print("Gera str tölu að integer og float")
in_str = input("Input s: ")
in_int = int(in_str)
print("in_int = ", in_int)
in_float = float(in_str)
print("in_float = ", in_float)

#Verkefni 3
print("Fjarlægð milli tveggja punkta")
import math
x1_str = input("Input x1: ")  # do not change this line
y1_str = input("Input y1: ")  # do not change this line
x2_str = input("Input x2: ")  # do not change this line
y2_str = input("Input y2: ")  # do not change this line
x1 = int(x1_str)
y1 = int(y1_str)
x2 = int(x2_str)
y2 = int(y2_str)
d = math.sqrt((x1-x2)**2+(y1 - y2)**2)
print("d =",d)  # do not change this line

#Verkefni 4
print("Tölur í runu af 6-tölum")
x_str = input("Input x: ")
# remember to convert to an int
x_str = int(x_str)
# first_three =
first_three = x_str // 1000
# last_two =
last_two = x_str % 100
# middle_two =
first_four = x_str // 100
middle_two = first_four % 100
print("original input:", x_str)
print("first_three:", first_three)
print("last_two:", last_two)
print("middle_two:", middle_two)

#Verkefni 5
print("Sekondur í klukkutíma,mínútur,sekondur")
secs_str = input("Input seconds: ") # do not change this line
secs_str = int(secs_str)
hours = secs_str // 3600
lefth = hours * 3600
minutes = (secs_str - lefth) // 60
leftm = minutes*60
seconds = (secs_str - lefth - leftm)
print(hours,":",minutes,":",seconds) # do not change this line

#Verkefni 6
print("BMI stig einstaklings")
weight_str = input("Weight (kg): ") # do not change this line
height_str = input("Height (cm): ") # do not change this line
bmi = float(weight_str)/(float(height_str)/100)**2
print("BMI is: ", bmi) # do not change this line

#Verkefni 7
print("US populatin eftir x mörg ár")
years_str = input("Years: ") # do not change this line
years_int = int(years_str)
pop = 307357870
years_sec = years_int*365*24*60*60
birth = years_sec/7
death = years_sec/13
immigrant = years_sec/35
new_population = birth - death + immigrant + pop
print("New population after", years_int, " years is ", int(new_population)) # do not change this line


