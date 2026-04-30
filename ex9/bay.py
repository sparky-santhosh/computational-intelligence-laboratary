def read_data():
    data = []
    # Make sure data.txt exists in the same folder!
    try:
        with open("data.txt", "r") as f:
            next(f)  # skip header
            for line in f:
                a, b, c = map(int, line.strip().split())
                data.append((a, b, c))
    except FileNotFoundError:
        print("Error: data.txt not found!")
        return []
    return data


def calculate_probabilities(data):
    total = len(data)
    if total == 0:
        print("No data to process.")
        return

    count_A = sum(1 for a,b,c in data if a == 1)
    count_B = sum(1 for a,b,c in data if b == 1)
    count_C = sum(1 for a,b,c in data if c == 1)

    count_AB = sum(1 for a,b,c in data if a == 1 and b == 1)

    # Probabilities
    P_A = count_A / total
    P_B = count_B / total
    P_C = count_C / total
    P_AB = count_AB / total

    P_B_given_A = count_AB / count_A if count_A != 0 else 0
    P_A_given_B = count_AB / count_B if count_B != 0 else 0

    print("\n--- Counts ---")
    print(f"Total = {total}")
    print(f"A=1 count = {count_A}")
    print(f"B=1 count = {count_B}")
    print(f"C=1 count = {count_C}")
    print(f"A and B count = {count_AB}") # Fixed symbol here

    print("\n--- Probabilities ---")

    print("\n1. Joint Probability")
    print("P(A and B) = count(A and B) / total") # Fixed symbol here
    print(f"P(A and B) = {count_AB}/{total} = {P_AB}")

    print("\n2. Marginal Probability")
    print("P(A) = count(A) / total")
    print(f"P(A) = {count_A}/{total} = {P_A}")

    print("\n3. Conditional Probability")
    print("P(A|B) = count(A and B) / count(B)") # Fixed symbol here
    print(f"P(A|B) = {count_AB}/{count_B} = {P_A_given_B}")

    print("\n4. Bayes Theorem")
    print("P(A|B) = [P(B|A) * P(A)] / P(B)")
    print(f"P(B|A) = {count_AB}/{count_A} = {P_B_given_A}")
    print(f"P(A) = {P_A}")
    print(f"P(B) = {P_B}")

    if P_B != 0:
        bayes = (P_B_given_A * P_A) / P_B
        print(f"P(A|B) = ({P_B_given_A} * {P_A}) / {P_B}")
        print(f"Result = {bayes}")
    else:
        print("Cannot divide by zero")


# Run
data = read_data()
if data:
    calculate_probabilities(data)
