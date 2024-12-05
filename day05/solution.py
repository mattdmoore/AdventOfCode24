with open("input.txt") as text:
    rules = [line.strip() for line in text]


def is_correctly_ordered(update, rules_dict):
    return not any(
        int(x) in rules_dict[u] for i, u in enumerate(update[::-1]) for x in update[:-i]
    )


updates = []
while rule := rules.pop():
    updates.append(rule)

rules_dict = {}
for rule in rules:
    x, y = rule.split("|")
    if x in rules_dict:
        rules_dict[x].add(int(y))
    else:
        rules_dict[x] = {int(y)}

result = 0
for update in updates:
    update = update.split(",")
    if is_correctly_ordered(update, rules_dict):
        result += int(update[len(update) // 2])

print(result)
