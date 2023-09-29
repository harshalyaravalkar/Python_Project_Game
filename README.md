# Python_Project_Game
This is my first project of python

In this project I coded a simple game.

in this game at first player is asked for a name for its character.
Then displays a main menu where player selects to :
1. Start Game
2. Display Life
3. Display Score
4. Display Coins
5. Quit Game
and asks for a input selection to enter number of coice.

Based on the choice game either displays the values or starts game or Quits game.
When player chooses to start game.
Player can perform 3 actions by giving input of respective alphabets for:

K = Kick
P = Punch
J = Jump

initially the attributes Score, Life and Coins which defined as Private attributes are 0,3 and 0 respectively

"Kick" action increments Score by 10
"Punch" action increments Score by 5
"Jump" action gains 2 coins

Game is Over when player looses all of its 3 lives and that is programmed to happen every time when a loop randomly selects 3 from a tuple of integers 1 to 4,this action is defined as "Stab" action.

Loops control the whole flow of this program and so I needed to have good understanding of loops.
When Lives become 0 loop terminates as it checks value of life attribute for every loop.
So, Game Ends there. 
