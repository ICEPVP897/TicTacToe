
# Tic-Tac-Toe GUI and Game Initialization Documentation

This document provides detailed documentation for the GUI and initialization script of the Tic-Tac-Toe game. The script sets up the game environment, handles user interactions, and manages the game loop using the Pygame library.

## Overview

The script initializes the Pygame environment, sets up the game screen, loads assets, and manages the game loop. It also defines several functions for drawing the game elements, handling user input, and updating the game state.

### Initialization

#### Pygame Initialization

The script starts by importing necessary modules and initializing Pygame:

```python

import pygame
from H_D_values import *
from Logic import GameLogic
import os
```

Pygame is initialized with the following commands:

```python


pygame.init()
pygame.font.init()
font = pygame.font.SysFont(None, 55)
```

#### Screen Setup

The script sets the screen dimensions and loads a background image:

```python

screen_width = 800
screen_height = 600
background_image = pygame.image.load('wallpaperflare.com_wallpaper.jpg')
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tic Tac Toe')
```

The screen is filled with a background color and updated:

```python

background = GRAY
screen.fill(background)
pygame.display.update()
```

#### Game Logic Initialization

The game logic is initialized by creating an instance of the `GameLogic` class:

```python

game_logic = GameLogic(RED, screen)
```

### Functions

#### `display_scores()`

This function displays the scores of the player and the AI on the screen:

```python

def display_scores():
    pygame.font.init()
    font = pygame.font.SysFont(None, 40)
    x_score_text = font.render(f'Player : X ', True, Maroon)
    o_score_text = font.render(f'AI : O ', True, Maroon)
    screen.blit(x_score_text, (10, 10))
    screen.blit(o_score_text, (10, 70))
```

#### `update_title()`

This function updates the title of the Pygame window to display the current scores of the players:

```python

def update_title():
    pygame.display.set_caption(f'Tic Tac Toe - Player X: {player_x_score} | Player O: {player_o_score}')
```

#### `draw_buttons(screen_width, screen_height)`

This function draws buttons on the screen:

```python

def draw_buttons(screen_width, screen_height):
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
```

#### `reset_game()`

This function resets the game board and updates the title of the Pygame window:

```python

def reset_game():
    game_logic.reset_board()
    update_title()
```

#### `show_message(message, duration=500)`

This function displays a message on the screen for a specified duration:

```python

def show_message(message, duration=500):
    overlay = pygame.Surface((screen.get_width(), screen.get_height()))
    overlay.set_alpha(128)
    overlay.fill((0, 0, 0))
    screen.blit(overlay, (0, 0))
    
    message_font = pygame.font.SysFont(None, 75)
    message_text = message_font.render(message, True, WHITE)
    text_rect = message_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    screen.blit(message_text, text_rect)
    
    pygame.display.update()
    pygame.time.delay(duration)
```

### Main Game Loop

The main game loop handles user input and updates the game state:

```python

running = True
reset_game()

while running:
    screen.blit(background_image, (0, 0))
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
                    screen.blit(background_image, (0, 0))
                    game_logic.draw_board(screen.get_width(), screen.get_height())
                    display_scores()
                    reset_button, continue_button = draw_buttons(screen.get_width(), screen.get_height())
                    pygame.display.update()
                    winner = game_logic.check_winner()
                    if winner == 'X':
                        player_x_score += 1
                        pygame.display.update()
                        show_message("Congrats!", 500)
                        pygame.time.wait(1000)
                        reset_game()
                    elif winner == None:
                        if game_logic.random_ai_move():
                            screen.blit(background_image, (0, 0))
                            game_logic.draw_board(screen.get_width(), screen.get_height())
                            display_scores()
                            reset_button, continue_button = draw_buttons(screen.get_width(), screen.get_height())
                            pygame.display.update()
                            winner = game_logic.check_winner()
                            if winner == 'O':
                                player_o_score += 1
                                pygame.display.update()
                                show_message("You lost!", 500)
                                pygame.time.wait(1000)
                                reset_game()
        elif event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            background_image = pygame.transform.scale(background_image, (event.w, event.h))

pygame.quit()
```

### Conclusion

This script sets up and manages the Tic-Tac-Toe game using Pygame. It initializes the game environment, handles user input, and updates the game state through a continuous game loop. Functions are defined to handle drawing the game elements, updating the title, resetting the game, and displaying messages. The main game loop ensures the game runs smoothly, responding to user interactions and updating the display accordingly.


# Tic-Tac-Toe Game Logic Documentation

This document provides an in-depth explanation of the `GameLogic` class implemented in Python using the Pygame library. The `GameLogic` class encapsulates all the functionality required for a simple Tic-Tac-Toe game, including drawing the game board, handling player and AI moves, checking for a winner, and resetting the board.

## Overview

The `GameLogic` class represents the core logic for a Tic-Tac-Toe game. It manages the game board, handles player inputs, and updates the game state. The main components of the class are as follows:

- **Attributes**: Store the game state and configuration.
- **Methods**: Implement the functionality for drawing the game board, making moves, checking for a winner, and resetting the game.

### Class Initialization

#### `__init__(self, LINE_COLOR, screen)`

The constructor initializes the game logic with the following attributes:

- **LINE_COLOR**: A tuple representing the color of the lines on the game board.
- **screen**: The Pygame surface where the game is rendered.
- **board**: A list representing the 3x3 game board, initially filled with empty spaces.
- **player**: The current player, either 'X' or 'O'. The game starts with player 'X'.
- **color_X**: The color of the 'X' symbol, imported from `H_D_values`.
- **color_O**: The color of the 'O' symbol, also imported from `H_D_values`.

### Methods

#### `draw_board(self, screen_width, screen_height)`

This method draws the Tic-Tac-Toe game board on the screen. It calculates the dimensions of each cell and iterates over the board to draw 'X' and 'O' symbols based on the current state.

- **screen_width**: The width of the game screen.
- **screen_height**: The height of the game screen.

The method divides the screen into a 3x3 grid, leaving a border of 120 pixels. It then draws horizontal and vertical lines to create the grid and calls `draw_x` or `draw_o` to render symbols in the occupied cells.

#### `draw_x(self, x, y, width, height)`

This method draws an 'X' symbol at a specified position on the game board.

- **x**: The x-coordinate of the top-left corner of the cell.
- **y**: The y-coordinate of the top-left corner of the cell.
- **width**: The width of the cell.
- **height**: The height of the cell.

The method uses Pygame's `draw.line` function to create two intersecting lines, forming an 'X'.

#### `draw_o(self, x, y, width, height)`

This method draws an 'O' symbol at a specified position on the game board.

- **x**: The x-coordinate of the top-left corner of the cell.
- **y**: The y-coordinate of the top-left corner of the cell.
- **width**: The width of the cell.
- **height**: The height of the cell.

The method uses Pygame's `draw.ellipse` function to create a circle, forming an 'O'.

#### `player_move(self, x, y)`

This method processes a player's move based on screen coordinates.

- **x**: The x-coordinate of the click.
- **y**: The y-coordinate of the click.

The method calculates the corresponding cell on the board from the screen coordinates. If the cell is empty, it places an 'X' in that cell and returns `True`. Otherwise, it returns `False`.

#### `random_ai_move(self)`

This method makes a random move for the AI player.

The method finds all empty cells on the board, chooses one randomly, and places an 'O' in that cell. It returns `True` if a move is made and `False` otherwise.

#### `check_winner(self)`

This method checks if there is a winner on the current board.

The method iterates over all possible winning combinations (horizontal, vertical, and diagonal) and returns the winning symbol ('X' or 'O') if a combination is met. If there is no winner, it returns `None`.

#### `reset_board(self)`

This method resets the game board to its initial state.

The method replaces all elements in the `board` list with empty spaces, effectively resetting the game.

## Conclusion

The `GameLogic` class encapsulates the essential functions needed to run a Tic-Tac-Toe game. It manages the game state, handles player and AI moves, checks for winners, and updates the visual representation of the game board. By using the Pygame library, it provides an interactive and graphical interface for the game.

# Hardcoded Values Documentation

This document provides detailed documentation for the `H_D_values` module, which contains various hardcoded color values and global variables used throughout the Tic-Tac-Toe game.

## Overview

The `H_D_values` module defines color constants and variables that are used in the game for various purposes such as setting the color of game elements and keeping track of player scores.

### Color Constants

The following color constants are defined as RGB tuples. These colors are used to style different elements of the game interface.

#### BLACK

```python

BLACK = (0, 0, 0)
```

- **Description**: Represents the color black.
- **Usage**: Typically used for text and dark elements.

#### GRAY

```python

GRAY = (127, 127, 127)
```

- **Description**: Represents the color gray.
- **Usage**: Used for backgrounds and neutral elements.

#### WHITE

```python

WHITE = (255, 255, 255)
```

- **Description**: Represents the color white.
- **Usage**: Commonly used for text and bright elements.

#### RED

```python

RED = (255, 0, 0)
```

- **Description**: Represents the color red.
- **Usage**: Used for highlighting important elements, such as the game grid lines.

#### GREEN

```python

GREEN = (0, 255, 0)
```

- **Description**: Represents the color green.
- **Usage**: Can be used for indicating success or valid actions.

#### BLUE

```python

BLUE = (0, 0, 255)
```

- **Description**: Represents the color blue.
- **Usage**: Used for drawing 'X' symbols on the game board.

#### YELLOW

```python

YELLOW = (255, 255, 0)
```

- **Description**: Represents the color yellow.
- **Usage**: Used for drawing attention to specific elements.

#### CYAN

```python

CYAN = (0, 255, 255)
```

- **Description**: Represents the color cyan.
- **Usage**: Used for various interface elements needing a distinct color.

#### MAGENTA

```python

MAGENTA = (255, 0, 255)
```

- **Description**: Represents the color magenta.
- **Usage**: Used for styling elements that require a vivid color.

#### Maroon

```python

Maroon = (128, 0, 0)
```

- **Description**: Represents the color maroon.
- **Usage**: Used for text and other elements that need a darker red shade.

#### Silver

```python

Silver = (192, 192, 192)
```

- **Description**: Represents the color silver.
- **Usage**: Used for drawing less prominent elements.

#### Navy

```python

Navy = (0, 0, 128)
```

- **Description**: Represents the color navy.
- **Usage**: Used for buttons and other elements that require a deep blue color.

### Game Variables

The following variables are used to keep track of player scores throughout the game.

#### `player_x_score`

```python

player_x_score = 0
```

- **Description**: Tracks the score of player 'X'.
- **Usage**: Incremented when player 'X' wins a game.

#### `player_o_score`

```python

player_o_score = 0
```

- **Description**: Tracks the score of player 'O'.
- **Usage**: Incremented when player 'O' wins a game.

## Conclusion_


The `H_D_values` module provides essential constants and variables that are used throughout the Tic-Tac-Toe game. The color constants help maintain a consistent color scheme, while the score variables keep track of the players' progress. By centralizing these values in one module, the game's codebase remains organized and easier to manage.
