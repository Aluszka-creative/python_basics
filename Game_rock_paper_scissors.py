# Game Rock - Paper - Scissors
import random

def kpn(wins, n):
    player_wins = int(0)
    computer_wins = int(0)

    for i in range(0, int(n)):
        while int(player_wins) < int(wins) and int(computer_wins) < int(wins):

                # What beats: What
                dict = {'Rock':'Scissors', 'Paper':'Rock', 'Scissors':'Paper'}

                # Random choice from the list
                list = ['Rock', 'Scissors', 'Paper']
                comp_choice = random.choice(list)

                # Player choice
                print('Write your choice')
                player_choice = input()

                # Conditions
                if dict[player_choice] == comp_choice:
                    player_wins += 1
                elif dict[comp_choice] == player_choice:
                    computer_wins += 1

                if player_choice != '':
                    print(comp_choice)

                print(str(comp_choice) + ' vs ' + str(player_choice))

        # /while
        winner = 'Winner: '
        if int(computer_wins) == int(wins):
            winner += 'Computer'
        elif int(player_wins) == int(wins):
            winner += 'Player ' + str(name)
        else:
            print('We have a tie :D')

    return winner

print('Welcome in a game Rock-Paper-Scissors, what is your name?')
name = input()
print('Hi, ' + name + '. Let\'s play! :)')
print('When you will write your choice computer will write his. You can chose Rock or Paper or Scissors')
print('Write number of wins')
wins = int(input())
print('Write number of rounds.')
n = int(input())
print(kpn(wins, n))
