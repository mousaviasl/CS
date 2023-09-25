class BaseballPlayer:
    
    def __init__(self):
        self.name = "none"
        self.number = "none"
        self.batting_avg = 0

    def calculate_batting_avg(self, incominghits, incoming_at_bats):
        self.batting_avg = round(incominghits / incoming_at_bats, 3)
        return self.batting_avg
        

#main program

print('Welcome to the program tracker!')
playerName = input("What is the player name?")
playerNumber = input("What is the player number?")

myPlayer = BaseballPlayer()

myPlayer.name = playerName
myPlayer.number = playerNumber

hits = int(input("How many hits did the player get?"))
at_bats = int(input("How mant attempts to hit the player get?"))
print(myPlayer.calculate_batting_avg(hits, at_bats))