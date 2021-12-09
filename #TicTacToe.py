#Tic Tac Toe by 100dario

#Board of the game. Every slot is filled with the content of the dictionary 'position' that is going to change during the game.
def board():
       print(position[7],'|',position[8],'|',position[9], end='        ')
       print('7 | 8 | 9')
       print('--+---+--', end='        ')
       print('--+---+--')
       print(position[4],'|',position[5],'|',position[6], end='        ')
       print('4 | 5 | 6 ')
       print('--+---+--',  end='        ')
       print('--+---+--')
       print(position[1],'|',position[2],'|',position[3], end='        ')
       print('1 | 2 | 3 ')

score={"X":0,"O":0} #Creating dictionary to store the score

print('\n#############################')
print('   Welcome to Tic Tac Toe!\n\n  To play, press the number \n  of the \
position you would \n  like to place your symbol')



whoplay=0 #Controls who plays at the beginning of every game
rnd=1 #Round
while True: #The game continues after a match finishes

       #Creation of the content of the gameboard, starting with empty strings in every slot
       #The keys represent the number of the slot to be filled, and is arranged to be exactly as a numeric keypad. 
       position={7:' ', 8:' ', 9:' ', \
              4:' ', 5:' ', 6:' ', \
              1:' ', 2:' ', 3:' '}

       #X starts the game but changes every game
       if whoplay%2==1:
              playing='X'
       else:
              playing='O'

       print('\n\n\n\nROUND %s:'%rnd)
       print('Score: X:%s   O:%s' %(score['X'],score['O']))

       tied=False #Check if game was a draw, so no points are added to the score
       t=0 #turn
       end=False #end of the game

       while end==False:
              #Changing the player every turn
              if playing=='X':
                     playing='O'
              else:
                     playing='X'

              print('\n#############################')
              print('It is %s\'s turn:\n' %(playing))

              board() #Calls the board
              while True:
                     selec=int(input('\nNumber of position: ')) #Player enters position
                     if position[selec]==' ': #Check if position is empty
                            position[selec]=playing #The position selected is filled with the current symbol
                            break
                     else: #If position is not empty, the program asks for a new number
                            print('This position is already filled. Please, enter another number.')
              

              if t>=4: #Only after 5 turns there can be a winner
                     
                   #Checking verticals from left to right
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

              if end==True: #Prints winner
                     print('\n')
                     board()
                     print('\nCongratulations! %s wins!'%(playing))
              elif t==8: #Tied condition after no winner
                     print('\n')
                     board()
                     print('\nTied game :(')
                     tied=True
                     end=True
                          
              
              t+=1
              
       if tied==False: #If the game ended tied no points are added to the score
              score[playing]+=1
       whoplay+=1
       rnd+=1


