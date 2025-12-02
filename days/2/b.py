import re

regex = r"^(.+)\1+$"


def main():
    sum = 0
    with open("./puzzle.txt") as f:
        for line in f:
            ranges = line.strip().split(",")
            for r in ranges:
                start, end = r.split("-")
                for i in range(int(start), int(end)+1):
                    if has_repetitions(str(i)):
                        sum += i
    print(f"sum of matching numbers: {sum}")


def has_repetitions(s):
    if re.match(regex, s):
        return True
    return False


if __name__ == "__main__":
    main()
