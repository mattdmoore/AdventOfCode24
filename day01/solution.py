with open("input.txt") as text:
    digits = [line.strip().split(" ") for line in text]

left = sorted([int(d[0]) for d in digits])
right = sorted([int(d[1]) for d in digits])
similarity_dict = {}
for r in right:
    if r in similarity_dict:
        similarity_dict[r] += r
    else:
        similarity_dict[r] = r
print(sum(similarity_dict[l] for l in left if l in similarity_dict))
