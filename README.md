# stack-game
In-terminal game where you move stacked rings of different sizes to a new position<br/>

The game begins in its initial state as follows:<br/>
![Alt text](https://github.com/Noah-Behm/stack-game/blob/main/start.PNG?raw=true "Title")

The player is prompted to pick a stack to move a piece from, and then where to place it.<br/>
After the player makes their choices, one of two major things will happen:<br/><br/>

1. The player made a valid move:<br/>
![Alt text](https://github.com/Noah-Behm/stack-game/blob/main/valid_move.PNG?raw=true "Title")<br/><br/>

In this case the player's move was valid, so the game state updates and it re-printed.<br/><br/>

2. The player made an invalid move:<br/>
![Alt text](https://github.com/Noah-Behm/stack-game/blob/main/invalid_move.PNG?raw=true "Title")<br/><br/>

In this case the player made an illegal move. They will be notified that they made a mistake, and prompted to hit enter when they are ready to resume.<br/>
After the player hits enter the same game state from before the illegal move will be displayed, and the player will be re-prompted to enter their move.<br/><br/>

The goal of the game is the move all of the rings from stack 1 to stack 3. When this occurs the player has beat the game and the following screen will be displayed:<br/>
![Alt text](https://github.com/Noah-Behm/stack-game/blob/main/win.PNG?raw=true "Title")<br/><br/>

Lastly, the player is asked if they would like to play again. If they enter 'y' the game restarts, otherwise the process ends.