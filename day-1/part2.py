file = open("input.txt")

contents = file.read()
elves = contents.split("\n\n")

calorie_list: list[int] = []

for elf in elves:
    calories = [int(x) for x in elf.split()]
    total_calories = sum(calories)
    calorie_list.append(total_calories)

calorie_list.sort(reverse=True)
top_3_total = sum(calorie_list[0:3])
print(top_3_total)
