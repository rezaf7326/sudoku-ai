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

        var_i, var_j, domain = self._var_selector(sudoku)

        for value in domain:
            if not self.__is_consistent(sudoku, var_i, var_j, value):
                continue
            sudoku[var_i][var_j] = value
            result = self.__search(sudoku)
            if result:
                return result
            sudoku[var_i][var_j] = 0

    # as protected method:
    def _var_selector(self, sudoku):
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


# backtracking with MRV heuristic:
class BacktrackingSudokuMRV(BacktrackingSudoku):
    def __init__(self, sudoku):
        super().__init__(sudoku)

    def _var_selector(self, sudoku):
        min_domains = self.__mrv_domains(sudoku)

        if not min_domains:
            return None, None, None

        var = min_domains.popitem()
        return var[0][0], var[0][1], var[1]

    @staticmethod
    def __mrv_domains(sudoku):
        domains_dict = {}
        for i in range(len(sudoku)):
            for j in range(len(sudoku)):
                if sudoku[i][j] == 0:
                    domains_dict[i, j] = set(range(1, len(sudoku) + 1))

        sqrt_n = int(math.sqrt(len(sudoku)))

        for i in range(len(sudoku)):
            for j in range(len(sudoku)):
                if type(sudoku[i][j]) is not set:
                    qs = range(sqrt_n)
                    block_i = int(i / sqrt_n)
                    block_i_set = {block_i * sqrt_n + q for q in qs}
                    block_j = int(j / sqrt_n)
                    block_j_set = {block_j * sqrt_n + q for q in qs}

                    for k in domains_dict.keys():
                        # are in same "row" | "column" | "sub-block"
                        if k[0] == i or k[1] == j or (k[0] in block_i_set and k[1] in block_j_set):
                            domains_dict[k].discard(sudoku[i][j])

        min_remaining_val = None
        for domain in domains_dict.values():
            if min_remaining_val is not None:
                min_remaining_val = min(min_remaining_val, len(domain))
            else:
                min_remaining_val = len(domain)

        # sudoku can't be solved
        if min_remaining_val == 0:
            return None

        min_domains = {k: domains_dict[k]
                       for k in domains_dict.keys()
                       if len(domains_dict[k]) == min_remaining_val}

        return min_domains
