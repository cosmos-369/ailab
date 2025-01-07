board = [" " for x in range(9)] 
def print_board(): 
    print() 
    print("|{}|{}|{}|".format(board[0], board[1], board[2]))
    print("|{}|{}|{}|".format(board[3], board[4], board[5]))
    print("|{}|{}|{}|".format(board[6], board[7], board[8]))
    print() 

def player_move(icon): 
    if icon == "x": 
        number = 1 
    else: 
        number = 2 
    
    print(f"your turn player{number}") 
    choice = int(input("enter your move:"))
    if board[choice] == " ": 
        board[choice] = icon 
    else: 
        print("space is already taken") 

def is_victory(icon) -> bool: 
    # check rows and cols 
    for i in range(3): 
        if board[i] == board[i+1] == board[i+2] == icon: 
            return True 
        if board[i] == board[i+3] == board[i+6] == icon: 
            return True 
    
    if board[0] == board[4] == board[8] == icon: 
        return True 
    if board[2] == board[4] == board[5] == icon: 
        return True 

    return False 


def is_draw(): 
    if " " not in board: 
        return True 
    return False 

# game logic 
while True: 
    print_board() 

    player_move("x") 
    print_board()
    if is_victory("x"): 
        print("x wins.!!") 
        break 
    elif is_draw(): 
        print("it a draw") 
        break 

    player_move("o") 
    print_board()
    if is_victory("o"): 
        print("o wins.!!") 
        break 
    elif is_draw(): 
        print("it a draw") 
        break 

