result = 0
with open("input.txt") as text:
    for line in text:
        parsed = [int(x) for x in line.strip().split(" ")]
        diffs = [a - b for a, b in zip(parsed[1:], parsed[:-1])]

        if (
            all(diffs)
            and max(abs(d) for d in diffs) < 4
            and (all(d < 0 for d in diffs) or all(d > 0 for d in diffs))
        ):
            print(diffs, parsed)
            result += 1
print(result)
