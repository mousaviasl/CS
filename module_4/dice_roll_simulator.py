import random

def print_histogram(rolls):
    total_rolls = sum(rolls.values())
    print("\nDICE ROLLING SIMULATION RESULTS")
    print(f"Total number of rolls = {total_rolls}.")

    for total, count in rolls.items():
        percentage = (count / total_rolls) * 100
        print(f"{total}: {'*' * int(percentage)}")

def main():
    print("Welcome to the dice throwing simulator!")
    num_simulations = int(input("How many dice rolls would you like to simulate? "))

    dice_rolls = {}

    for _ in range(num_simulations):
        roll = random.randint(1, 6) + random.randint(1, 6)
        if roll in dice_rolls:
            dice_rolls[roll] += 1
        else:
            dice_rolls[roll] = 1

    print("\nDICE ROLLING SIMULATION RESULTS")
    print(f"Total number of rolls = {num_simulations};")
    for total, count in sorted(dice_rolls.items()):
        print(f"{total}: {count}")

    print_histogram(dice_rolls)

    print("\nThank you for using the dice throwing simulator. Goodbye!")

if __name__ == "__main__":
    main()
