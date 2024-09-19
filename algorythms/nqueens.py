from typing import List

def is_safe(board, row, col, n):
    for i in range(col):
        if board[row][i] == 'Q':
            return False

    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1


    i, j = row, col
    while i < n and j >= 0:
        if board[i][j] == 'Q':
            return False
        i += 1
        j -= 1

    return True

def solve_n_queens_from_partials(board: List[List[str]], col: int, n: int) -> List[List[str]]:
    if col >= n:
        raise ValueError("col_start ne peut pas être supérieur ou égal à la taille de l'échiquier.")
    
    def solve(board, col, solutions):
        if col == n:
            print(f"Solution trouvée : {board}")  
            solutions.append(["".join(row) for row in board])
            return
        for i in range(n):
            if is_safe(board, i, col, n):
                board[i][col] = 'Q'
                print(f"Place reine en ({i}, {col})")  
                solve(board, col + 1, solutions)
                board[i][col] = '.'
    
    solutions = []
    solve(board, col, solutions)
    
    if not solutions:
        print("Aucune solution trouvée.") 
    
    return solutions

