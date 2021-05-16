from IPython.display import clear_output

def display_board(board):
    
    print(board[7]+' | '+board[8]+' | '+board[9])
    print('--|'+'---|'+'--')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('--|'+'---|'+'--')
    print(board[1]+' | '+board[2]+' | '+board[3])

test_board=['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)

def player_input():


    marker=''
    while marker!='X' and marker!='O':
        marker=input('Player1 : Choose X or O: ').upper()
    if marker=='X':
        return('X','O')
    else:
        return('O','X')
player_input()

def place_marker(board,marker,position):
    board[position]=marker

place_marker(test_board,'$',8)
display_board(test_board)


def win_check(board,mark):
#Win tic tac toe?
#all rows  and column check & diagonals check
    return (board[7]==mark and board[8]==mark and board[9]==mark) or(board[4]==board[5]==board[6]==mark) or (board[1]==board[2]==board[3]==mark) or (board[7]==board[4]==board[1]==mark) or (board[8]==board[5]==board[2]==mark) or (board[9]==board[6]==board[3]==mark) or (board[1]==board[5]==board[9]==mark) or (board[3]==board[5]==board[7]==mark)
display_board(test_board)
win_check(test_board,'X')

#randomly decide who go first

import random

def choose_first():
    flip=random.randint(0,1)
    if flip==0:
        return 'Player1'
    else:
        return 'Player2'

def space_check(board,position):
    return board[position]== ' '

def full_boardCheck(board):
    for i in range(0,10):
        if space_check(board,i):
            return False

    return True
    
def player_choice(board):
    position=0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input('Choose a position: (1-9)'))
    return position

def replay():
    return input("Play again? Yes or No").lower().startswith('y')
    

#while loop to keep running the game
print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_boardCheck(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_boardCheck(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break