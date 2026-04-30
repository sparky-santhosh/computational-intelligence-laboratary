TOTAL = 52

def show_result(name, favorable):
    print(f"\n--- {name} Calculation ---")
    print(f"Favorable outcomes = {favorable}")
    print(f"Total outcomes = {TOTAL}")
    print(f"Probability = {favorable}/{TOTAL}")
    print(f"Decimal = {round(favorable / TOTAL, 4)}")
    print("---------------------------")

while True:
    print("\n===== CARD PROBABILITY MENU =====")
    print("1. Heart")
    print("2. Face Card (J, Q, K)")
    print("3. Ace")
    print("4. Red Card")
    print("5. Black Card")
    print("6. Exit")

    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Please enter a valid number ")
        continue

    if choice == 1:
        show_result("Heart", 13)

    elif choice == 2:
        print("\nFace Cards = 3 (J,Q,K) * 4 suits = 12")
        show_result("Face Card", 12)

    elif choice == 3:
        show_result("Ace", 4)

    elif choice == 4:
        print("\nRed Cards = Hearts(13) + Diamonds(13) = 26")
        show_result("Red Card", 26)

    elif choice == 5:
        print("\nBlack Cards = Spades(13) + Clubs(13) = 26")
        show_result("Black Card", 26)

    elif choice == 6:
        print("Program Ended ")
        break

    else:
        print("Invalid choice ")

