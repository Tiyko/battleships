"""Importing random module"""
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

        x_row = input("Enter the row of the ship: \n")
        while x_row not in '12345678':
            print('Not an appropriate choice, please select a valid row')
            x_row = input("Enter the row of the ship: \n")

        y_column = input("Enter the column letter of the ship: \n").upper()
        while y_column not in "ABCDEFGH":
            print(
                "Not an appropriate choice, please select a valid column"
            )
            y_column = input(
                "Enter the column letter of the ship: \n").upper()
        return int(x_row) - 1,\
            GameBoard.get_letters_to_numbers(self)[y_column]

    def count_hit_ships(self):
        """Counts the number of hit ships and marks it on the board"""
        hit_ships = 0
        for row in self.board:
            for column in row:
                if column == "X":
                    hit_ships += 1
        return hit_ships


def run_game():
    """Function that runs the game"""
    print(" ")
    print("This is a battleship game!")
    print("There are 20 ships hidden on a board of 64 slots.")
    print("Select the row number (1 to 8) and the column letter (A to H)")
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
        # get user input
        user_x_row, user_y_column = Battleship.get_user_input(object)
        # check if duplicate guess
        while user_guess_board.board[user_x_row][user_y_column] == "-" or\
                user_guess_board.board[user_x_row][user_y_column] == "X":
            print(" ")
            print("You guessed that one already.")
            user_x_row, user_y_column = Battleship.get_user_input(object)
        # check for hit or miss
        if computer_board.board[user_x_row][user_y_column] == "X":
            print(" ")
            print("You sunk a battleship!")
            user_guess_board.board[user_x_row][user_y_column] = "X"
        else:
            print(" ")
            print("You missed!")
            user_guess_board.board[user_x_row][user_y_column] = "-"
        # check for win or lose
        if Battleship.count_hit_ships(user_guess_board) == 20:
            print(" ")
            print("You sunk all battleships!")
            break
        else:
            bullets -= 1
            print(f"You have {bullets} bullets remaining.")
            if bullets == 0:
                print("Sorry you ran out of bullets.")
                print("Game over!")
                Battleship.count_hit_ships(user_guess_board)
                break


run_game()
