"""Import modules"""
import random


class GameBoard:
    """Gameboard class, builds an 8 by 8 board"""

    def __init__(self, board):
        self.board = board

    def get_letters_to_numbers(self):
        """Sets the X and Y axis"""
        letters_to_numbers = {"A": 0, "B": 1, "C": 2,
                              "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
        return letters_to_numbers

    def print_board(self):
        """Prints the board"""
        print("  ")
        print("  A B C D E F G H")

        row_number = 1
        for row in self.board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1


class Battleship:
    """Class that builds and randomizes the battleships on the board"""

    def __init__(self, board):
        self.board = board
        self.x_row = 0
        self.y_column = 0

    def create_ships(self):
        """Ramdomizes the ships on the board"""
        for _ in range(20):
            self.x_row, self.y_column = random.randint(
                0, 7), random.randint(0, 7)
            while self.board[self.x_row][self.y_column] == "X":
                self.x_row, self.y_column = random.randint(
                    0, 7), random.randint(0, 7)
            self.board[self.x_row][self.y_column] = "X"
        return self.board

    def get_user_input(self):
        """Gets the user input and prints the result"""

    def count_hit_ships(self):
        """Counts the number of ships and marks it on the board"""


def run_game():
    """Function that runs the game"""
    print(" ")
    print("This is a battleship game!")
    print("There are 20 ships hidden on a board of 64 slots.")
    print("You have 20 bullets. How many ships can you bring down?")
    print(" ")
    computer_board = GameBoard([[" "] * 8 for i in range(8)])
    user_guess_board = GameBoard([[" "] * 8 for i in range(8)])
    Battleship.create_ships(computer_board)

    # start 20 turns
    bullets = 20
    print(bullets, "bullets.")
    while bullets > 0:
        GameBoard.print_board(user_guess_board)


run_game()
