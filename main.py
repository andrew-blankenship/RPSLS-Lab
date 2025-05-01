#Rock, Paper, Scissors, Lizard, Spock
import random

winner = {'Rock': ['Lizard', 'Scissors'], 'Paper': ['Rock', 'Spock'], 'Scissors': ['Paper', 'Lizard'], 'Lizard': ['Spock', 'Paper'], 'Spock': ['Scissors', 'Rock']}
options = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']

print('\nWelcome to Rock, Paper, Scissors, Lizard, Spock!\nFirst to 3 points wins!')
print('To play you will pick one of the 5 options (Rock, Paper, Scissors, Lizard, Spock)\nThe computer will then randomly select an option\nA winner will then be determined as in the original Rock Paper Scissors except each option now defeats and loses to two other options')
print('To start the game please type in one of the following choices Rock, Paper, Scissors, Lizard, or Spock')
print('Make sure that you spell your choice correctly and start with a capital letter.')

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
        counter = 1
        while self.player1.wins < 3 and self.player2.wins < 3:
            print(f'Round {counter}:')
            self.player1.get_choice()
            self.player2.choice = random.choice(options)
            print(f'Com chose: {self.player2.choice}')
            self.winners()
            print(f'Current score: User: {self.player1.wins} Com: {self.player2.wins}\n----------\n')
            counter +=1

        if self.player1.wins == 3:
            print('User is the Winner!')
        else:
            print('Com is the Winner!')
        print(f'Final score: User: {self.player1.wins} Com: {self.player2.wins}')
        print('Thanks for playing!')
            
        




user = Player()
computer = Player()




game = Game(user, computer)
game.game_loop()