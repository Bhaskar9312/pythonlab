import random

class RPS:
    def __init__(self, n):
        self.n = n
        self.win = []

    def computer_choice(self):
        p = random.randint(1, 3)
        if p == 1:
            return 'rock'
        elif p == 2:
            return 'paper'
        elif p == 3:
            return 'scissor'

    def game(self):
        for i in range(self.n):
            g = self.computer_choice()
            print("Round", i + 1, "- Computer chose:", g, end=' ')
            v = input("Your move (rock/paper/scissor): ").lower()

            if v not in ['rock', 'paper', 'scissor']:
                print("Invalid move! Please enter rock, paper, or scissor.")
                continue

            if v == g:
                print("It's a tie!")
                self.win.append('tie')
            elif (v == 'rock' and g == 'scissor') or (v == 'paper' and g == 'rock') or (v == 'scissor' and g == 'paper'):
                print("You win this round!")
                self.win.append('win')
            else:
                print("You lose this round!")
                self.win.append('lose')

    def results(self):
        wins = self.win.count('win')
        losses = self.win.count('lose')
        ties = self.win.count('tie')
        print("\nResults after", self.n, "rounds:")
        print("Wins:", wins)
        print("Losses:", losses)
        print("Ties:", ties)

# Initialize game for 5 rounds
p1 = RPS(5)
p1.game()
p1.results()
