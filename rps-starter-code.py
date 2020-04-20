#!/usr/bin/env python3
import random
import time as t
import datetime
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


def print_pause(message, delay=2):
    # printes a message with delay
    # default delay = 2
    print(message)
    t.sleep(delay)


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
    def __init__(self):
        super().__init__()
        self.name = "Player 1"

    def move(self):
        try:
            player_move = input("Rock, paper, scissors? > ").lower()
        except KeyboardInterrupt:
            self.move()

        if player_move in self.valid_moves:
            return player_move
        else:
            return self.move()

    def enter_name(self):
        try:
            player_name = input("Enter your name > ").capitalize()
        except KeyboardInterrupt:
            self.enter_name()

        if player_name.isalpha():
            self.name = player_name
        else:
            print_pause("please enter your name without numbers,"
                        " spaces or any symboles!")
            self.enter_name()


class ReflectPlayer(Player):
    def move(self):
        if self.their_move is None:
            return random.choice(self.valid_moves)
        else:
            return self.their_move


class CyclePlayer(Player):
    def move(self):
        if self.my_move is None:
            return self.valid_moves[0]
        else:
            move_index = self.valid_moves.index(self.my_move)
            if move_index == len(self.valid_moves)-1:
                return self.valid_moves[0]
            else:
                return self.valid_moves[move_index+1]


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.game_type = None
        self.valid_game = ['round', 'match']

    def intro(self):
        print_pause(f"Welcome {self.play_name} to The Game")
        self.game_type = self.choose_game()
        while self.game_type not in self.valid_game:
            self.game_type = self.choose_game()
        print_pause(f"you have choosen to play a {self.game_type}")

    def choose_game(self):
        print_pause("\nWould you like to play a")
        try:
            game_type = input("round, match > ").lower()
        except KeyboardInterrupt:
            self.choose_game()

        print_pause(" ")
        return game_type

    def play_round(self):
        self.move1 = self.p1.move()
        self.move2 = self.p2.move()
        print_pause(f"{self.play_name}: {self.move1}  Player 2: {self.move2}")
        self.p1.learn(self.move1, self.move2)
        self.p2.learn(self.move2, self.move1)

    def play_game(self):
        if self.p1.name == "Player 1":
            self.p1.enter_name()
        self.play_name = self.p1.name
        self.intro()
        print_pause("Game start!")
        if self.game_type == "round":
            self.play_round()
            self.keep_score()
        else:
            n = 3  # number of rounds
            for round in range(n):
                print_pause(" ")
                print_pause(f"Round {round+1}: of {n}")
                self.play_round()
                self.keep_score()
        print_pause(f"Score:\n  {self.play_name}: {self.p1.score}\n"
                    f"  Player 2: {self.p2.score}")
        self.final_result = f"Score:  {self.play_name}: {self.p1.score}" +\
                            f"  Player 2: {self.p2.score}"
        self.save_scores()
        print_pause(" ")
        print_pause("Game over!")
        print_pause(" ")
        self.play_again()

    def keep_score(self):
        move1 = self.move1
        move2 = self.move2
        if beats(move1, move2):
            print_pause(f"******Player *{self.play_name}* is the Winner******")
            self.p1.score += 1
        elif move1 == move2:
            print_pause("********************** Draw! **********************")
        else:
            print_pause("*************Player *Two* is the Winner************")
            self.p2.score += 1

    def play_again(self):
        try:
            choice = input("Would you like to play again? (y/n) > ").lower()
        except KeyboardInterrupt:
            self.play_again()

        if choice in ['y', "n", "yes", "no"]:
            if choice in ['y', 'yes']:
                print_pause("Excellent! Restarting the game ...")
                self.play_game()
            elif choice in ['n', 'no']:
                print_pause("Thanks for playing! See you next time.")
        else:
            print_pause("Try again!")
            self.play_again()

    def save_scores(self):
        # to save the score and time in a file called scores.txt
        # if the file note exist it will be created
        dt = datetime.datetime.now()
        with open('scores.txt', 'a') as file:
            file.write(str(self.final_result + " @ " + str(dt) + ".\n"))


if __name__ == '__main__':
    bot = random.choice([RandomPlayer(),
                        ReflectPlayer(),
                        CyclePlayer()])
    game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()
