def main():
    import re

    with open("input.txt") as file:
        contents = file.read()
        info, instructions = contents.strip().split("\n\n")
        info = info.splitlines()

        stacks = {}
        idx_to_label = {}

        # The last line contains the stack numbers
        for i, c in enumerate(info.pop()):
            if c.isdigit():
                idx_to_label[i] = c
                stacks[c] = []

        # Add the elements to the appropriate stack
        for line in reversed(info):
            for i, element in enumerate(line):
                if i in idx_to_label and not element.isspace():
                    c = idx_to_label[i]
                    stacks[c].append(element)

        # Parse instructions
        for instruction in instructions.splitlines():
            amount, origin, destination = re.findall(r"\b\d+\b", instruction)
            for i in range(int(amount)):
                item = stacks[origin].pop()
                stacks[destination].append(item)

        tops = ""

        # Sort by stack number
        for number, stack in sorted(stacks.items()):
            tops += stack[-1]

        print(tops)


if __name__ == "__main__":
    main()
