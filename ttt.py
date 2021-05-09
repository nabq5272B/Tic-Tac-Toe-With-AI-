# Tic Tac Toe 

# Board 
board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

# Drawing the board on the screen 
def Board(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print("......")
    print(board[4] + '|' + board[5] + '|' + board[6])
    print("......")
    print(board[7] + '|' + board[8] + '|' + board[9])
    print("\n")


# To find out if there's any freespace in the board
def freeSpace(position):
    if board[position] == ' ': # If it finds a space in the board then it returns true
        return True
    
    return False # Otherwise it returns false

# To find out if the game is a draw
def Draw():
    for key in board.keys(): # Loop for searching each element in the board
        if board[key] == ' ': # If an element is empty it returns false, i.e. it will not draw 
            return False
    return True

# Evaluatiion Function for the win of the board
def Win():
    if (board[1] == board[2] and board[2] == board[3] and board[1] != ' '): # horizontal
        return True
    elif (board[4] == board[5] and board[5] == board[6] and board[4] != ' '): # "
        return True
    elif (board[7] == board[8] and board[8] == board[9] and board[7] != ' '): # "
        return True
    elif (board[1] == board[4] and board[4] == board[7] and board[1] != ' '): # vertical
        return True
    elif (board[2] == board[5] and board[5] == board[8] and board[2] != ' '): # "
        return True
    elif (board[3] == board[6] and board[6] == board[9] and board[3] != ' '): # "
        return True
    elif (board[1] == board[5] and board[5] == board[9] and board[1] != ' '): # diagonal
        return True
    elif (board[3] == board[5] and board[5] == board[7] and board[3] != ' '): # diagonal
        return True
    else:
        return False

# Evaluation Fucntion for marking down who wins the board, same as the Win() but sees that if board[i] = x or o, where i = 1 to 9
def Mark(mark):
    if (board[1] == board[2] and board[2] == board[3] and board[1] == mark):
        return True
    elif (board[4] == board[5] and board[5] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[8] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[4] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[5] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[6] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[5] == board[9] and board[1] == mark):
        return True
    elif (board[3] == board[5] and board[5] == board[7] and board[3] == mark):
        return True
    else:
        return False
    

# To insert a letter in the board (x or o) in a certain position
def letterInsert(letter, position):
    if freeSpace(position): # Finds the free space in the board where the player can insert the letter
        board[position] = letter
        Board(board)

        if Draw():
            print("Draw")
            exit()

        if Win():
            if letter == 'o':
                print('Player-2 Wins')
                exit()

            else:
                print("Player-1 wins!")
                exit()
        return
            

    else: # If no space is found then it asks the player to input a letter with a new position
        print('No insertion available')
        position = int(input("Enter new position: "))
        letterInsert(letter, position)
        return


player = 'x'
computer = 'o'

# Function for the player 1
def Player():
    position = int(input("Enter the position for player-1(x): "))
    letterInsert(player, position)
    return

# Function for the player 2
def Player2():
    position = int(input("Enter the position for player-2(o): "))
    letterInsert(computer, position)
    return

# Fucntion for the Computer
def Computer():
    bestScore = -1000 # initially we call this variable to take the best score and assign a negative large value
    bestMove = 0 # initally we call this variable to make the best move and assign 0
    for key in board.keys():
        if board[key] == ' ':
            board[key] = computer
            score = minimax(board, 0, False) # using the minimax algorithm for tic tac toe
            board[key] = ' '
            if score > bestScore: 
                bestScore = score
                bestMove = key

    letterInsert(computer, bestMove)
    return

# Here is the minimax function where we use the minimax algorithm in python for tic tac toe 
def minimax(board, depth, isMax):
    if Mark(computer): # computer = o
        return 1
    elif Mark(player): # player = x
        return -1
    elif Draw():
        return 0

    if isMax: # For maximizing
        bestScore = -1000
        for key in board.keys():
            if board[key] == ' ':
                board[key] = computer
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if score > bestScore:
                    bestScore = score
        return bestScore

    else: # For minimizing
        bestScore = 1000
        for key in board.keys():
            if board[key] == ' ':
                board[key] = player
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if score < bestScore:
                    bestScore = score
        return bestScore
    

while not Win():

    print('1' + '|' + '2' + '|' + '3')
    print("......")
    print('4' + '|' + '5' + '|' + '6')
    print("......")
    print('7' + '|' + '8' + '|' + '9 ')
    print("\n")

    print("Player-1 is x")
    print("Player-2 is o")
    print("\n")
    print("NOTE: While entering the position only use the number between (1-9) or else the game would crash!")
    print("\n")


    mode = input('Multiplayer(M) | AI(A): ') # Which mode the player wants to play


    if mode.upper() == 'M':
        
        while not Win():
            Player()
            Player2()
        

    elif mode.upper() == 'A':
        print('Now Player-2 is the computer!')

        difficulty = input('Easy(E) | Hard(H): ') # Difficulty settings in the AI mode

        if difficulty.upper() == 'E':
            while not Win():
                Player()
                Computer()

        elif difficulty.upper() == 'H':
            while not Win():
                Computer()
                Player()
        

    
    
    
