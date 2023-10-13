class TicTacToe:
    def __init__(self):
        self.state = [[' ' for _ in range(3)] for _ in range(3)]

    def print_board(self):
        for row in self.state:
            print(" | ".join(row))
            print("-" * 9)

    def make_move(self, row, col, val):
        if self.is_valid_move(row, col) and self.state[row][col] == ' ':
            self.state[row][col] = val
            return True
        return False

    def is_valid_move(self, row, col):
        return 0 <= row < 3 and 0 <= col < 3

    def terminal_node(self):
        for i in range(3):
            if self.state[i][0] == self.state[i][1] == self.state[i][2] != ' ':
                return True, self.state[i][0]
            if self.state[0][i] == self.state[1][i] == self.state[2][i] != ' ':
                return True, self.state[0][i]

        if self.state[0][0] == self.state[1][1] == self.state[2][2] != ' ':
            return True, self.state[0][0]
        if self.state[0][2] == self.state[1][1] == self.state[2][0] != ' ':
            return True, self.state[0][2]

        for i in range(3):
            for j in range(3):
                if self.state[i][j] == ' ':
                    return False, ' '

        return True, 'Tie'

    def get_empty_cells(self):
        empty_cells = []
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == ' ':
                    empty_cells.append((i, j))
        return empty_cells

    def minimax(self, depth, is_maximizing):
        game_over, result = self.terminal_node()
        if game_over:
            if result == 'X':
                return -1
            elif result == 'O':
                return 1
            else:
                return 0

        if is_maximizing:
            max_eval = -float("inf")
            for move in self.get_empty_cells():
                row, col = move
                self.make_move(row, col, 'O')
                eval = self.minimax(depth + 1, False)
                self.state[row][col] = ' '
                max_eval = max(max_eval, eval)
            return max_eval
        else:
            min_eval = float("inf")
            for move in self.get_empty_cells():
                row, col = move
                self.make_move(row, col, 'X')
                eval = self.minimax(depth + 1, True)
                self.state[row][col] = ' '
                min_eval = min(min_eval, eval)
            return min_eval

    def find_best_move(self):
        best_eval = -float("inf")
        best_move = None
        for move in self.get_empty_cells():
            row, col = move
            self.make_move(row, col, 'O')
            eval = self.minimax(0, False)
            self.state[row][col] = ' '
            if eval > best_eval:
                best_eval = eval
                best_move = move
        return best_move


def main():
    game = TicTacToe()

    while True:
        game.print_board()
        row, col = map(int, input("Enter your move (row col): ").split())
        if game.make_move(row, col, 'X'):
            game_over, result = game.terminal_node()
            if game_over:
                game.print_board()
                if result == 'X':
                    print("You win!")
                elif result == 'O':
                    print("Computer wins!")
                else:
                    print("It's a tie!")
                break

            best_move = game.find_best_move()
            game.make_move(best_move[0], best_move[1], 'O')
            game_over, result = game.terminal_node()
            if game_over:
                game.print_board()
                if result == 'X':
                    print("You win!")
                elif result == 'O':
                    print("Computer wins!")
                else:
                    print("It's a tie!")
                break


if __name__ == "__main__":
    main()