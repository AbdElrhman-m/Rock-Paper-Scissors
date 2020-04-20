#!/usr/bin/env python3
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        super().__init__()
        self.score = 0
        self.valid_moves = ["rock", "paper", "scissors"]
        self.my_move = None
        self.their_move = None
        
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move

class RandomPlayer(Player):
    def move(self):
        return random.choice(self.valid_moves)


class HumanPlayer(Player):
    def move(self):
        player_move = input("Rock, paper, scissors? > ").lower()
        if player_move in self.valid_moves:
            return player_move
        else:
            return self.move()

class ReflectPlayer(Player):
    def move(self):
        if self.their_move == None:
            return random.choice(self.valid_moves)
        else:
            return self.their_move

def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(" ")
            print(f"Round {round}:")
            self.play_round()
            self.keep_score()
        print(f"Score: Player 1: {self.p1.score}  Player 2: {self.p2.score}")
        print(" ")
        print("Game over!")

    def keep_score(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        if beats(move1, move2):
            print("*************Player *one* is the Winner************")
            self.p1.score += 1
        elif move1 == move2:
            print("********************** Draw! **********************")
        else:
            print("*************Player *Two* is the Winner************")
            self.p2.score += 1

if __name__ == '__main__':
    game = Game(ReflectPlayer(), HumanPlayer())
    game.play_game()
