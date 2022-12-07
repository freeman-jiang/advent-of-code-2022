file = open("input.txt")
contents = file.read()
lines = contents.splitlines()


def get_priority(c: str) -> int:
    if c.islower():
        return ord(c) - ord('a') + 1
    elif c.isupper():
        return ord(c) - ord('A') + 27


def chunk(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


groups = list(chunk(lines, 3))

total = 0

for group in groups:
    set1 = set(group[0])
    set2 = set(group[1])
    set3 = set(group[2])

    (item,) = set1 & set2 & set3
    total += get_priority(item)

print(total)
