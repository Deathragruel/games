class TicTacToe():
    """ Implementation of a two-player tic-tac-toe game. """
    def __init__(self):
        """ We will make the board using a dictionary in which each value will be an
        empty space and each key will represent that empty space's location. The values
        will be replaced upon input. """
        self.the_board = {'7': ' ', '8': ' ', '9': ' ',
                          '4': ' ', '5': ' ', '6': ' ',
                          '1': ' ', '2': ' ', '3': ' '}
        self.board_keys = []
        self.game_active = True


    def run_game(self):
        self._assign_keys()
        the_board = self.the_board
        turn = 'X'
        self.turn = turn
        count = 0
        first_time = True

        while self.game_active:
            if first_time:
                print("The keypad on the right side of your keyboard represents the "
                        "movement places. Like this:"
                        "\n7|8|9"
                        "\n-+-+-"
                        "\n4|5|6"
                        "\n-+-+-"
                        "\n1|2|3")
                first_time = False
            print("\nIt's your turn, " + turn + ". Move to which place?")
            self._print_board(the_board)
        
            move = input()
        
            try:
                if the_board[move] == ' ':
                    the_board[move] = turn
                    count += 1
                else:
                    print("That place is already filled. \nMove to which place?")
                    continue
            
            except KeyError:
                print("What you typed is not a movement option.")
                continue
            
            else:
                # Now we will check if player X or O has won, for every move after 5
                # moves.
                if count >= 5:
                    self._check_which_player_won()

                # If neither X or O wins and the board is full, we'll declare the
                # result as 'tie'
                if count == 9:
                    print("\nGame Over.\n")
                    print("It's a Tie!!")
                    self.game_active = False

                # Now we have to change the player after every move.
                if turn == 'X':
                    turn = 'O'
                else:
                    turn = 'X'
        self._restart()


    def _check_which_player_won(self):
       
       the_board = self.the_board
       turn = self.turn
       
       if the_board['7'] == the_board['8'] == the_board['9'] != ' ':
           # across the top
           self._print_board(the_board)
           print("\nGame Over.\n")
           print(" **** " + turn + " won. ****")
           self.game_active = False
       
       elif the_board['4'] == the_board['5'] == the_board['6'] != ' ':
           # across the middle
           self._print_board(the_board)
           print("\nGame Over.\n")
           print(" **** " + turn + " won. ****")
           self.game_active = False
       
       elif the_board['1'] == the_board['2'] == the_board['3'] != ' ':
           # across the bottom
           self._print_board(the_board)
           print("\nGame Over.\n")
           print(" **** " + turn + " won. ****")
           self.game_active = False
       
       elif the_board['1'] == the_board['4'] == the_board['7'] != ' ':
           # down the left side
           self._print_board(the_board)
           print("\nGame Over.\n")
           print(" **** " + turn + " won. ****")
           self.game_active = False
       
       elif the_board['2'] == the_board['5'] == the_board['8'] != ' ':
           # down the middle
           self._print_board(the_board)
           print("\nGame Over.\n")
           print(" **** " + turn + " won. ****")
           self.game_active = False
       
       elif the_board['3'] == the_board['6'] == the_board['9'] != ' ':
           # down the right side
           self._print_board(the_board)
           print("\nGame Over.\n")
           print(" **** " + turn + " won. ****")
           self.game_active = False
       
       elif the_board['7'] == the_board['5'] == the_board['3'] != ' ':
           # diagonal
           self._print_board(the_board)
           print("\nGame Over.\n")
           print(" **** " + turn + " won. ****")
           self.game_active = False
       
       elif the_board['1'] == the_board['5'] == the_board['9'] != ' ':
           # diagonal
           self._print_board(the_board)
           print("\nGame Over.\n")
           print(" **** " + turn + " won. ****")
           self.game_active = False
        

    def _assign_keys(self):
        self_board_keys = self.board_keys
        for key in self.the_board:
            self_board_keys.append(key)


    def _print_board(self, board):
        """ We have to update the board each time a move is played so we will make a
        function which will print the updated board each time it is called. """
        print(board['7'] + '|' + board['8'] + '|' + board['9'])
        print('-+-+-')
        print(board['4'] + '|' + board['5'] + '|' + board['6'])
        print('-+-+-')
        print(board['1'] + '|' + board['2'] + '|' + board['3'])


    def _restart(self): 
        # Now we will ask if player wants to restart the game or not.
        restart = input("Do you want to play again? (y/n)")
        if restart == "y" or restart == "Y":
            for key in self.board_keys:
                self.the_board[key] = " "

            self.run_game()


if __name__ == '__main__':
    ttt = TicTacToe()
    ttt.run_game()
