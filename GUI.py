import pygame
from H_D_values import *
from Logic import GameLogic

import os


"""Initialize Pygame"""
pygame.init()
pygame.font.init()
font = pygame.font.SysFont(None, 55)

"""ADD FONT"""

"""Gets the size of the screen"""
# info = pygame.display.Info()
# screen_width = info.current_w
# screen_height = info.current_h
screen_width = 800
screen_height = 600


# Load the background image
background_image = pygame.image.load('wallpaperflare.com_wallpaper.jpg')  # Make sure to replace 'background.jpg' with the path to your image
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))


"""Create the screen"""
screen = pygame.display.set_mode((screen_width, screen_height))
# screen = pygame.display.set_mode((initial_width, initial_height), pygame.RESIZABLE)
pygame.display.set_caption('Tic Tac Toe') # Title



"""Color"""
background = GRAY
screen.fill(background)
pygame.display.update()

"""Initialize game logic"""
game_logic = GameLogic(RED, screen) # calls the game logic class and creates an 'Object'



def display_scores():
    
    """
        Displays the scores of the player and the AI on the screen.
        This function initializes the Pygame font, sets the font size to 40, and creates text surfaces for the player's score and the AI's score. The text surfaces are then blitted onto the screen at the specified coordinates.
        Parameters:
            None
        Returns:
            None
    """
    pygame.font.init()
    font = pygame.font.SysFont(None, 40)
    x_score_text = font.render(f'Player : X ', True, Maroon)
    o_score_text = font.render(f'AI : O ', True, Maroon)
    screen.blit(x_score_text, (10, 10))
    screen.blit(o_score_text, (10, 70))

def update_title():
    """
        Updates the title of the Pygame window to display the current scores of the players in a Tic Tac Toe game.
        This function uses f-strings to format the title string with the current scores of the players. The scores are obtained from the `player_x_score` and `player_o_score` variables.
        Parameters:
            None
        Returns:
            None
    """
    pygame.display.set_caption(f'Tic Tac Toe - Player X: {player_x_score} | AI O : {player_o_score}')





def draw_buttons(screen_width, screen_height):
   
    """
        Draws buttons on the screen with the specified dimensions and text. It initializes the necessary fonts and button properties,
        creates button rectangles, draws the buttons,
        and blits the text onto the buttons. Returns the rectangle objects for the reset and continue buttons.
    """
    pygame.font.init()
    font = pygame.font.SysFont(None, 30)
    button_width = 100
    button_height = 30
    button_margin = 10

    reset_button = pygame.Rect(screen_width - button_width - 10, screen_height - 2 * button_height - button_margin - 10, button_width, button_height)
    continue_button = pygame.Rect(screen_width - button_width - 10, screen_height - button_height - 10, button_width, button_height)
    
    pygame.draw.rect(screen, Navy, reset_button)
    pygame.draw.rect(screen, Navy, continue_button)
    
    font = pygame.font.SysFont(None, 26)
    reset_text = font.render('Reset', True, WHITE)
    continue_text = font.render('Continue', True, WHITE)
    
    screen.blit(reset_text, (reset_button.x + 30, reset_button.y + 5))
    screen.blit(continue_text, (continue_button.x + 15, continue_button.y + 5))
    
    return reset_button, continue_button

def reset_game():
    
    """
        Reset the game by resetting the game board and updating the title of the Pygame window.

        This function calls the `reset_board` method of the `game_logic` object to reset the game board to its initial state. It then calls the `update_title` function to update the title of the Pygame window with the current scores of the players.

        Parameters:
            None

        Returns:
            None
    """
    game_logic.reset_board()
    update_title()
    
    
    

def show_message(message, duration=500):
    """
    Display a message on the screen for a specified duration.

    Args:
        message (str): The message to be displayed.
        duration (int, optional): The duration in milliseconds for which the message should be displayed. Defaults to 500.

    Returns:
        None

    This function creates an overlay surface with transparency and fills it with a black background. It then renders the message using a font and centers it on the screen. The overlay and the message are blitted onto the screen using the `blit` function. Finally, the `update` function is called to update the display and `time.delay` is used to pause the execution for the specified duration.
    """
    
    
    
    overlay = pygame.Surface((screen.get_width(), screen.get_height()))
    overlay.set_alpha(128)  # Transparency
    overlay.fill((0, 0, 0))  # Black background
    screen.blit(overlay, (0, 0))
    
    message_font = pygame.font.SysFont(None, 75)
    message_text = message_font.render(message, True, WHITE)
    text_rect = message_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    screen.blit(message_text, text_rect)
    
    pygame.display.update()
    pygame.time.delay(duration)



"""
This code snippet implements a simple game loop using Pygame for a Tic-Tac-Toe game.

1. It initializes the game state and necessary variables.
2. Enters a game loop where it continuously updates the screen with game elements.
3. Handles user input events such as mouse clicks for game interactions.
4. Manages game logic, player moves, checking for a winner, and updating scores.
5. Resizes the game window if a resize event occurs.
6. Finally, it quits Pygame when the game loop ends.

Note: This docstring provides an overview of the functionality of the code snippet.
"""
running = True
reset_game()


while running:
    
    
    screen.blit(background_image, (0, 0))  # Draw the background image
    game_logic.draw_board(screen.get_width(), screen.get_height())
    display_scores()
    reset_button, continue_button = draw_buttons(screen.get_width(), screen.get_height())
    pygame.display.update()
    
    
    for event in pygame.event.get():
        
        
        if event.type == pygame.QUIT:
            
            
            running = False
            
            
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            
            
            x, y = event.pos
            
            
            if reset_button.collidepoint(x, y):
                
                
                player_x_score = 0
                player_o_score = 0
                reset_game()
                
                
            elif continue_button.collidepoint(x, y):
                game_logic.reset_board()
                
                
            else:
                
                
                if game_logic.player_move(x, y):
                    
                    
                    screen.blit(background_image, (0, 0))  # Draw the background image
                    game_logic.draw_board(screen.get_width(), screen.get_height())
                    display_scores()
                    reset_button, continue_button = draw_buttons(screen.get_width(), screen.get_height())
                    pygame.display.update()
                    winner = game_logic.check_winner()
                    
                    
                    if winner == 'X':
                        
                        
                        player_x_score += 1
                        pygame.display.update()
                        show_message("Congrats!", 500)  # Show message for 0.5 seconds
                        pygame.time.wait(1000)  # Wait for 2 seconds
                        reset_game()
                        
                        
                    elif winner == None:
                        
                        
                        if game_logic.random_ai_move():
                            
                            
                            screen.blit(background_image, (0, 0))  # Draw the background image
                            game_logic.draw_board(screen.get_width(), screen.get_height())
                            display_scores()
                            reset_button, continue_button = draw_buttons(screen.get_width(), screen.get_height())
                            pygame.display.update()
                            winner = game_logic.check_winner()
                            
                            
                            if winner == 'O':
                                
                                
                                player_o_score += 1
                                pygame.display.update()
                                show_message("You lost!", 500)  # Show message for 0.5 seconds
                                pygame.time.wait(1000)  # Wait for 2 seconds
                                reset_game()
                                
                                
        elif event.type == pygame.VIDEORESIZE:
            
            
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            background_image = pygame.transform.scale(background_image, (event.w, event.h))  # Rescale the background image
            
            
            
            
            
            
            
            
            

"""Quit Pygame"""
pygame.quit()




