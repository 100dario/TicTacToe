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
First, the board is filled with a ``position`` dictionary. At the beginning of a match, this dictionary is going to be initialized with empty strings (``' '``) to create an empty board:    
<pre><code>position={7:' ', 8:' ', 9:' ', \
          4:' ', 5:' ', 6:' ', \
          1:' ', 2:' ', 3:' '}</code></pre>
          
The second thing you can notice is that, actually, a second board is being displayed! This board is static and shows 9 numbers that represents every position of the board, and it is arranged to imitate a numeric keypad. This is to facilitate the selection of the position that the player wants to put a symbol on.    
              
The board is displayed in the terminal like this:          

![Gameboard](https://user-images.githubusercontent.com/95108679/145337535-00a5683b-545f-4708-9084-0cd08cb1603b.png)           


Now, we need to make sure that a player selects only an empty position on the board. This can be acomplished by checking the current value on the dictionary that holds the symbols. If the value is an empty string (``' '``), it means that this position in available to place a new symbol:
<pre><code>while True:
       selec=int(input('\nNumber of position: '))
       if position[selec]==' ':
              position[selec]=playing
              break
       else:
              print('This position is already filled. Please, enter another number.')</code></pre>              
              
The variable ``playing`` holds a string 'X' or 'O' that changes every turn depending in the player (you can see how this works in the full code) and is used to fill the board with the corresponding symbol.            

Our final main portion of code is to check the winning conditions. Three same symbols in a row are necessary to win the game, so the program is going to check row by row, including diagnonals, and compare all the values of a single row to make sure that they are the same symbol. Also, the game can end in a draw after all the positions on the board are filled and no winning conditions are met. 

![winning](https://user-images.githubusercontent.com/95108679/145432475-4fc620ce-98f2-41e2-b607-01862994195a.png)             

And the winning conditions code looks like this:        
<pre><code>
if position[7]==position[4]==position[1]!=' ':
     end=True
elif position[8]==position[5]==position[2]!=' ':
     end=True
elif position[9]==position[6]==position[3]!=' ':
     end=True
#Checking horizontals from top to bottom
elif position[7]==position[8]==position[9]!=' ':
     end=True
elif position[4]==position[5]==position[6]!=' ':
     end=True
elif position[1]==position[2]==position[3]!=' ':
     end=True
#Checking diagonals
elif position[7]==position[5]==position[3]!=' ':
     end=True
elif position[9]==position[5]==position[1]!=' ':
     end=True

if end==True: 
       board()
       print('\nCongratulations! %s wins!'%(playing))
elif t==8:
       board()
       print('\nTied game :(')
       tied=True
       end=True</code></pre>
