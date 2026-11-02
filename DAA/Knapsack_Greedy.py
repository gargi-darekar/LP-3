def fractional_knapsack(W, wt, val, n):
    items = sorted(
        zip(wt, val),
        key=lambda x: x[1] / x[0],
        reverse=True
    )

    total = 0

    for w, v in items:
        if W == 0:
            break
        if w <= W:
            total += v
            W -= w
        else:
            total += v * W / w
            W = 0

    return total


n = int(input("Enter number of items: "))
val = list(map(int, input("Enter values: ").split()))
wt = list(map(int, input("Enter weights: ").split()))
W = int(input("Enter knapsack capacity: "))

print("Maximum value:", fractional_knapsack(W, wt, val, n))
