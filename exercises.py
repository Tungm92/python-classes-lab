class Game():
    def __init__(self, turn='X', tie=False, winner=None):
        self.turn = turn
        self.tie = tie
        self.winner = winner
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None
        }

    def play_game(self):
            print("~Welcome to Mai Tic-Tac-Toe~")
            while not self.winner and not self.tie:
                self.render()
            self.print_board()
            self.print_message()
    
    def print_board(self):
        b = self.board
        print(f'''
               A   B   C
            1) {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
               ----------
            2) {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
               ----------
            3) {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        ''')

    def print_message(self):
        if self.tie:
            print('Tie game!')
        elif self.winner:
            print(f'{self.winner} wins the game!')
        else:
            print(f"It's player {self.turn}'s turn!")

    def get_move(self):
        b = self.board
        while True:
            move = input(f"Enter a valid move (example: A1): ").lower()
            if (move == 'a1' or move == 'a2' or move == 'a3' or move == 'b1' or move == 'b2' or move == 'b3' or move == 'c1' or move == 'c2' or move =='c3') and self.board[move] == None:
                b[move] = self.turn
                return
            else:
                print('Invalid move, please try again.')
    
    def check_for_winner(self):
        
        combos = (
            self.board['a1'] and (self.board['a1'] == self.board['b1'] == self.board['c1']),
            self.board['a2'] and (self.board['a2'] == self.board['b2'] == self.board['c2']),
            self.board['a3'] and (self.board['a3'] == self.board['b3'] == self.board['c3']),
            self.board['a1'] and (self.board['a1'] == self.board['a2'] == self.board['a3']),
            self.board['b1'] and (self.board['b1'] == self.board['b2'] == self.board['b3']),
            self.board['c1'] and (self.board['c1'] == self.board['c2'] == self.board['c3']),
            self.board['a1'] and (self.board['a1'] == self.board['b2'] == self.board['c3']),
            self.board['a3'] and (self.board['a3'] == self.board['b2'] == self.board['c1']),
        )

        for combo in combos:
            if combo:
                self.winner = self.turn
                break
    
    def check_for_tie(self):
        b = self.board
        self.tie = True
        for square in b:
            if not b[square]:
                self.tie = False
                break              

    def switch_turn(self):
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'

    def render(self):
        self.print_board()
        self.print_message()
        self.get_move()
        self.check_for_winner()
        self.check_for_tie()
        self.switch_turn()

game_instance = Game()
game_instance.play_game()