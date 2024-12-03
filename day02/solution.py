from typing import Sequence

result = 0


def is_safe(level: Sequence[int]) -> bool:
    increasing = all(1 <= a - b <= 3 for a, b in zip(level[1:], level[:-1]))
    decreasing = all(1 <= a - b <= 3 for a, b in zip(level[:-1], level[1:]))
    return increasing or decreasing


with open("input.txt") as text:
    for line in text:
        report = [int(x) for x in line.strip().split(" ")]

        if is_safe(report):
            result += 1
        else:
            for i, _ in enumerate(report):
                if is_safe(report[:i] + report[i+1:]):
                    result += 1
                    break

print(result)
