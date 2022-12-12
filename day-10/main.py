def main():
    with open("input.txt") as file:
        register_value = 1

        # history[i] gives the value of the register `x` during the ith cycle
        history: list[int] = [-1]

        for line in file.read().splitlines():
            if line == "noop":
                history.append(register_value)
            else:
                value = int(line.split()[1])
                history.append(register_value)
                history.append(register_value)
                register_value += value

        history.append(register_value)

        signal_cycles = {20, 60, 100, 140, 180, 220}

        part1_answer = sum([cycle * value for (cycle, value) in enumerate(history) if cycle in signal_cycles])
        print(part1_answer)

        # Stupid indexing thing because the history array is 1-indexed, but the pixel is not
        for cycle, position in enumerate(history[1:], 1):
            pixel_position = (cycle - 1) % 40
            sprite_position = history[cycle]

            # Changed the printing characters so it's more legible
            if abs(sprite_position - pixel_position) <= 1:
                print("O", end="")
            else:
                print(" ", end="")

            if cycle % 40 == 0:
                print()  # newline


if __name__ == "__main__":
    main()
