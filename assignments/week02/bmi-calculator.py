weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height ** 2)

if bmi <= 18.5:
    print("Underweight")
elif bmi <= 24.9:
    print("Normal weingt")
elif bmi <= 29.9:
    print("Overweignt")
else:
    print("Obese")