# TicTacToe - Python

This code is an introductory Tic Tac Toe game developed in Python.  

+ It requires two players and it's played in the terminal by inserting numbers. A distribution of numbers are displayed to help locate the positions on the board.
+ The first match starts with the 'X' player but after a match finishes the starting player changes.  
+ At the end of a match a score is presented with the points of every player. If the game ends in draw no points are added to the players.

### How the code works?   
As you know, Tic Tac Toe is won by placing three equals symbols in a row. It could be horizontally, vertically or diagonally.   
In every turn, each player has the oportunity to place their symbol in the empty spaces of the board. No symbols can be placed in already filled spaces.    
so far, we need to:   
1. Create a board able to change every turn to show the status of the game.
2. Check if a selected position on the board is filled or if it is available to place a symbol.
3. Check the winning conditions.    

For the board, a function ``board()`` is declared:   
<pre><code>def board():    
       print(position[7],'|',position[8],'|',position[9], end='        ')   
       print('7 | 8 | 9')   
       print('--+---+--', end='        ')   
       print('--+---+--')   
       print(position[4],'|',position[5],'|',position[6], end='        ')   
       print('4 | 5 | 6 ')    
       print('--+---+--',  end='        ')    
       print('--+---+--')   
       print(position[1],'|',position[2],'|',position[3], end='        ')   
       print('1 | 2 | 3 ')</code></pre>   
       
Two things are happening in this function.  
First, the board is filled with a ``position`` dictionary. At the beginning of the a match, this dictionary is going to be initialized with empty strings (``' '``) to create an empty board:    
<pre><code>position={7:' ', 8:' ', 9:' ', \
          4:' ', 5:' ', 6:' ', \
          1:' ', 2:' ', 3:' '}</code></pre>
          
The second thing you can notice is that, actually, a second board is being displayed! This board is static and shows 9 numbers that represents every position of the board, and it is arranged to imitate a numeric keypad. This is to facilitate the selection of the position that the player wants to put a symbol on.

![Gameboard](https://user-images.githubusercontent.com/95108679/145337535-00a5683b-545f-4708-9084-0cd08cb1603b.png)
