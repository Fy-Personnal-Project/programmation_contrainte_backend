from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from fastapi import FastAPI, HTTPException
from algorythms.nqueens import solve_n_queens_from_partials, is_safe


app = FastAPI()

class PartialBoard(BaseModel):
    board: List[List[str]]
    col_start: int  

@app.get("/")
def read_root():
    return {'message' : 'Bonjour, FastAPI'}

@app.post("/solve_partial")
def solve_nqueens_partial(partial_board: PartialBoard):
    board = partial_board.board
    col_start = partial_board.col_start
    n = len(board)
    
    try:
        solutions = solve_n_queens_from_partials(board, col_start, n)
        if not solutions:
            raise HTTPException(status_code=404, detail="Aucune solution trouvée.")
        return {"solutions": solutions, "total_solutions": len(solutions)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

