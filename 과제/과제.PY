# https://www.ploggingdev.com/2016/11/n-queens-solver-in-python-3/

import copy


def take_input(): # 입력을 받는 함수
    """Accepts the size of the chess board"""

    while True:
        try:
            size = int(input('What is the size of the chessboard? n = \n'))
            if size == 1: #체스판의 크기가 최소 4 여야 한다. 따라서 3이하의 수가 들어오면 재입력 받는다.
                print("Trivial solution, choose a board size of at least 4")
            if size <= 3:
                print("Enter a value such that size>=4")
                continue
            return size
        except ValueError:
            print("Invalid value entered. Enter again")


def get_board(size): #입력받은 크기를 이용해 n*n 크기의 체스판을 만든다.
    """Returns an n by n board"""
    board = [0] * size
    for ix in range(size):
        board[ix] = [0] * size
    return board


def print_solutions(solutions, size): #솔루션이라는 리스트를 받아 원소들을 배열에맞게 출력함 (이 출력은 경우의수를 그래픽화 한거임)
    """Prints all the solutions in user friendly way"""
    for sol in solutions:
        for row in sol:
            print(row)
        print()


def is_safe(board, row, col, size):
    """Check if it's safe to place a queen at board[x][y]"""

    # check row on left side
    for iy in range(col): #그 열의 퀸이 있다면, False 반환
        if board[row][iy] == 1:
            return False

    ix, iy = row, col
    while ix >= 0 and iy >= 0: #현위치에서 왼쪽위 대각선으로 체크하며 퀸이있다면 False반환
        if board[ix][iy] == 1:
            return False
        ix -= 1
        iy -= 1

    jx, jy = row, col
    while jx < size and jy >= 0: #현 위치에서 왼쪽 아래 대각선으로 체크하며 퀸이 있다면 False반환
        if board[jx][jy] == 1:
            return False
        jx += 1
        jy -= 1

    return True #퀸이 없다고 판단이 되면 True를 리턴에 안전하다고 알림


def solve(board, col, size): #
    """Use backtracking to find all solutions"""
    # base case
    if col >= size:# 문제 해결을 하면 끝나는거 
        return

    for i in range(size):
        if is_safe(board, i, col, size): #퀸을 놓을수 있는자리일때 퀸을 놓는다.
            board[i][col] = 1
            if col == size - 1: 마지막 행에 퀸을 놓았
                add_solution(board)
                board[i][col] = 0
                return
            solve(board, col + 1, size)
            # backtrack
            board[i][col] = 0


def add_solution(board):
    """Saves the board state to the global variable 'solutions'"""
    global solutions
    saved_board = copy.deepcopy(board)
    solutions.append(saved_board)


size = take_input()

board = get_board(size)

solutions = []

solve(board, 0, size)

print_solutions(solutions, size)

print("Total solutions = {}".format(len(solutions)))