import math

from part1 import get_monkeys

NUM_ROUNDS = 10000


def main():
    with open("input.txt") as file:
        monkeys = get_monkeys(file)

        all_divisors = [m.divisor for m in monkeys]
        product_of_all_divisors = math.prod(all_divisors)

        for round in range(NUM_ROUNDS):
            for monkey in monkeys:
                for item in monkey.items:
                    item = monkey.inspect(item)
                    target = monkey.toss(item)

                    # Post process to keep numbers small
                    item = item % product_of_all_divisors

                    monkeys[target].items.append(item)
                monkey.items = []

        for i, monkey in enumerate(monkeys):
            print(f"Monkey {i} inspected items {monkey.items_inspected} times.")

        most_active_monkeys = sorted(monkeys, key=lambda m: m.items_inspected)[-2:]
        print(math.prod([m.items_inspected for m in most_active_monkeys]))


if __name__ == "__main__":
    main()
