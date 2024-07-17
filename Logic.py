import pygame
import random
from random import choice
from H_D_values import *
class GameLogic:
    def __init__(self, LINE_COLOR, screen):
        """
            Class representing the game logic for a Tic-Tac-Toe game.

            Attributes:
                LINE_COLOR (tuple): The color of the lines on the game board.
                screen (pygame.Surface): The screen on which the game is played.
                board (list): A list representing the 3x3 game board with empty spaces.
                player (str): The current player ('X' or 'O').
                color_X (tuple): The color of the 'X' symbol.
                color_O (tuple): The color of the 'O' symbol.

            Methods:
                draw_board(screen_width, screen_height): Draw the game board on the screen.
                draw_x(x, y, width, height): Draw an 'X' symbol at the specified position.
                draw_o(x, y, width, height): Draw an 'O' symbol at the specified position.
                player_move(x, y): Process the player's move based on the screen coordinates.
                random_ai_move(): Make a random move for the AI player.
                check_winner(): Check if there is a winner on the current board.
                reset_board(): Reset the game board to its initial state.
        """
        # Color of the lines on the game board
        self.LINE_COLOR = LINE_COLOR

        # The screen on which the game is played
        self.screen = screen

        # Initialize a 3x3 board with all spaces empty
        self.board = [' ' for _ in range(9)]

        # Start with player 'X'
        self.player = 'X'
        
        self.color_X = BLUE
        self.color_O = WHITE

    def draw_board(self, screen_width, screen_height):
        """
            Draw the game board on the screen.

            Parameters:
                screen_width (int): The width of the screen.
                screen_height (int): The height of the screen.

            Returns:
                None
            """
        # Calculate the width and height of each third of the screen, leaving a 120-pixel border
        third_width = (screen_width - 240) // 3
        third_height = (screen_height - 240) // 3

        # Iterate over each position on the board
        for row in range(3):
            for col in range(3):
                # Calculate the index on the board based on the row and column
                index = row * 3 + col
                x = 120 + col * third_width
                y = 120 + row * third_height

                # Check the value at that position on the board
                if self.board[index] == 'X':
                    # Draw an 'X' shape if the value is 'X'
                    self.draw_x(x, y, third_width, third_height)
                elif self.board[index] == 'O':
                    # Draw an 'O' shape if the value is 'O'
                    self.draw_o(x, y, third_width, third_height)
                    
                    
        for i in range(1, 3):
            pygame.draw.line(self.screen, self.LINE_COLOR, (120, 120 + i * third_height), (120 + 3 * third_width, 120 + i * third_height), 7)
            pygame.draw.line(self.screen, self.LINE_COLOR, (120 + i * third_width, 120), (120 + i * third_width, 120 + 3 * third_height), 7)

        # Draw the border around the grid
        pygame.draw.rect(self.screen, self.LINE_COLOR, (120, 120, 3 * third_width, 3 * third_height), 7)


        # # Draw the horizontal lines dividing the board
        # pygame.draw.line(self.screen, self.LINE_COLOR, (120 + third_width, 120), (120 + third_width, 120 + 3 * third_height), 7)
        # pygame.draw.line(self.screen, self.LINE_COLOR, (120 + 2 * third_width, 120), (120 + 2 * third_width, 120 + 3 * third_height), 7)

        # # Draw the vertical lines dividing the board
        # pygame.draw.line(self.screen, self.LINE_COLOR, (120, 120 + third_height), (120 + 3 * third_width, 120 + third_height), 7)
        # pygame.draw.line(self.screen, self.LINE_COLOR, (120, 120 + 2 * third_height), (120 + 3 * third_width, 120 + 2 * third_height), 7)






    def draw_x(self, x, y, width, height):
        """
            Draw an 'X' symbol at the specified position on the game board.

            Parameters:
                x (int): The x-coordinate of the top-left corner of the cell.
                y (int): The y-coordinate of the top-left corner of the cell.
                width (int): The width of the cell.
                height (int): The height of the cell.

            Returns:
                None
        """
        padding = 20  # Padding from the edges of the cell
        pygame.draw.line(self.screen, self.color_X, (x + padding, y + padding), (x + width - padding, y + height - padding), 7)
        pygame.draw.line(self.screen, self.color_X, (x + width - padding, y + padding), (x + padding, y + height - padding), 7)



    def draw_o(self, x, y, width, height):
        """
            Draw an 'O' symbol at the specified position on the game board.

            Parameters:
                x (int): The x-coordinate of the top-left corner of the cell.
                y (int): The y-coordinate of the top-left corner of the cell.
                width (int): The width of the cell.
                height (int): The height of the cell.

            Returns:
                None
        """
        padding = 20  # Padding from the edges of the cell
        pygame.draw.ellipse(self.screen, self.color_O, (x + padding, y + padding, width - 2 * padding, height - 2 * padding), 7)



    def player_move(self, x, y):
        """
            Process the player's move based on the screen coordinates.

            Parameters:
                x (int): The x-coordinate of the click.
                y (int): The y-coordinate of the click.

            Returns:
                bool: True if the move is valid and made successfully, False otherwise.
        """
        # Calculate the board coordinates based on screen coordinates
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()
        third_width = (screen_width - 240) // 3
        third_height = (screen_height - 240) // 3

        # Check if the click is within the grid bounds (using the correct offset)
        if x < 120 or x > screen_width - 120 or y < 120 or y > screen_height - 120:
            return False

        # Calculate row and col using floating-point division for better accuracy
        col = (x - 120) // third_width
        row = (y - 120) // third_height
        
        
        """row and col are within valid range"""
        if col < 0 or col >= 3 or row < 0 or row >= 3:
            return False

        # Calculate the index on the board based on the row and column
        index = row * 3 + col

        # Check if the spot is empty and make the move
        if self.board[index] == ' ':
            self.board[index] = 'X'
            return True
        return False


    def random_ai_move(self):
        """
            Find all the indices of empty spots on the board.
            If there are empty spots, choose one randomly and place an 'O' there.
            Returns True if a move is made, False otherwise.
        """
        # Find all the indices of empty spots on the board
        empty_indices = [i for i, spot in enumerate(self.board) if spot == ' ']

        # If there are empty spots, choose one randomly and place an 'O' there
        if empty_indices:
            ai_index = random.choice(empty_indices)
            self.board[ai_index] = 'O'
            return True
        return False
    
    
    def check_winner(self):
        """
            Check if there is a winner on the current board.

            This function checks all the winning combinations on the board and returns the winning symbol if there is a winner.
            The winning combinations are defined as follows:
            - Horizontal: [0, 1, 2], [3, 4, 5], [6, 7, 8]
            - Vertical: [0, 3, 6], [1, 4, 7], [2, 5, 8]
            - Diagonal: [0, 4, 8], [2, 4, 6]

            Returns:
                str: The winning symbol ('X' or 'O') if there is a winner, None otherwise.
        """
        # Winning combinations
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
            [0, 4, 8], [2, 4, 6]  # Diagonal
        ]

        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ' ':
                return self.board[combo[0]]

        return None

    def reset_board(self):
        
        """
            Reset the game board to its initial state by replacing all the elements in the board list with empty spaces.

            This function does not take any parameters.

            Returns:
                None
        """
        
        self.board = [' ' for _ in range(9)]
