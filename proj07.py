# =============================================================================
# 
# Project 7
# 
# Algorithm:
#     define dictionary
#     set initial variables used in functions
#     define initialize function
#     define function to choose the color
#     define function to display the board
#     define function to drop the disc
#     define function to check whether the disk is a winning four
#     define function to check whether the game is over
#     define main function to incorporate all other functions
#     run main
#     
# =============================================================================
    
pieces = {'black':'b', 'white':'w'}
COLUMN = 7
ROW = 6

def initialize():
    '''
    initialize function creates a list of lists called board
    to begin with an empty board
    
    '''
    board = []
    row0 = [0,0,0,0,0,0,0]
    row1 = [0,0,0,0,0,0,0]
    row2 = [0,0,0,0,0,0,0]
    row3 = [0,0,0,0,0,0,0]
    row4 = [0,0,0,0,0,0,0]
    row5 = [0,0,0,0,0,0,0]
    board.append(row0)
    board.append(row1)
    board.append(row2)
    board.append(row3)
    board.append(row4)
    board.append(row5)
    return board
    

def choose_color():
    '''
    choose color function takes no parameters and prompts at the beginning of
    the game for the first player to choose a function. It then assigns both 
    players to a color and returns these colors in a tuple
    
    '''
    while True:
        player1_color = input("Pick a color: ")
        if player1_color.lower() != "black" and player1_color.lower() != "white":
            print( "Wrong color; enter only 'black' or 'white', try again.")
        if player1_color.lower() == "black":
            player1_color = "black"
            player2_color = "white"
            break
        if player1_color.lower() == "white":
            player1_color = "white"
            player2_color = "black"
            break
    return (player1_color, player2_color)

def board_display(board):
    '''
    Board display takes in the board parameter which is initialized at the
    beginning and updated throughout the game and displays it in a visual way
    
    '''
    print("Current board:")
    C = COLUMN
    R = ROW
    hline = '\n' + (' ' * 2) + ('+---' * C) + '+' + '\n'
    numline = ' '.join([(' ' + str(i) + ' ') \
                        for i in range(1, C + 1)])
    str_ = (' ' * 3) + numline + hline
    for r in range(0, R):
        str_ += str(r+1) + ' |'
        for c in range(0, C):
            str_ += ' ' + \
                (str(board[r][c]) \
                     if board[r][c] is not 0 else ' ') + ' |'
        str_ += hline
    print (str_)

def drop_disc(board, column, color): 
    '''
    Drop disc function takes in three parameters, the board, column and color
    of the player's turn. It uses an if else statement to determine whether
    the column is valid then uses a loop if it is to check which row the entered 
    column is empty at to place it there. If the column is not valid it returns
    none, if it is full it returns "full" and otherwise it returns the row.
    
    '''
    if column not in range(1,8):
        print("Column should be in range 1 to 7. Please try again.")
        return None
    else:
        column = column - 1
        for ROW in reversed(range(6)):    
            if board[ROW][column] == 0:
                board[ROW][column] = pieces[color]
                break
            ROW -= 1
            if board[0][column] != 0:
                print("This column is full. Please try again.")
                ROW = "full"
                break
        if ROW != "full":
            ROW += 1
        return ROW

def check_disc(board, row, column):
    '''
    Check disc function takes in three parameters, board, row, and column of 
    a certain disc. It then scans the disc and surrounding discs with loops
    to check if the disc is part of a vertic group of 4 of the same color, a 
    horizontal group and a diagonal group. It returns True if it is and False
    if it is not.
    
    '''

        # Define list of lists of lists for each possible coordinate in 
        # diagonal winning groups
    diagonals = []
    
    diag_0 = [[0,3],[1,2],[2,1],[3,0]]
    diag_1 = [[0,4],[1,3],[2,2],[3,1],[4,0]]
    diag_2 = [[0,5],[1,4],[2,3],[3,2],[4,1],[5,0]]
    diag_3 = [[1,5],[2,4],[3,3],[4,2],[5,1],[6,0]]
    diag_4 = [[2,5],[3,4],[4,3],[5,2],[6,1]]
    diag_5 = [[3,5],[4,4],[5,3],[6,2]]
    diag_6 = [[6,3],[5,2],[4,1],[3,0]]
    diag_7 = [[6,4],[5,3],[4,2],[3,1],[2,0]]
    diag_8 = [[6,5],[5,4],[4,3],[3,2],[2,1],[1,0]]
    diag_9 = [[5,5],[4,4],[3,3],[2,2],[1,1],[0,0]]
    diag_10 = [[4,5],[3,4],[2,3],[1,2],[0,1]]
    diag_11 = [[3,5],[2,4],[1,3],[0,2]]
    
    diagonals.append(diag_0)
    diagonals.append(diag_1)
    diagonals.append(diag_2)
    diagonals.append(diag_3)
    diagonals.append(diag_4)
    diagonals.append(diag_5)
    diagonals.append(diag_6)
    diagonals.append(diag_7)
    diagonals.append(diag_8)
    diagonals.append(diag_9)
    diagonals.append(diag_10)
    diagonals.append(diag_11)
    
        # define counter variables and edit rows and columns
    counter_col = 0
    counter = 0
    counter_diag = 0
    row = row -1 
    column = column - 1
    
        # return None if row or column are not valid
    if row not in range(0,6) or column not in range(0,7):
        return None
    
        # dictate which color is being checked
    if board[row][column] == "b":
        color_of_disc = "b"
    elif board[row][column] == "w":
        color_of_disc = "w"
    else:
        return False
    
        # create loop to go through each row in set column, checking for
        # horizontal groups of 4 of the dictated color, returns True if one exists
    for r in range(6):
        if board[r][column] == color_of_disc:
            counter += 1
            if counter == 4:
                return True
                break
        if board[r][column] != color_of_disc:
            counter = 0
            
        # create loop to go through each column in set row, checking for
        # vertical groups of 4 of the dictated color, returns True if one exists        
    for c in range(7):
        if board[row][c] == color_of_disc:
            counter_col += 1
            if counter_col == 4:
                return True
                break
        if board[row][c] != color_of_disc:
            counter_col = 0
       
        # create loop to go through each diagonal group in list called diagonals
    for diag in diagonals:
            # if set column and row is in one group, loop through each location
            # looking for groups of 4 of the dictated color, return True if one exists
        if [column, row] in diag:
            counter_diag = 0
            for location in diag:
                if board[location[1]][location[0]] == color_of_disc:
                    counter_diag +=1
                    if counter_diag == 4:
                        return True
                if board[location[1]][location[0]] != color_of_disc:
                    counter_diag = 0

        # return False if no counters contain four consecutive color             
    if counter_col < 4 and counter < 4 and counter_diag <4:
        return False
    

def is_game_over(board):
    '''
    Is game over takes one parameter of board then iterates through each 
    location to check each disk using check_disk. It counts empty spaces as
    well and returns "draw" if there are no empty spaces. Otherwise it returns
    the winning color if there is a win and returns False if there is not.
    '''
    empty = 0
    winning_color = ""
    
        # iterate through locations to find winning group
    for row in range(6):
        for column in range(7):
            if board[row][column] == 0:
                empty += 1
            if check_disc(board,row,column) == True:
                winning_color = board[row][column]
                if winning_color ==  'w':
                    winning_color = "white" 
                elif winning_color == 'b':
                    winning_color = "black"
                    
        # returns different values depending on win and empty spaces
    if empty == 0:
        return "draw"
    elif winning_color == "":
        return False
    else:
        return winning_color
            


def main():
    '''
    The main function displays rules for game, prompts the players and combines
    all defined functions to loop through alternating player turns until there
    is a win, someone passes, or someone exits.
    
    '''
    banner = """
       ____ ___  _   _ _   _ _____ ____ _____ _  _   
      / ___/ _ \| \ | | \ | | ____/ ___|_   _| || |  
     | |  | | | |  \| |  \| |  _|| |     | | | || |_ 
     | |__| |_| | |\  | |\  | |__| |___  | | |__   _|
      \____\___/|_| \_|_| \_|_____\____| |_|    |_|  
    """
    intro = """
    Connect Four is a two-player connection game in which the players first choose a color and \
    then take turns dropping one colored disc from the top into a seven-column, six-row vertically suspended grid. \
    The pieces fall straight down, occupying the lowest available space within the column. \
    The objective of the game is to be the first to form a horizontal, vertical, or diagonal line of four of one's own discs. 
    """
    usage = """
        Usage:
            pass:   give up, admit defeat
            exit:   exit the game
            i:      drop a disk into column i
    """
    
        # print the initial strings and define variables
    print(banner)
    print(intro)
    print(usage)
    player_color = ""
    other_color = ""
    count = 0
    usage_choice = ""
    usage_choice = ""
    continue_game = 'yes'  # can't use "continue" because it has a special meaning
    
        # main while loop loops as long as continue game is "yes"
    while continue_game == "yes" :
        color = choose_color()      # prompt for color of player 1
        print("You are '{}' and your opponent is '{}'.".format(color[0],color[1]))
        board = initialize()
        board_display(board)        # initialize and display board
        
            # second while loop loops until break is stated
        while True:
            if count%2 == 0:                # alternate players by keeping count
                player_color = color[0]
                other_color = color[1]
            else:
                player_color = color[1]
                other_color = color[0]
                
                # prompt for turn
            usage_choice = input("{}'s turn :> ".format(player_color))
                
                # if statement for exit
            if usage_choice.lower() == "exit":
                continue_game = ""
                break

                # elif statement for pass
            elif usage_choice.lower() == "pass":
                print("{} gave up! {} is the winner!! yay!!!".format(player_color,other_color))
                continue_game = input("Would you like to play again? ").lower()
                break 
            
                # elif statement for if a digit is entered
            elif usage_choice.isdigit():
                
                    # if statement for an invalid column
                if int(usage_choice) < 1 or int(usage_choice) > 7:
                    print("Invalid column: 1 <= column <= 7. Please try again.")
                    continue
                
                    # elif statemnt for a correct column, functions stated to continue game play
                elif int(usage_choice) >= 1 and int(usage_choice) <= 7:
                    drop_disc(board, int(usage_choice), player_color)
                    board_display(board)
                    game_over = is_game_over(board)
                    
                        # if and elif statements for if the game ends
                    if game_over == "draw":
                        print("The board is full so this game ends in a draw.")
                        continue_game = input("Would you like to play again? ").lower()
                        break
                    elif game_over == "white":
                        print("white wins!")
                        continue_game = input("Would you like to play again? ").lower() 
                    elif game_over == "black":
                        print("black wins!")
                        continue_game = input("Would you like to play again? ").lower()
                        break 
                    count +=1           # count increased to alternate players
                    
            else:       # else if an invalid option is entered
                print("Invalid option\n", usage)                
                
    else:       # else if continue_game does not equal yes
        print("\nThanks for playing! See you again soon!")
        quit



if __name__ == "__main__":
    main()