#tik tak toe game
import random

def game():
    
    play = True
    board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]     
    
    def vizualize():
        print(board[0])
        print(board[1])
        print(board[2])

    turn = True
    turn_num = 0
    while play:
        if turn_num == 0:
            vizualize()
            
        x = int(input('please enter a row (1, 2, or 3) '))
        y = int(input('please enter a column (1, 2, or 3) '))
        if board[x - 1][y - 1] == '_':
            if turn:
                board[x - 1][y - 1] = 'X'
                turn = False
                turn_num += 1
            else:
                board[x - 1][y - 1] = 'O'
                turn = True
                turn_num += 1
        else:
            print('This spot has already been taken')
            continue
        
        vizualize()
        if turn_num >= 5 and turn_num <= 9:
            play = logic(board)
            if turn_num == 9:
                print("It's a tie")
                play = False

def logic(x):

    for i in range(0, 2):
        if x[i][0] == x[i][1] and x[i][1] == x[i][2]:
            if x[i][0] == 'X':
                print('Game Over. Player 1 wins')
            else:
                print('Game Over. Player 2 wins')
            return False
            
        elif x[0][i] == x[1][i] and x[1][i] == x[2][i]:
            if x[i][0] == 'X':
                print('Game Over. Player 1 wins')
            else:
                print('Game Over. Player 2 wins')
            return False
            
    if x[0][0] == x[1][1] and x[1][1] == x[2][2]:
        if x[i][0] == 'X':
            print('Game Over. Player 1 wins')
        else:
            print('Game Over. Player 2 wins')
        return False
        
    elif x[2][0] == x[1][1] and x[1][1] == x[0][2]:
        if x[i][0] == 'X':
            print('Game Over. Player 1 wins')
        else:
            print('Game Over. Player 2 wins')
        return False
    else:
        return True
        
game()

