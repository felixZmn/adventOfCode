def main():
    sum = 0
    with open("./puzzle.txt") as f:
        for line in f:
            value = max_joltage(line.strip())
            sum += value
    print(f"sum of joltages: {sum}")


def max_joltage(s):
    first = max(s[:len(s)-1])
    index = s.index(first)
    second = max(s[index+1:])
    return int(f"{first}{second}")


if __name__ == "__main__":
    main()
