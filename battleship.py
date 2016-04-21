from random import randint

board = []

number_turns = 4

#the range increases the columns, the board.append increases the rows
for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print ("".join(row))

print ("Let's play Battleship!")
print ("You have "+ str(number_turns) + " turns to hit my ship")
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

#Uncomment these if you want to see the answer each time
#print ship_row
#print ship_col

for turn in range(number_turns):
    
    guess_row = int(input("Guess Row:"))-1
    guess_col = int(input("Guess Col:"))-1

    if guess_row == ship_row and guess_col == ship_col:
        print ("Congratulations! You sunk my battleship!")
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print ("Oops, that's not even in the ocean.")
        elif(board[guess_row][guess_col] == "X"):
            print ("You guessed that one already.")
        else:
            print ("You missed my battleship!")
            board[guess_row][guess_col] = "X"
    print ("You have " + str(number_turns - (turn + 1)) + " turns left")
    print_board(board)
    print("")