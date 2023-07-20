class GameBoard:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)] # 3x3 board

    def set_items(self, user, position): # position is 1-9
        row, col = divmod(position - 1, 3) # gets the row and column
        if self.board[row][col] == ' ':
            self.board[row][col] = user
            return True
        return False
    @property
    def game_board(self): # returns the board
        return self.board

    def clear_board(self): # clears the board
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        return self.board

    def is_board_full(self): # checks if the board is full
        for row in self.board: # checks if there are any empty spaces
            for item in row: # if there are, returns false
                if item == ' ': # if there are no empty spaces, returns true
                    return False
        return True

    def is_game_won(self): # checks if the game is won
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False

    def print_board(self): # prints the board
        print('---------')
        for row in self.board:
            print('|', *row, '|')
        print('---------')


class Game: # controls the game

    def game_start(self): # starts the game
        self.controlBoard = GameBoard()
        self.game_board = self.controlBoard.game_board
        self.playerone = 'X'
        self.playertwo = 'O'
        print("Welcome to Tic Tac Toe!")
        self.player_one = input("Enter the name of Player 1: ")
        self.player_two = input("Enter the name of Player 2: ")
        print("Here is your game board:")
        self.controlBoard.print_board()
        self.turn = 1
        self.take_turn()

    def game_end(self): # ends the game
        if self.game_running == False:
            replay = input("Press 0 to quit or 1 to play again: ")
            try:
                if int(replay) == 0:
                    print("Thanks for playing!")
                    return False
                elif int(replay) == 1:
                    self.game_running = True
                    self.controlBoard.clear_board()
                    self.game_start()
                else:
                    raise ValueError
            except ValueError:
                print("Please enter a valid number.")
                self.game_end()

    def take_turn(self): # takes a turn
        print("Pick a number between 1-9 to place your mark.")
        try:
            position = int(input()) # gets the position
            if position < 1 or position > 9:
                raise ValueError

            if self.controlBoard.set_items(self.playerone if self.turn % 2 == 0 else self.playertwo, position): # sets the item
                self.controlBoard.print_board() # prints the board
                self.turn += 1
                if self.controlBoard.is_game_won():
                    print(f"{self.player_one if self.turn % 2 == 0 else self.player_two} wins!") # checks if the game is won
                    self.game_running = False
                    self.game_end()
                elif self.controlBoard.is_board_full():
                    print("It's a tie!")
                    self.game_running = False
                    self.game_end()
                else:
                    self.take_turn()
            else:
                print("That spot is taken!")
                self.take_turn()

        except ValueError:
            print("Please enter a valid number.")
            self.take_turn()

    def main(self):
        self.game_running = True
        self.game_start()




if __name__ == '__main__':
    game = Game()
    game.main()
