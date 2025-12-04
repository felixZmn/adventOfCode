def main():
    sum = 0
    removed_in_previous = 1
    arr = []
    with open("./sample.txt") as f:
        arr = [list(line.rstrip("\n")) for line in f]

    while removed_in_previous > 0:
        removed_in_previous = 0
        for r, row in enumerate(arr):
            for c, val in enumerate(row):
                if val == "@":
                    if count_adjacent_rolls(arr, r, c) < 4:
                        removed_in_previous += 1
                        arr[r][c] = "."
                        sum += 1
    print(f"total removed rolls: {sum}")


def count_adjacent_rolls(data, x, y):
    rolls = 0
    # all 8 possible directions
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),          (0, 1),
                  (1, -1),  (1, 0),  (1, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(data) and 0 <= ny < len(data[0]):
            if data[nx][ny] == "@":
                rolls += 1
    return rolls


if __name__ == "__main__":
    main()
