from time import sleep
class TicTacToe:
    def __init__(self):
        self.board = "_________"
        self.state = True
        self.symbol = "X"
        self.move = [0,0]
        self.pos = -1
    
    def loading_screen(self):
        print('''
         _           _            _             
        | | (_)    | |           | |            
        | |_ _  ___| |_ __ _  ___| |_ ___   ___ 
        | __| |/ __| __/ _` |/ __| __/ _ \ / _ \\
        | |_| | (__| || (_| | (__| || (_) |  __/
        \__|_|\___|\__\__,_|\___|\__\___/ \___|        
            
        ''')

    def start_game(self):
        print('-' * 9) # print dashed lines
        
        for i in range(3):
            print('|', " ".join(" "*3),'|')
            if i != 2:
                print()        
        print('-' * 9) # print dashed lines

    def create_board(self):
        print('-' * 9) # print dashed lines
        
        for i in range(3):
            # instead of printing underscores, print spaces
            board_copy = self.board
            board_copy = board_copy.replace("_", " ")

            print('|', " ".join(board_copy[i*3:(i+1)*3]),'|')
            if i != 2:
                print()  
                
        print('-' * 9) # print dashed lines

    def winner(self, val:str)->int:
        status = 0 # lose
        lst_val = (val * 3)
     
        row_check = (self.board[:3] == lst_val) or (self.board[3:6] == lst_val) or (self.board[6:] == lst_val)
        col_check = (self.board[:7:3] == lst_val) or (self.board[1:8:3] == lst_val) or (self.board[2::3] == lst_val)
        diag_check = (self.board[::4] == lst_val) or (self.board[2:7:2] == lst_val)
        
        if row_check or col_check or diag_check:
            status = 1 # wins

        return status

    def game_state(self)->tuple:
        result = (0, "Game not finished") # default

        # conditions for impossible board analyzed
        impossible = abs(self.board.count("X") - self.board.count("O")) >= 2 or (self.winner("X")) == 1
        impossible1 = self.winner("O") == 1
        impossible = impossible and impossible1

        if ("_" not in self.board) and (self.winner("X") == 0 and self.winner("O") == 0):
            result = (1, "Draw")
        elif self.winner("X") == 1:
            result = (1, "X wins")
        elif self.winner("O") == 1:
            result = (1, "O wins")
        elif impossible:
            result = (-1, "Impossible")

        return result
    
    def get_coord(self)->int:
        # This math is based on zero-indexing. Converting the tuple to a zero index that can be used directly on the board
        if self.move[0] == 1:
            self.pos = self.move[1] - self.move[0]
        elif self.move[0] == 2:
            self.pos = self.move[1] + self.move[0]
        else:
            self.pos = 2 + (self.move[1] + self.move[0])

        return self.pos

    def user_move(self):
        state = True
        
        while state:
            self.move = input("Enter your desired position: ").split()
            
            # analyzing first possible error
            try:
                int(self.move[0])
                int(self.move[1])
            except ValueError:
                print("You should enter numbers!")
            except IndexError:
                print("You should enter two numbers!")
            else: 
                valid_nums = [1,2,3]
                # analyzing second possible error
                result = all(int(elem) in valid_nums for elem in self.move) 

                if not result:
                    print("Coordinates should be from 1 to 3!")
                else:
                    self.move = [int(val) for val in self.move]
                    self.pos = self.get_coord()

                    # third possible error
                    if self.board[self.pos] != '_':
                        print("This cell is occupied! Choose another one!")
                    else:
                        self.board = self.board[:self.pos] + self.symbol + self.board[self.pos+1:] # update board
                        self.symbol = "O" if self.symbol == "X" else "X" # update symbol
                        state = False # terminate loop


def main():
    game = TicTacToe()
    game.loading_screen()
    print("Welcome to Tic-Tac-Toe v1.5.0")
    print()
    print('Loading an empty board...')
    sleep(2)
    game.start_game()
    sleep(1)
    state = True


    while(state):
        game.user_move()
        print()
        game.create_board()

        # check game state
        (status, msg) = game.game_state()

        if status != 0 and status != -1:
            print(msg)
            state = False


if __name__ == "__main__":
    main()

            
