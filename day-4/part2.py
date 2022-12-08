def exists_overlap(a: str, b: str) -> bool:
    low_a, high_a = [int(x) for x in a.split("-")]
    low_b, high_b = [int(x) for x in b.split("-")]

    if high_a < low_b:
        return False

    if high_b < low_a:
        return False

    return True


def main():
    total = 0
    for pair in open("input.txt").read().splitlines():
        a, b = pair.split(",")
        if exists_overlap(a, b):
            total += 1

    print(total)


if __name__ == "__main__":
    main()
