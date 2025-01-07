def is_safe(board, row, col): 
    # check vertically 
    for i in range(row): 
        if board[i] == col: 
            return False 
        
    # check diagonally
    for i in range(row): 
        if abs(i - row) == abs(board[i] - col):
            return False 

    return True 

def solve_n_queen(board, row): 
    if row == len(board): 
        return [board[:]] 
    
    solutions = [] 
    for col in range(len(board)): 
        if is_safe(board, row, col): 
            board[row] = col 
            solutions.extend(solve_n_queen(board, row + 1))
            board[row] = -1 

    return solutions 

def print_solution(solution):
    for row in solution:
        print(" ".join("Q" if i == row else "." for i in range(len(solution)))) 
        print("\n")

n = 8 
board = [-1] * n 
solutions = solve_n_queen(board, 0)
print(f"Found {len(solutions)} solutions for the 8-Queens problem.\n")

if solutions:
    print("One of the solutions:")
    print_solution(solutions[0])
