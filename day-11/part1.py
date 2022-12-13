NUM_ROUNDS = 20


class Monkey:
    def __init__(self, *, items: list[int],
                 operation: str,
                 magnitude: int,
                 divisor,
                 true_monkey,
                 false_monkey):
        # Old worry level -> new worry level
        def inspect(old: int) -> int:
            self.items_inspected += 1
            value = old if magnitude == "old" else int(magnitude)

            if operation == "*":
                return old * value
            elif operation == "+":
                return old + value
            else:
                raise Exception(f"math operation {operation} not recognized")

        # Takes an item and returns the monkey to throw it to
        def toss(item: int) -> bool:
            if item % divisor == 0:
                return true_monkey
            else:
                return false_monkey

        self.divisor = divisor
        self.items = items
        self.inspect = inspect
        self.toss = toss
        self.get_bored = lambda item: item // 3
        self.items_inspected = 0

    def __str__(self):
        return str(self.__dict__)


def get_monkeys(file):
    monkeys_info = file.read().split("\n\n");
    monkeys: list[Monkey] = []
    for monkey_info in monkeys_info:
        monkey_info = [line.strip() for line in monkey_info.strip().splitlines()]
        items = [int(num_str.replace(" ", "")) for num_str in monkey_info[1].split(":")[1].split(", ")]
        operation, magnitude = monkey_info[2].split("old", 1)[1].strip().split()
        divisor = int(monkey_info[3].split(" by")[1])
        true_monkey = int(monkey_info[4].split("monkey ")[1])
        false_monkey = int(monkey_info[5].split("monkey ")[1])

        monkey = Monkey(items=items, operation=operation, magnitude=magnitude, divisor=divisor,
                        true_monkey=true_monkey, false_monkey=false_monkey)
        monkeys.append(monkey)

    return monkeys


def main():
    with open("input.txt") as file:
        monkeys = get_monkeys(file)

        for _ in range(NUM_ROUNDS):
            for monkey in monkeys:
                for item in monkey.items:
                    item = monkey.inspect(item)
                    item = monkey.get_bored(item)
                    target = monkey.toss(item)
                    monkeys[target].items.append(item)
                monkey.items = []

        m1, m2 = sorted(monkeys, key=lambda m: m.items_inspected)[-2:]
        part1_answer = m1.items_inspected * m2.items_inspected
        print(part1_answer)


if __name__ == "__main__":
    main()
