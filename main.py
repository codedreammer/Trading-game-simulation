import random

def trading_game():

    money = 1000
    rounds = int(input("Enter the number of rounds you want to play: "))
    marbles = ["green"] * 6 + ["red"] * 4

    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num}")
        bet = int(input("Enter your bet: "))
        
        if bet > money:
            print("You cannot bet more than you have!")
            continue
        
        drawn_marble = random.choice(marbles)
        print(f"You drew a {drawn_marble} marble.")
        
        if drawn_marble == "green":
            money += bet
            print(f"You won! Your balance is now {money} gold pieces.")
        else:
            money -= bet
            print(f"You lost! Your balance is now {money} gold pieces.")
        
        if money <= 500:
            print("You lost half of your money. Game over!")
            break
    
    print(f"\nGame finished! Your final balance is {money} gold pieces.")

# Bonus implementation:
def trading_game_bonus():
    # Initialize game variables
    money = 1000
    rounds = int(input("Enter the number of rounds you want to play: "))
    marbles = ["green"] * 5 + ["red"] * 3 + ["black"] * 1 + ["white"] * 1

    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num}")
        bet = int(input("Enter your bet: "))
        
        if bet > money:
            print("You cannot bet more than you have!")
            continue
        
        drawn_marble = random.choice(marbles)
        print(f"You drew a {drawn_marble} marble.")
        
        if drawn_marble == "green":
            money += bet
            print(f"You won! Your balance is now {money} gold pieces.")
        elif drawn_marble == "black":
            money += bet * 10
            print(f"Jackpot! You drew the black marble. Your balance is now {money} gold pieces.")
        elif drawn_marble == "white":
            money -= bet * 5
            print(f"Unlucky! You drew the white marble. Your balance is now {money} gold pieces.")
        else:
            money -= bet
            print(f"You lost! Your balance is now {money} gold pieces.")
        
        if money <= 500:
            print("You lost half of your money. Game over!")
            break
    
    print(f"\nGame finished! Your final balance is {money} gold pieces.")

# Run the program
trading_game()
