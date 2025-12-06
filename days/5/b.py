def main():
    total = 0
    arr = []
    with open("./puzzle.txt") as f:
        arr = [line.strip() for line in f]

    split = next(i for i, line in enumerate(arr) if "-" not in line)

    # store ranges compactly
    good_ranges = []
    for line in arr[:split]:
        s, e = map(int, line.split("-"))
        good_ranges.append((s, e))

    good_ranges.sort()  # sort by start
    merged = []

    for s, e in good_ranges:
        if not merged:
            merged.append([s, e])
        else:
            last_s, last_e = merged[-1]
            if s <= last_e + 1:
                merged[-1][1] = max(last_e, e)
            else:
                merged.append([s, e])

    total = 0
    for s, e in merged:
        total += (e - s + 1)

    print(f"total fresh ingredients: {total}")


def in_ranges(n, ranges):
    for s, e in ranges:
        if s <= n <= e:
            return True
    return False


if __name__ == "__main__":
    main()
