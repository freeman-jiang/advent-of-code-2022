from enum import Enum


class Direction(str, Enum):
    UP = "U"
    LEFT = "L"
    DOWN = "D"
    RIGHT = "R"


# Returns the new tail. Could be the same if a change is not needed
def update_tail(head_location: tuple[int, int], tail_location: tuple[int, int]) -> tuple[int, int]:
    head_x, head_y = head_location
    tail_x, tail_y = tail_location

    # Check if touching
    if abs(head_x - tail_x) <= 1 and abs(head_y - tail_y) <= 1:
        return tail_x, tail_y

    # Process straight lines if the head and tail share a common x/y
    if head_y == tail_y or head_x == tail_x:
        if head_y - tail_y == 2:  # Head is 2 above tail
            tail_y += 1
        elif head_y - tail_y == -2:  # Head is 2 below tail
            tail_y -= 1
        elif head_x - tail_x == 2:  # Head is 2 right of tail
            tail_x += 1
        elif head_x - tail_x == -2:  # Head is 2 left of tail
            tail_x -= 1

    # Process diagonals
    else:
        if head_y > tail_y and head_x > tail_x:  # Head is diagonal up right
            tail_y += 1
            tail_x += 1
        elif head_y > tail_y and head_x < tail_x:  # Head is diagonal up left
            tail_y += 1
            tail_x -= 1
        elif head_y < tail_y and head_x > tail_x:  # Head is diagonal down right
            tail_y -= 1
            tail_x += 1
        elif head_y < tail_y and head_x < tail_x:  # Head is diagonal down left
            tail_y -= 1
            tail_x -= 1

    # Return the new coordinates for the tail
    return tail_x, tail_y


def main():
    with open("input.txt") as file:
        tail_location = (0, 0)
        head_location = (0, 0)

        # You may also use an OrderedDict[tuple[int, int], None] if you want to maintain insertion order
        visited: set[tuple[int, int]] = {head_location}

        for line in file.read().splitlines():
            direction, multiplier = line.split()
            multiplier = int(multiplier)
            head_x, head_y = head_location

            if direction == Direction.UP:
                for _ in range(multiplier):
                    head_location = (head_x, head_y + 1)
                    head_x, head_y = head_location
                    tail_location = update_tail(head_location, tail_location)
                    visited.add(tail_location)
            elif direction == Direction.DOWN:
                for _ in range(multiplier):
                    head_location = (head_x, head_y - 1)
                    head_x, head_y = head_location
                    tail_location = update_tail(head_location, tail_location)
                    visited.add(tail_location)
            elif direction == Direction.LEFT:
                for _ in range(multiplier):
                    head_location = (head_x - 1, head_y)
                    head_x, head_y = head_location
                    tail_location = update_tail(head_location, tail_location)
                    visited.add(tail_location)
            elif direction == Direction.RIGHT:
                for _ in range(multiplier):
                    head_location = (head_x + 1, head_y)
                    head_x, head_y = head_location
                    tail_location = update_tail(head_location, tail_location)
                    visited.add(tail_location)

        answer = len(visited)
        print(answer)


if __name__ == "__main__":
    main()
