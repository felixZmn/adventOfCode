def main():
    sum = 0
    with open("./puzzle.txt") as f:
        for line in f:
            ranges = line.strip().split(",")
            for r in ranges:
                start, end = r.split("-")
                for i in range(int(start), int(end)+1):
                    if is_reversable(str(i)):
                        sum += i
    print(f"sum of reversable numbers: {sum}")


def is_reversable(s):
    length = len(s)

    if length % 2 != 0:
        return False

    half = length // 2
    if s[:half] == s[half:]:
        return True
    return False


if __name__ == "__main__":
    main()
