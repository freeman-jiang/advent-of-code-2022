from order_checker import find_order, Result

DIVIDER_PACKETS = [[[2]], [[6]]]


def custom_cmp(left: list | int, right: list | int) -> -1 | 0 | 1:
    ordering = find_order(left, right)
    if ordering == Result.Ordered:
        return -1
    if ordering == Result.Unordered:
        return 1
    return 0


def main():
    with open("input.txt") as file:
        raw_packets = file.read().split("\n\n")
        parsed_packets = DIVIDER_PACKETS
        part1 = 0

        for index, pairs in enumerate(raw_packets, start=1):
            left, right = [eval(x) for x in pairs.split()]
            parsed_packets.extend([left, right])
            ordering = find_order(left, right)

            match ordering:
                case Result.Ordered:
                    part1 += index
                case Result.Unordered:
                    continue
                case Result.Continue:
                    raise Exception(f"Lists are identical {left}, {right}")

        print(part1)

        import functools
        import math
        sorted_packets = sorted(parsed_packets, key=functools.cmp_to_key(custom_cmp))
        decoder_key = math.prod([index for index, packet in enumerate(sorted_packets, 1) if
                                 packet == DIVIDER_PACKETS[0] or packet == DIVIDER_PACKETS[1]])
        print(decoder_key)


if __name__ == "__main__":
    main()
