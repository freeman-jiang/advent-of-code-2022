def exists_total_overlap(a: str, b: str) -> bool:
    low_a, high_a = a.split("-")
    low_b, high_b = b.split("-")

    low_a = int(low_a)
    high_a = int(high_a)
    low_b = int(low_b)
    high_b = int(high_b)

    if low_a <= low_b and high_a >= high_b:
        return True

    if low_b <= low_a and high_b >= high_a:
        return True

    return False


def main():
    pairs = open("input.txt").read().splitlines()
    total = 0

    for pair in pairs:
        a, b = pair.split(",")
        if exists_total_overlap(a, b):
            total += 1

    print(total)


if __name__ == "__main__":
    main()
