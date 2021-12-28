from random import shuffle
import sys

def display_board(board):
    print("_____________")
    print("|",board[0],"|",board[1],"|",board[2],"|")
    print("-------------")
    print("|",board[3],"|",board[4],"|",board[5],"|")
    print("-------------")
    print("|",board[6],"|",board[7],"|",board[8],"|")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾") #print(chr(8254)+chr(8254))
    #print("▔▔▔▔▔▔▔") # print(chr(0x2594))
    #print(chr(0x35e)+chr(0x35e))

def player_input():

    choice = input("Please choose X or O: ")
    while choice.upper()[0] is not 'X' and choice.upper()[0] is not 'O':

        choice = input("Wrong choice, please choose between X or O: ")
    
    if choice.upper()=='X':
        return ['X','O']
    elif choice.upper()=='O':
        return ['O','X']

def place_marker(board, choice, position):
    if board[position]==' ':
        board[position]=str(choice).upper()
        return board
    else:
        print("TURN LOST! Make sure to select EMPTY spaces!")

def win_check(board, mark):
    # if 012, 345, 678, 246, 047, 036, 147, 258
    mark = str(mark).upper()
    return (board[0]==board[1]==board[2]==mark # top across
    or board[3]==board[4]==board[5]==mark # middle across
    or board[6]==board[7]==board[8]==mark # bottom across
    or board[2]==board[4]==board[6]==mark # diagonal
    or board[0]==board[4]==board[8]==mark # diagonal
    or board[0]==board[3]==board[6]==mark # left down
    or board[1]==board[4]==board[7]==mark # middle down
    or board[2]==board[5]==board[8]==mark) # right down

def who_first(players):
    shuffle(players)
    return players

def space_check(board, position):
    if board[position]==' ':
        return True
    else:
        return False 

def full_board_check(board):
    return False if ' ' in board else True

def player_choice(board):

    choice = input("Please choose a position (1-9): ")
    while choice.isalpha() or int(choice)not in [1,2,3,4,5,6,7,8,9]: #choice=='0' or int(choice)>=10
        choice = input("Wrong choice! Try again (1-9): ")


    return int(choice)-1 if space_check(board, int(choice)-1) else False

def replay():
    answer = input("Play again?(Y/N) ")
    while answer.upper() not in ['Y', 'N']:
        answer = input("Wrong input! Play again?(Y/N) ")
    if answer.upper()=='Y':
        return True
    elif answer.upper()=='N':
        return False


print("Welcome to Tic Tac Toe!")

# display_board(board)
# full_board_check(board)
# replay()
# player_choice(board)
# space_check(board, position='')
# who_first()
# player_input()
# place_marker(board,choice,position='')
# win_check(board, mark='')


while True:
    # Set the game up here
    board = [" "]*9
    players = player_input()
    print("Players: {}".format(players))
    print("Player 1: {}\nPlayer 2: {}".format(players[0],players[1]))
    players = who_first(players)
    print("Shuffled players: {}".format(players))
    print(f"{players[0]} goes first!")
    display_board(board)
    game_on = True
    #pass

    while game_on:
        #Player 1 Turn
        if full_board_check(board)==False:
            print("Player 1:")
            place_marker(board, players[0], player_choice(board))
            display_board(board)
        else:
            print("The game is a Draw!")
            if replay()==False:
                print("Goodbye! Thanks for playing!")
                sys.exit()
            else:
                break
        if win_check(board, players[0]):
            print("Congratulations! Player 1 won!")
            if replay()==False:
                print("Goodbye! Thanks for playing!")
                sys.exit()
            else:
                break
        

        # Player2's turn.
        if full_board_check(board)==False:
            print("Player 2:")
            place_marker(board, players[1], player_choice(board))
            display_board(board)
        else:
            print("The game is a Draw!")
            if replay()==False:
                print("Goodbye! Thanks for playing!")
                sys.exit()
            else:
                break
        if win_check(board, players[1]):
            print("Congratulations! Player 2 won!")
            if replay()==False:
                print("Goodbye! Thanks for playing!")
                sys.exit()
            else:
                break
        