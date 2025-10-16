colors = []
n = int(input("Enter total number of colors: "))
print("Enter colors:")

for i in range(n):
    color = input(f"Color {i+1}: ")
    colors.append(color)

if colors:
    print(f"\nFirst color is: {colors[0]}")
    print(f"Last color is: {colors[-1]}")
else:
    print("No colors were entered.")
