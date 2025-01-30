class TicTacToeAgent:
    def __init__(self):
        self.symbol = 'O'  # Assuming 'O' is the agent's symbol

    def get_best_move(self, board):
        # Use Minimax algorithm to find the best move
        best_score = float('-inf')
        best_move = None

        for row in range(3):
            for col in range(3):
                if board[row][col] == '':
                    board[row][col] = self.symbol  # Make the move
                    score = self.minimax(board, False)  # Get the score for this move
                    board[row][col] = ''  # Undo the move

                    if score > best_score:
                        best_score = score
                        best_move = (row, col)

        # Check if a best move was found
        if best_move is None:
            return self.random_move(board)  # Return a random move if no best move is found

        return best_move

    def minimax(self, board, is_maximizing):
        # Check for terminal states
        if self.check_winner(board, self.symbol):
            return 1  # Agent wins
        elif self.check_winner(board, 'X'):
            return -1  # User wins
        elif all(cell != '' for row in board for cell in row):
            return 0  # Draw

        if is_maximizing:
            best_score = float('-inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] == '':
                        board[row][col] = self.symbol
                        score = self.minimax(board, False)
                        board[row][col] = ''
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] == '':
                        board[row][col] = 'X'
                        score = self.minimax(board, True)
                        board[row][col] = ''
                        best_score = min(score, best_score)
            return best_score

    def check_winner(self, board, symbol):
        # Check rows, columns, and diagonals for a win
        for row in range(3):
            if all(cell == symbol for cell in board[row]):
                return True
        for col in range(3):
            if all(board[row][col] == symbol for row in range(3)):
                return True
        if all(board[i][i] == symbol for i in range(3)) or all(board[i][2 - i] == symbol for i in range(3)):
            return True
        return False

    def random_move(self, board):
        # Return a random valid move
        import random
        valid_moves = [(i, j) for i in range(3) for j in range(3) if board[i][j] == '']
        return random.choice(valid_moves) if valid_moves else None