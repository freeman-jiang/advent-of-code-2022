file = open("input.txt")
contents = file.read()
lines = contents.splitlines()


def get_priority(c: str) -> int:
    if c.islower():
        return ord(c) - ord('a') + 1
    elif c.isupper():
        return ord(c) - ord('A') + 27


total = 0

for rucksack in lines:
    halfway = len(rucksack) // 2
    left = rucksack[:halfway]
    right = rucksack[halfway:]
    seen = set(left)

    for item in right:
        if item in seen:
            total += get_priority(item)
            break

print(total)
