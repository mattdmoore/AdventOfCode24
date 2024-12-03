with open("input.txt") as text:
    digits = [line.strip().split(" ") for line in text]

left = sorted([int(d[0]) for d in digits])
right = sorted([int(d[1]) for d in digits])
similarity_dict = {}
for val in right:
    if val in similarity_dict:
        similarity_dict[val] += val
    else:
        similarity_dict[val] = val

result = sum(similarity_dict[val] for val in left if val in similarity_dict)
print(result)
