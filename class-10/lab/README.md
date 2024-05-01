# LAB-10: Connect 4

## Connect4 game
Connect Four (also known as Connect 4, Four Up, Plot Four, Find Four, Captain's Mistress, Four in a Row, Drop Four, and Gravities in the Soviet Union) is a two-player connection board game, in which the players choose a color and then take turns dropping colored tokens into a seven-column, six-row vertically suspended grid. The pieces fall straight down, occupying the lowest available space within the column. The objective of the game is to be the first to form a horizontal, vertical, or diagonal line of four of one's own tokens.

*for this lab, the winner will be only the first one who form a horizontal, vertical lines.  
the diagonal will be stretch goal*


1. Create a notebook on Kaggle called "connectFour"

## Lab Requirements
- We will build a connectFour game with a help from "numpy" and Matplotlib libraries
- we will consider that the player one will be represented as number 1, and number 2 for the player 2

## Implementation Notes
we will have a class called "connectFour", and implement the following methods:

- Constructor:
    - attribute for the board, array(6X7) of zeros
    - winner attribute (number = 0)

- drop_piece:
    - two parameters:
        1. Player_number will be 1 or 2 that refers to the player number
        2. The column that the player will put the token on
    - find the first available place to put the token on it
    - return the row, and a boolean referring that if there is a place or not

- check_winner:
    - parameters: row, column
    - check if there is a winner
    - return boolean

- show_board:
    - will show the board using The imshow() function in pyplot module of matplotlib library
    - make sure that every token's player have a different color

- play:
    - parameters:
        1. player_number
        2. column
    - make sure first that the player are even 1 or 2
    - drop a piece
    - check if there is a winner
    - show the board


## Testing
- create an instance for the game
- show the board
- start playing, adding these two scenarios 
- Add Two scenarios.
    - player one win with vertical lines
    - player Two win with horizontal lines

## Stretch goal
- find a way to check if there is a winner with diagonal line
  
## Submission Instructions
- Submit the link to your notebook