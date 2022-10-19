# stack-game
Game where you move stacked rings of different sizes to a new position in opposite order

The game begins in its initial state as follows:
![Alt text](https://github.com/Noah-Behm/stack-game/blob/main/start.PNG?raw=true "Title")

The player is prompted to pick a stack to move a piece from, and then where to place it.
After the player makes their choices, one of two major things will happen:

1. The player made a valid move:
![Alt text](https://github.com/Noah-Behm/stack-game/blob/main/valid_move.PNG?raw=true "Title")

In this case the player's move was valid, so the game state updates and it re-printed.

2. The player made an invalid move:
![Alt text](https://github.com/Noah-Behm/stack-game/blob/main/invalid_move.PNG?raw=true "Title")

In this case the player made an illegal move. They will be notified that they made a mistake, and prompted to hit enter when they are ready to resume.
After the player hits enter the same game state from before the illegal move will be displayed, and the player will be re-prompted to enter their move.

The goal of the game is the move all of the rings from stack 1 to stack 3. When this occurs the player has beat the game and the following screen will be displayed:
![Alt text](https://github.com/Noah-Behm/stack-game/blob/main/win.PNG?raw=true "Title")

Lastly, the player is asked if they would like to play again. If they enter 'y' the game restarts, otherwise the process ends.