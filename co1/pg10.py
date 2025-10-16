n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))

largest = n1  # assume n1 is largest

if n2 > largest:
    largest = n2
if n3 > largest:
    largest = n3

print(f"Largest number is: {largest}")
