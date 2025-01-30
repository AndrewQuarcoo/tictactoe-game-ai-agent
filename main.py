import pygame
import sys
import os
from environment import TicTacToeEnvironment
from agent import TicTacToeAgent

def show_start_popup():
    # Create a popup for starting the game
    popup = pygame.Surface((300, 200))
    popup.fill((255, 255, 255))
    font = pygame.font.Font(None, 36)
    text = font.render("Start", True, (255, 0, 0))
    button_rect = pygame.Rect(100, 80, 100, 40)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    return  # Start the game

        popup.blit(text, (120, 90))
        pygame.draw.rect(popup, (255, 0, 0), button_rect)
        screen.blit(popup, (screen.get_width() // 2 - 150, screen.get_height() // 2 - 100))
        pygame.display.flip()

def main():
    global screen
    pygame.init()
    screen = pygame.display.set_mode((300, 300))
    pygame.display.set_caption("Tic Tac Toe")
    env = TicTacToeEnvironment()
    agent = TicTacToeAgent()

    show_start_popup()  # Show the start popup

    while True:
        timer_event = pygame.USEREVENT + 1
        pygame.time.set_timer(timer_event, 1000)  # Set timer to 1 second
        timer_count = 10  # 10 seconds countdown

        while timer_count > 0:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == timer_event:
                    timer_count -= 1

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    env.handle_click(pos)
                    if env.current_player == 'X':
                        move = agent.get_best_move(env.board)
                        env.board[move[0]][move[1]] = agent.symbol
                        env.current_player = 'X'  # Switch back to player

            # Draw the timer
            font = pygame.font.Font(None, 36)
            timer_text = font.render(f"Time: {timer_count}", True, (255, 255, 255))
            screen.fill((30, 30, 30))  # Clear the screen
            screen.blit(timer_text, (220, 10))  # Display timer at top right
            env.draw_board()  # Draw the board
            pygame.display.flip()

        # Agent's turn after timer
        move = agent.get_best_move(env.board)
        env.board[move[0]][move[1]] = agent.symbol
        env.current_player = 'X'  # Switch back to player

        # Check for game over
        if env.check_winner(agent.symbol):
            show_game_over_popup("User Lost! Click to Restart")
            break

def show_game_over_popup(message):
    popup = pygame.Surface((300, 200))
    popup.fill((255, 255, 255))
    font = pygame.font.Font(None, 36)
    text = font.render(message, True, (255, 0, 0))
    button_rect = pygame.Rect(100, 80, 100, 40)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    main()  # Restart the game

        popup.blit(text, (50, 30))
        pygame.draw.rect(popup, (255, 0, 0), button_rect)
        screen.blit(popup, (screen.get_width() // 2 - 150, screen.get_height() // 2 - 100))
        pygame.display.flip()

if __name__ == "__main__":
    main()
