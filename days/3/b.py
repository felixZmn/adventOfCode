def main():
    sum = 0
    with open("./puzzle.txt") as f:
        for line in f:
            value = max_joltage(line.strip())
            sum += value
    print(f"sum of joltages: {sum}")


def max_joltage(s, length=11):
    first = max(s[:len(s)-length])
    index = s.index(first)
    new_s = s[index+1:]
    second = max_joltage(new_s, length-1) if length > 1 else max(new_s)
    return int(f"{first}{second}")


if __name__ == "__main__":
    main()
