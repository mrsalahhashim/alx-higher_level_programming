#!/usr/bin/python3
def is_safe(board, row, col, N):
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, col, N):
    if col >= N:
        return True

    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            if solve_n_queens(board, col + 1, N):
                print_solution(board)
            board[i][col] = 0  # Backtrack

    return False

def print_solution(board):
    solution = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)

def main(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    if not solve_n_queens(board, 0, N):
        print("No solution exists")

if __name__ == "__main__":
    # Check for command-line arguments and their validity
    # If valid, call main(N) with the appropriate N