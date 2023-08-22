import random

def stuck_in_the_mud():
    dice = [random.randint(1, 6) for _ in range(5)]
    score = sum([value for value in dice if value != 2 and value != 5])
    print("Stuck in the Mud")
    while True:
        choice = input("Press r to roll or q to quit: ")
        
        if choice == 'r':
            roll = [random.randint(1, 6) for _ in dice if _ != 2 and _ != 5]
            dice = roll
            score += sum(roll)
            print(f"You rolled: {roll}")
            print(f"Score: {score}")
            
            if len(dice) == 0:
                print("All dice are stuck in the mud.")
                break
        elif choice == 'q':
            print("Thanks for playing")
            break
        else:
            print("Invalid choice. Press r to roll or q to quit.")
stuck_in_the_mud()
