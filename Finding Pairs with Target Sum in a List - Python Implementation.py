a = [2, 3, 6, 4, 4, 5]
target_sum = 8

pairs = []
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] + a[j] == target_sum:
            pairs.append((a[i], a[j]))

print(f"Pairs with sum {target_sum}: {pairs}")
