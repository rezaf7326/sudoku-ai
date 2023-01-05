import json
from algorithm import BacktrackingSudoku, BacktrackingSudokuMRV


class AI:
    def __init__(self):
        pass

    # the solve function takes a json string as input
    # and outputs the solved version as json
    def solve(self, problem):
        problem_data = json.loads(problem)
        sudoku_obj = problem_data.get("sudoku")

        # backtracking as local-search:

        """simple:"""
        # backtracking = BacktrackingSudoku(sudoku_obj)
        """MRV heuristic:"""
        backtracking = BacktrackingSudokuMRV(sudoku_obj)

        backtracking.search()
        solution = backtracking.get_result()

        return solution
