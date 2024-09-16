#!/usr/bin/python3
import sys

def print_usage_and_exit():
    print("Usage: nqueens N")
    sys.exit(1)

def print_number_error_and_exit():
    print("N must be a number")
    sys.exit(1)

def print_minimum_error_and_exit():
    print("N must be at least 4")
    sys.exit(1)

if len(sys.argv) != 2:
    print_usage_and_exit()

try:
    N = int(sys.argv[1])
except ValueError:
    print_number_error_and_exit()

if N < 4:
    print_minimum_error_and_exit()

def is_safe(board, row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False
    return True

def solve_nqueens(board, row, solutions):
    if row == len(board):
        solution = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return
    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1
            solve_nqueens(board, row + 1, solutions)
            board[row][col] = 0

def nqueens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens(board, 0, solutions)
    return solutions

solutions = nqueens(N)
for solution in solutions:
    print(solution)

