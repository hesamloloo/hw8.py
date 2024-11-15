class Board:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
    
    def display_board(self):
        print("-------------")
        for i in range(3):
            print(f"| {self.board[i*3]} | {self.board[i*3+1]} | {self.board[i*3+2]} |")
            print("-------------")
    
    def update_board(self, position, player):
        if self.board[position] == ' ':
            self.board[position] = player
            return True
        return False
    
    def check_winner(self, player):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  
            [0, 4, 8], [2, 4, 6]              
        ]
        for condition in win_conditions:
            if self.board[condition[0]] == player and self.board[condition[1]] == player and self.board[condition[2]] == player:
                return True
        return False
    
    def is_full(self):
        return ' ' not in self.board


class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = 'X'
    
    def switch_player(self):
        if self.current_player == 'X':
            self.current_player = 'O'
        else:
            self.current_player = 'X'
    
    def play(self):
        while True:
            self.board.display_board()
            position = int(input(f"Player {self.current_player}, choose a position (1-9): ")) - 1
            if position < 0 or position > 8:
                print("Invalid position! Please choose between 1 and 9.")
                continue
            if not self.board.update_board(position, self.current_player):
                print("This position is already taken! Try again.")
                continue
            
            if self.board.check_winner(self.current_player):
                self.board.display_board()
                print(f"Player {self.current_player} wins!")
                break
            elif self.board.is_full():
                self.board.display_board()
                print("It's a tie!")
                break
            
            self.switch_player()


def main_menu():
    while True:
        print("Welcome to the XO game!")
        print("1. Start Game")
        print("2. Quit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            game = Game()
            game.play()
        elif choice == '2':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice! Please choose 1 or 2.")

main_menu()