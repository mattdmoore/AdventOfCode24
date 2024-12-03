import re

result = 0
do = True
with open("input.txt") as text:
    for line in text:
        pairs = re.findall("mul\((\d+),(\d+)\)|(do(n't)?\(\))", line)
        for a, b, flag, _ in pairs:
            match flag:
                case "do()":
                    do = True
                case "don't()":
                    do = False
            if do and not flag:
                result += int(a) * int(b)
print(result)
