from enum import Enum


class Result(Enum):
    Unordered = 0
    Ordered = 1
    Continue = 2


DBG = False


def find_order(left: list | int, right: list | int) -> Result:
    if DBG:
        print(f"Comparing {left} and {right}")

    # Case 1: Two Integers
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return Result.Ordered
        elif left > right:
            return Result.Unordered
        else:
            return Result.Continue

    # Case 2: Two Lists
    if isinstance(left, list) and isinstance(right, list):
        if not left and right:
            return Result.Ordered
        elif not right and left:
            return Result.Unordered

        # We have two non-empty lists
        i = 0
        while True:
            if i == len(left) and i == len(right):
                return Result.Continue
            if i == len(left):  # Left ran out first
                return Result.Ordered
            if i == len(right):  # Right ran out first
                return Result.Unordered

            res = find_order(left[i], right[i])
            if res == Result.Continue:
                i += 1
            else:
                return res

    # Case 3: Mixed Types
    if isinstance(left, int):
        return find_order([left], right)
    else:
        return find_order(left, [right])
