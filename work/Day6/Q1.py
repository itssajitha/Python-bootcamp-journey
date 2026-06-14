import random
names = ["Saji", "Binu", "Hayra", "Aysha", "Azim"]

try:
    index = int(input("Enter an index : "))
    print("Name at index:", names[index])

except ValueError:
    print("Invalid input")

except IndexError:
    print("Index out of range")

print("Randomly selected name:", random.choice(names))