from IPython.display import clear_output

player1 = ""
player2 = ""
player1_marker = ''
player2_marker = ''

#This function will print out a board and it will have indexes 1-9 which corresponds to number on the numberpad
#The 1-9 pad will have 3x3 board representation.
def display_board(board):
        print("| |")
        print("" + board[7] + "|" + board[8] + "|" + board[9])
        print("| |")
        print("---------")
        print("| |")
        print("" + board[4] + "|" + board[5] + "|" + board[6])
        print("| |")
        print("---------")
        print("| |")
        print("" + board[1] + "|" + board[2] + "|" + board[3])
        print("| |")

#Take in the player's input which can be in form of X or O. while loop the input process till X/O are obtained.
def player_input():
    marker = ''
    while not (marker == "X" or marker == "O"):
        print("Do you want to be X or O,", player1, "?")
        marker = input()
        if marker == "X":
            print(player1 , "is X and", player2 , "is O")
            return ('X','O')
        else:
            print(player1 , "is O and", player2 , "is X")
            return ('O','X')

#Take the inputted marker and apply it on the board in this function.
def place_marker(board, marker, position):
    board[position] = marker

#Take in the board and check if the mark makes one player win or no.
def win_check(board, mark):
    return((board[7] == mark and board [8] == mark and board[9] == mark) or
           (board[4] == mark and board[5] == mark and board[6] == mark) or
           (board[1] == mark and board[2] == mark and board[3] == mark) or
           (board[7] == mark and board[4] == mark and board[1] == mark) or
           (board[8] == mark and board[5] == mark and board[2] == mark) or
           (board[9] == mark and board[6] == mark and board[3] == mark) or
           (board[7] == mark and board[5] == mark and board[3] == mark) or
           (board[9] == mark and board[5] == mark and board[1] == mark))

#Randomly decides which player goes first using the random module. return a string of which player goes first.
import random
def choose_first():
    if random.randint(0,1) == 0:
        return player2
    else:
        return player1

#returns true or false if space is available on the board or no.
def space_check(board,position):
    return board[position] == ''

#Check if the board is full or no.
def full_board_check(board):
    for i in range(0,10):
        if space_check(board,i):
            return False
        return True

#Ask for the players choice from 1-9 numbers. and run space_check() function to see the space is available or no.
def player_choice(board):
    position = ''
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board,int(position)):
        print("Choose your position: (1-9)")
        position = input()
    return int(position)

#Boolean value is returned after asking if the players want to play again.
def replay():
    return "Do you want to play again? Enter 'yes' or 'no' !".lower().startswith('y')

print("Welcome to TIC-TAC-TOE!!")

while True:
    #Reset the board.
    theBoard = [''] * 10
    if(player1 == '' or player2 == ''):
        player1 = input("enter player 1's name: ")
        player2 = input("enter player 2's name: ")
    if player1_marker == '' and player2_marker == '':
        player1_marker,player2_marker = player_input()
    turn = choose_first()
    print(turn + " will go first!")
    game_on = True

    while game_on:
        if turn == player1:
            #Player1's turn
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard,player1_marker,position)
            if win_check(theBoard,player1_marker):
                display_board(theBoard)
                print(player1, ", congrats! You won!")
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("Draw Game!")
                    break
                else:
                    display_board(theBoard)
                    turn = player2
        else:
            #Player 2's turn
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard,player2_marker,position)

            if win_check(theBoard,player2_marker):
                display_board(theBoard)
                print(player2, "has won!")
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("Draw Game!")
                    break
                else:
                    turn = player1
        if not replay():
            break