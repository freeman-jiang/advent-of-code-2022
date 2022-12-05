file = open("input.txt")

contents = file.read()
elves = contents.split("\n\n")

max_calories = 0

for elf in elves:
    calories = [int(x) for x in elf.split()]
    total_calories = sum(calories)
    max_calories = max(max_calories, total_calories)

print(max_calories)
