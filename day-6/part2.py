WINDOW_SIZE = 14


def main():
    with open("input.txt") as file:
        datastream = file.read().strip()

        for i, c in enumerate(datastream):
            window = datastream[i:i + WINDOW_SIZE]
            # print(window)
            if len(window) == len(set(window)):
                answer = i + WINDOW_SIZE
                print(answer)
                return


if __name__ == "__main__":
    main()
