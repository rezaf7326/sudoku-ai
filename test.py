import json
from algorithm import BacktrackingSudoku


puzzle_1 = {
    "sudoku": [
        [1, 0, 4, 8, 6, 5, 2, 3, 7],
        [7, 0, 5, 4, 1, 2, 9, 6, 8],
        [8, 0, 2, 3, 9, 7, 1, 4, 5],
        [9, 0, 1, 7, 4, 8, 3, 5, 6],
        [6, 0, 8, 5, 3, 1, 4, 2, 9],
        [4, 0, 3, 9, 2, 6, 8, 7, 1],
        [3, 0, 9, 6, 5, 4, 7, 1, 2],
        [2, 0, 6, 1, 7, 9, 5, 8, 3],
        [5, 0, 7, 2, 8, 3, 6, 9, 4]
    ]
}

puzzle_2 = {
    "sudoku": [
        [0, 0, 4, 7, 2, 0, 9, 0, 0],
        [0, 3, 9, 0, 0, 8, 0, 0, 5],
        [0, 0, 1, 5, 0, 6, 0, 0, 4],
        [0, 4, 0, 0, 1, 0, 5, 2, 0],
        [0, 2, 8, 0, 5, 0, 1, 7, 0],
        [0, 1, 6, 0, 3, 0, 0, 9, 0],
        [4, 0, 0, 9, 0, 1, 3, 0, 0],
        [1, 0, 0, 3, 0, 0, 8, 4, 0],
        [0, 0, 7, 0, 8, 5, 6, 0, 0]
    ]
}


def test(puzzle_json_str):
    obj = json.loads(puzzle_json_str)
    backtracking = BacktrackingSudoku(obj.get("sudoku"))
    backtracking.search()

    print('puzzle search result:')
    for row in backtracking.get_result():
        print(str(row))


test(json.dumps(puzzle_1))
test(json.dumps(puzzle_2))
