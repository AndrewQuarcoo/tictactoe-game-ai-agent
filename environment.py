import pygame
import sys

class TicTacToeEnvironment:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((300, 300))
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'  # Assuming 'X' is the human player

    def draw_board(self):
        # Draw the game board with a modern look
        self.screen.fill((30, 30, 30))  # Dark background for a modern feel
        for row in range(3):
            for col in range(3):
                # Draw grid lines
                pygame.draw.rect(self.screen, (50, 50, 50), (col * 100, row * 100, 100, 100), 5)

                if self.board[row][col] == 'X':
                    # Draw 'X' with a funky color and font
                    font = pygame.font.Font(None, 100)  # Use a larger font size
                    text = font.render('X', True, (255, 0, 0))  # Red color for 'X'
                    self.screen.blit(text, (col * 100 + 25, row * 100 + 10))  # Center the text
                elif self.board[row][col] == 'O':
                    # Draw 'O' with a funky color and font
                    font = pygame.font.Font(None, 100)  # Use a larger font size
                    text = font.render('O', True, (0, 0, 255))  # Blue color for 'O'
                    self.screen.blit(text, (col * 100 + 25, row * 100 + 10))  # Center the text

        pygame.display.flip()  # Update the display

    def handle_click(self, pos):
        # Handle player clicks
        x, y = pos
        row = y // 100
        col = x // 100
        if self.board[row][col] == '':
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'  # Switch player

    def reset_game(self):
        # Reset the game state
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'  # Reset to the starting player
        self.draw_board()  # Redraw the board

    def check_winner(self, symbol):
        # Check rows for a win
        for row in range(3):
            if all(cell == symbol for cell in self.board[row]):
                return True
        # Check columns for a win
        for col in range(3):
            if all(self.board[row][col] == symbol for row in range(3)):
                return True
        # Check diagonals for a win
        if all(self.board[i][i] == symbol for i in range(3)) or all(self.board[i][2 - i] == symbol for i in range(3)):
            return True
        return False
