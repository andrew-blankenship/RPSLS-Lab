#Rock, Paper, Scissors, Lizard, Spock
import random

winner = {'Rock': ['Lizard', 'Scissors'], 'Paper': ['Rock', 'Spock'], 'Scissors': ['Paper', 'Lizard'], 'Lizard': ['Spock', 'Paper'], 'Spock': ['Scissors', 'Rock']}
options = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

print('Welcome to Rock, Paper, Scissors, Lizard, Spock!\n First to 3 points wins!\n To start the game please type in one of the following choices Rock, Paper, Scissors, Lizard, or Spock')



class Player():
    def __init__(self):
        self.choice = 'none'
        self.wins = 0
        self.losses = 0

    def get_choice(self):
        print('Please make your selection:')
        self.choice = input()
        while self.choice not in options:
            print('invalid choice, try again:')
            self.choice = input()
    
    
    

class Game():
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        
    
    def winners(self):
        if self.player2.choice in winner[self.player1.choice]:
            print('User Wins!')
            self.player1.wins +=1
            return 'User'
        elif self.player1.choice in winner[self.player2.choice]:
            print('Com Wins!')
            self.player2.wins +=1
            return 'Com'
        else:
            print("It's a Draw.")

    def game_loop(self):
        while self.player1.wins < 3 and self.player2.wins < 3:
            self.player1.get_choice()
            self.player2.choice = random.choice(options)
            self.winners()

        if self.player1.wins == 3:
            print('User is the Winner!')
        else:
            print('Com is the Winner!')
        print(f'Final score:\n User: {self.player1.wins} Com: {self.player2.wins}')
            
        




user = Player()
computer = Player()




game = Game(user, computer)
game.game_loop()