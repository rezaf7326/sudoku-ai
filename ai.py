import json
from algorithm import BacktrackingSudoku


class AI:
    def __init__(self):
        pass

    # the solve function takes a json string as input
    # and outputs the solved version as json
    def solve(self, problem):
        problem_data = json.loads(problem)

        # backtracking as local-search
        backtracking = BacktrackingSudoku(problem_data.get("sudoku"))
        backtracking.search()
        solution = backtracking.get_result()

        return solution
