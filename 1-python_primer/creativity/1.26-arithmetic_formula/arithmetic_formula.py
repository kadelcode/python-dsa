# Input three (3) integers
a = int(input("Enter the first integer (a): "))
b = int(input("Enter the second integer (b): "))
c = int(input("Enter the third integer (c): "))


# Check if the integers satisfy any of the formulas
if a + b == c:
    print(f"{a} + {b} = {c} is a valid formula.")

elif a == b - c:
    print(f"{a} = {b} - {c} is a valid formula.")

elif a * b == c:
    print(f"{a} * {b} = {c} is a valid formula.")

else:
    print("No valid arithmetic formula found.")