import re


def diagonals(L):
    h, w = len(L), len(L[0])
    return [
        "".join([L[h - p + q - 1][q] for q in range(max(p - h + 1, 0), min(p + 1, w))])
        for p in range(h + w - 1)
    ]


with open("input.txt") as text:
    rows = [line.strip() for line in text]

columns = ["".join(line) for line in list(zip(*rows))]
diagonal_a = diagonals(rows)
diagonal_b = diagonals([r[::-1] for r in rows])

result = 0
for line in [*rows, *columns, *diagonal_a, *diagonal_b]:
    xmas = re.findall("XMAS", line)
    samx = re.findall("SAMX", line)
    result += len(xmas) + len(samx)


# Part 2
def x_mas(i, j, w):
    """
    corners [0 - 1]
            [- A -]
            [2 - 3]
    """
    corners = "".join(
        [w[i - 1][j - 1], w[i - 1][j + 1], w[i + 1][j - 1], w[i + 1][j + 1]]
    )
    return corners in ("SMSM", "MSMS", "MMSS", "SSMM")


def find_idx(s, C):
    idx = [i for i, c in enumerate(s) if c == C and 0 < i < len(s) - 1]
    return idx


result = 0
for i, row in enumerate(rows[1:-1]):
    for j in find_idx(row, "A"):
        result += int(x_mas(i + 1, j, rows))
print(result)
