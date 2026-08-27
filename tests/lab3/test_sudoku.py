import unittest

from src.lab3.sudoku import (
    group,
    get_row,
    get_col,
    get_block,
    find_empty_positions,
    find_possible_values,
    solve,
    check_solution,
    generate_sudoku,
)

class SudokuTestCase(unittest.TestCase):
    def test_group(self):
        self.assertEqual(group([1, 2, 3, 4], 2), [[1, 2], [3, 4]])

    def test_get_row(self):
        grid = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
        self.assertEqual(get_row(grid, (1, 0)), ["4", "5", "6"])

    def test_get_col(self):
        grid = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
        self.assertEqual(get_col(grid, (0, 1)), ["2", "5", "8"])

    def test_get_block(self):
        grid = [["1", "2", "3", "4", "5", "6", "7", "8", "9"], ["4", "5", "6", "7", "8", "9", "1", "2", "3"], ["7", "8", "9", "1", "2", "3", "4", "5", "6"], ["2", "3", "4", "5", "6", "7", "8", "9", "1"], ["5", "6", "7", "8", "9", "1", "2", "3", "4"], ["8", "9", "1", "2", "3", "4", "5", "6", "7"], ["3", "4", "5", "6", "7", "8", "9", "1", "2"], ["6", "7", "8", "9", "1", "2", "3", "4", "5"], ["9", "1", "2", "3", "4", "5", "6", "7", "8"]]
        self.assertEqual(get_block(grid, (1, 1)), ["1", "2", "3", "4", "5", "6", "7", "8", "9"])

    def test_find_empty_positions(self):
        grid = [["1", "2", "."], ["4", "5", "6"], ["7", "8", "9"]]
        self.assertEqual(find_empty_positions(grid), (0, 2))

    def test_no_empty_positions(self):
        grid = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
        self.assertEqual(find_empty_positions(grid), None)

    def test_find_possible_values(self):
        grid = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
        self.assertEqual(find_possible_values(grid, (0, 2)), {"1", "2", "4"})

    def test_solve(self):
        grid = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
        solution = solve(grid)
        self.assertTrue(solution is not None)
        self.assertTrue(check_solution(solution))

    def test_check_solution(self):
        solution = [["5", "3", "4", "6", "7", "8", "9", "1", "2"], ["6", "7", "2", "1", "9", "5", "3", "4", "8"], ["1", "9", "8", "3", "4", "2", "5", "6", "7"], ["8", "5", "9", "7", "6", "1", "4", "2", "3"], ["4", "2", "6", "8", "5", "3", "7", "9", "1"], ["7", "1", "3", "9", "2", "4", "8", "5", "6"], ["9", "6", "1", "5", "3", "7", "2", "8", "4"], ["2", "8", "7", "4", "1", "9", "6", "3", "5"], ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]
        self.assertTrue(check_solution(solution))

    def test_bad_solution(self):
        solution = [["5", "5", "4", "6", "7", "8", "9", "1", "2"], ["6", "7", "2", "1", "9", "5", "3", "4", "8"], ["1", "9", "8", "3", "4", "2", "5", "6", "7"], ["8", "5", "9", "7", "6", "1", "4", "2", "3"], ["4", "2", "6", "8", "5", "3", "7", "9", "1"], ["7", "1", "3", "9", "2", "4", "8", "5", "6"], ["9", "6", "1", "5", "3", "7", "2", "8", "4"], ["2", "8", "7", "4", "1", "9", "6", "3", "5"], ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]
        self.assertFalse(check_solution(solution))
    
    def test_generate_sudoku(self):
        grid = generate_sudoku(40)
        empty_cnt = 0
        for row in grid:
            for value in row:
                if value == ".":
                    empty_cnt += 1
        self.assertEqual(empty_cnt, 41)
        
    def test_generate_full_sudoku(self):
        grid = generate_sudoku(1000)
        empty_cnt = 0
        for row in grid:
            for value in row:
                if value == ".":
                    empty_cnt += 1
        self.assertEqual(empty_cnt, 0)
        
        



