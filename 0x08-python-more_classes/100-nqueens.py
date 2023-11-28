#!/usr/bin/python3

import sys


def is_safe(board, row, col, n):

    for i in range(col):

        if board[i] == row or \
           board[i] == row - (col - i) or \
           board[i] == row + (col - i):

            return False

    return True


def solve_nqueens(board, col, n):
    if col == n:
        print_solution(board)
        return

    for row in range(n):

        if is_safe(board, row, col, n):
            board[col] = row
            solve_nqueens(board, col + 1, n)


def print_solution(board):

    solution = [[i, board[i]] for i in range(len(board))]
    print(solution)


def nqueens_solver(n):

    if not n.isdigit():

        print("N must be a number")
        sys.exit(1)

    n = int(n)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * n
    solve_nqueens(board, 0, n)


if __name__ == "__main__":

    if len(sys.argv) != 2:

        print("Usage: nqueens N")
        sys.exit(1)

    nqueens_solver(sys.argv[1])
