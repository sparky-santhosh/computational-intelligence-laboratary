def activation(yin):
    for low, high, out in ranges:
        if low <= yin < high:
            return out
    print("Warning: yin not in any range:", yin)
    exit()

def train():
    global w, b
    max_epochs = 5
    for epoch in range(1, max_epochs + 1):
        print("\n===== Epoch", epoch, "=====")
        print("Inputs\t t\t yin\t y\t weights\t b")
        print("------------------------------------------------------------")
        error = False
        for row in data:
            x = row[:-1]
            t = row[-1]
            yin = b
            for i in range(n):
                yin += x[i] * w[i]
            y = activation(yin)
            print(f"{x}\t {t}\t {yin}\t {y}\t {w}\t {b}")
            if y != t:
                for i in range(n):
                    w[i] = w[i] + alpha * x[i] * t
                b = b + alpha * t
                error = True
        print("------------------------------------------------------------")
        print("Updated weights:", w, "b =", b)
        if not error:
            print("\nConverged at Epoch", epoch)
            return
    print("\nStopped at max epoch (5)")
    
data = []
with open("data.txt", "r") as f:
    for line in f:
        row = list(map(int, line.split()))
        data.append(row)

n = int(input("Enter number of inputs (n): "))
w = []
print("Enter initial weights:")
for i in range(n):
    w.append(float(input(f"w{i+1}: ")))

b = float(input("Enter bias (b): "))
alpha = float(input("Enter learning rate (alpha): "))

ranges = []
k = int(input("Enter number of activation ranges: "))
print("Enter ranges (low high output)")
print("NOTE: Use -99999 for -inf and 99999 for +inf")
for i in range(k):
    low = int(input(f"Range {i+1} low: "))
    high = int(input(f"Range {i+1} high: "))
    out = int(input(f"Output for this range: "))
    ranges.append((low, high, out))

train()

print("\nFinal Answer:")
print("Weights:", w)
print("Bias:", b)

