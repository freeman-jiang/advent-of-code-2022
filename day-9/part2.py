from part1 import update_tail
from part1 import Direction


def main():
    with open("input.txt") as file:
        # rope[0] is the head, followed by the 9 knots where rope[9] is the tail
        rope: list[tuple[int, int]] = list(zip((0,) * 10, (0,) * 10))
        tail_visited: set[tuple[int, int]] = {(0, 0)}

        for line in file.read().splitlines():
            direction, multiplier = line.split()
            multiplier = int(multiplier)
            head_x, head_y = rope[0]

            if direction == Direction.UP:
                for _ in range(multiplier):
                    # Update the true head
                    rope[0] = (head_x, head_y + 1)
                    head_x, head_y = rope[0]

                    # Update the rest of the rope
                    for i in range(1, len(rope)):
                        rope[i] = update_tail(head_location=rope[i - 1], tail_location=rope[i])

                    tail_visited.add(rope[9])
            elif direction == Direction.DOWN:
                for _ in range(multiplier):
                    rope[0] = (head_x, head_y - 1)
                    head_x, head_y = rope[0]

                    for i in range(1, len(rope)):
                        rope[i] = update_tail(head_location=rope[i - 1], tail_location=rope[i])

                    tail_visited.add(rope[9])
            elif direction == Direction.LEFT:
                for _ in range(multiplier):
                    rope[0] = (head_x - 1, head_y)
                    head_x, head_y = rope[0]

                    for i in range(1, len(rope)):
                        rope[i] = update_tail(head_location=rope[i - 1], tail_location=rope[i])

                    tail_visited.add(rope[9])
            elif direction == Direction.RIGHT:
                for _ in range(multiplier):
                    rope[0] = (head_x + 1, head_y)
                    head_x, head_y = rope[0]

                    for i in range(1, len(rope)):
                        rope[i] = update_tail(head_location=rope[i - 1], tail_location=rope[i])

                    tail_visited.add(rope[9])

        answer = len(tail_visited)
        print(answer)


if __name__ == "__main__":
    main()
