#Rock, Paper, Scissors, Lizard, Spock
winner = {'Rock': ['Lizard', 'Scissors'], 'Paper': ['Rock', 'Spock'], 'Scissors': ['Paper', 'Lizard'], 'Lizard': ['Spock', 'Paper'], 'Spock': ['Scissors', 'Rock']}
options = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']


class Player():
    def __init__(self, choice):
        self.choice = choice
        self.wins = 0
        self.losses = 0

    def get_choice(self):
        self.choice = input()
        while self.choice not in options:
            print('invalid choice, try again:')
            self.choice = input()
    
    def get_choice(self):
        self.choice = input()
        while self.choice not in options:
            print('invalid choice, try again:')
            self.choice = input()
    
    def winners(self, other):
        if other.choice in winner[self.choice]:
            print('User Wins!')
            self.wins +=1
            return 'User'
        elif self.choice in winner[other.choice]:
            print('Com Wins!')
            other.wins +=1
            return 'Com'
        else:
            print("It's a Draw.")

class Game():
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        
    '''def winners(self):
        if self.player2 in winner[self.player1]:
            print('User Wins!')
            return 'User'
        elif self.player1 in winner[self.player2]:
            print('Com Wins!')
            return 'Com'
        else:
            print("It's a Draw.")'''

    '''def get_choice(self):
        self.choice = input()
        while self.choice not in options:
            print('invalid choice, try again:')
            self.choice = input()'''

    '''def game_loop(self):
        user = Player(self.player1)
        computer = Player(self.player2)
        while user.player.wins < 3 and computer.player.wins < 3:
            if self.winners(self.player2.choice) == 'User':
                user.wins += 1
            choice = input()'''
            
        


import random
com_choice = random.choice(options)

choice = input()
while choice not in options:
    print('invalid choice, try again:')
    choice = input()


user = Player(choice)
computer = Player(com_choice)


while user.wins < 3 and computer.wins < 3:
    user.winners(computer)
    user.get_choice()
    computer.choice = random.choice(options)

if user.wins == 3:
    print('User is the Winner!')
else:
    print('Com is the Winner!')
print(user.wins, computer.wins)