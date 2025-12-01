def main():
    current_position = 50
    counter = 0

    with open("./days/1/puzzle.txt") as f:
        for line in f:
            direction, steps = line[0], int(line[1:])

            counter += steps // 100
            remaining_steps = steps % 100

            if direction == "L":
                new_position = (current_position - remaining_steps) % 100
                if current_position != 0 and current_position - remaining_steps <= 0:
                    counter = counter + 1

            else:
                new_position = (current_position + remaining_steps) % 100
                if current_position != 0 and current_position + remaining_steps >= 100:
                    counter = counter + 1

            current_position = new_position

        print(f"total times 0: {counter}")


if __name__ == "__main__":
    main()
