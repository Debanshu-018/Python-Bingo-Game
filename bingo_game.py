import random

SIZE = 5

def generate_card():
    numbers = random.sample(range(1, 76), SIZE * SIZE)
    card = [numbersi * SIZE:(i + 1) * SIZE] for i in range(SIZE)]
    card[2][2] = "FREE"
    return card

def mark_number(card, number):
    for i in range(SIZE):
        for j in range(SIZE):
            if card[i][j] == number:
                card[i][j] = "X"

def print_card(card, title):
    print(f"\n{title}")
    print("-" * 30)
    for row in card:
        print(" ".join(f"{str(x):>4}" for x in row))
    print("-" * 30)

def bingo_count(card):
    count = 0

    # Rows
    for row in card:
        if all(x == "X" or x == "FREE" for x in row):
            count += 1

    # Columns
    for col in range(SIZE):
        if all(card[row][col] == "X" or card[row][col] == "FREE" for row in range(SIZE)):
            count += 1

    # Main diagonal
    if all(card[i][i] == "X" or card[i][i] == "FREE" for i in range(SIZE)):
        count += 1

    # Other diagonal
    if all(card[i][SIZE - 1 - i] == "X" or card[i][SIZE - 1 - i] == "FREE" for i in range(SIZE)):
        count += 1

    return count

def main():
    print("=" * 40)
    print("        PYTHON BINGO GAME")
    print("=" * 40)

    player = generate_card()
    computer = generate_card()

    called = []

    while True:
        print_card(player, "Your Card")

        input("\nPress Enter to draw a number.....")

        remaining = list(set(range(1, 76)) - set(called))
        number = random.choice(remaining)
        called.append(number)

        print(f"\nNumber Called: {number}")

        mark_number(player, number)
        mark_number(computer, number)

        player_score = bingo_count(player)
        computer_score = bingo_count(computer)

        print(f"Your Bingo Lines: {player_score}")
        print(f"Computer Bingo Lines: {computer_score}")

        if player_score >= 5 and computer_score >= 5:
            print("\nIt's a Draw!")
            break
        elif player_score >= 5:
            print("\n🎉 Congratulations! You Win!")
            break
        elif computer_score >= 5:
            print("\n💻 Computer Wins!")
            break

if __name__ == "__main__":
    main()
