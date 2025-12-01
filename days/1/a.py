def main():
    dial = 50
    counter = 0

    with open("./days/1/puzzle.txt") as f:
        for line in f:
            direction, steps = line[0], int(line[1:])

            if direction == "L":
                dial = (dial - steps) % 100
            else:
                dial = (dial + steps) % 100

            counter += dial == 0

        print(f"total times 0: {counter}")


if __name__ == "__main__":
    main()
