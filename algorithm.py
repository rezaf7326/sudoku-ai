import math


"""backtracking-search with CSF approach"""


class BacktrackingSudoku:
    def __init__(self, sudoku):
        # sudoku must be a python object
        self.__sudoku = sudoku
        self.__successful_search = False

    def search(self):
        solution = self.__search(self.__sudoku)
        if solution:
            self.__sudoku = solution
            self.__successful_search = True

    def get_result(self):
        if not self.__successful_search:
            print('sorry! could not find any solutions for the sudoku')
        return self.__sudoku

    # backtracking-search is a form of local-search:
    #   backtracking is an algorithmic technique for solving problems recursively
    #   by trying to build a solution incrementally, one piece at a time
    #   (in sudoku case - by one piece we mean one cell of the board),
    #   removing those solutions that fail to satisfy the constraints of
    #   the problem at any point of time.
    def __search(self, sudoku):
        if self.__is_sudoku_solved(sudoku):
            return sudoku

        var_i, var_j, domain = self.__var_selector(sudoku)

        for value in domain:
            if not self.__is_consistent(sudoku, var_i, var_j, value):
                continue
            sudoku[var_i][var_j] = value
            result = self.__search(sudoku)
            if result:
                return result
            sudoku[var_i][var_j] = 0

    @staticmethod
    def __var_selector(sudoku):
        for i in range(len(sudoku)):
            for j in range(len(sudoku)):
                if sudoku[i][j] == 0:
                    return i, j, range(1, len(sudoku) + 1)

    @staticmethod
    def __is_sudoku_solved(sudoku):
        for row in sudoku:
            for var in row:
                if var == 0:
                    return False
        return True

    # checks weather it is consistent with the rules of the
    #   game to assign the value to the cell at (i,j)
    @staticmethod
    def __is_consistent(sudoku, var_i, var_j, value):
        # check row consistency
        for var in sudoku[var_i]:
            if var != 0 and var == value:
                return False

        # check column consistency
        for row in sudoku:
            if row[var_j] != 0 and row[var_j] == value:
                return False

        # check sub-block (9-cell by 9-cell block) consistency
        sqrt_n = int(math.sqrt(len(sudoku)))
        block_i = int(var_i / sqrt_n)
        block_j = int(var_j / sqrt_n)
        qs = range(sqrt_n)
        for i in [block_i * sqrt_n + q for q in qs]:
            for j in [block_j * sqrt_n + q for q in qs]:
                if (i, j) != (var_i, var_j) and sudoku[i][j] != 0 and sudoku[i][j] == value:
                    return False

        return True
