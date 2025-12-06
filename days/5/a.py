def main():
    sum = 0
    arr = []
    with open("./puzzle.txt") as f:
        arr = [line.strip() for line in f]

    split = next(i for i, line in enumerate(arr) if "-" not in line)

    # store ranges compactly
    good_ranges = []
    for line in arr[:split]:
        s, e = map(int, line.split("-"))
        good_ranges.append((s, e))

    # check ingredients
    for line in arr[split:]:
        if not line.strip():
            continue
        n = int(line)
        if in_ranges(n, good_ranges):
            sum += 1

    print(f"total fresh ingredients: {sum}")


def in_ranges(n, ranges):
    for s, e in ranges:
        if s <= n <= e:
            return True
    return False


if __name__ == "__main__":
    main()
