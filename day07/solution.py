from typing import Dict, List


def process_input(file_name: str) -> Dict[int, tuple]:
    result = {}
    with open(file_name) as text:
        for line in text:
            target, values = line.strip().split(":")
            result[int(target)] = tuple(int(v) for v in values.strip().split(" "))
    return result


def process_node(target: int, values: tuple) -> bool:
    # print(target, values)
    q, r = divmod(target, (next_target := values[-1]))
    # print(q, r)
    if len(values) == 1:
        return q == 1 and not r
    return process_node(target - next_target, values[:-1]) or (
        not r and process_node(q, values[:-1])
    )


equations = process_input("input.txt")

result = 0
for target, values in equations.items():
    if process_node(target, values):
        print(target, values)
        result += target

print(result)
