# https://www.ploggingdev.com/2016/11/n-queens-solver-in-python-3/

import copy
import queue

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
            if col == size - 1: #모든 퀸을 다 놓으면 함수를 끝낸다.
                add_solution(board) #함수를 끝내기전에 답을 출력하는 함수에 저장을 해준다.
                board[i][col] = 0
                return
            solve(board, col + 1, size) #재귀를 이용해 다음 행에 퀸을 놓을 방법을 찾는다.
            # backtrack
            board[i][col] = 0


def add_solution(board): #답을 추가해주는 함수, 추가한답을 출력해야함
    """Saves the board state to the global variable 'solutions'"""
    global solutions
    saved_board = copy.deepcopy(board)
    solutions.append(saved_board)


def bfs_solve(size):
    q=queue.Queue()  ##queue 객체를 생성 합니다.
    for i in range(size): ## 처음에 size만큼 queue 객체에 삽입합니다.
        a=[]
        a.append(i)
        q.put(a)
    while(q.empty()==False): ## queue 객체가 빌때까지 반복합니다.
        original_get=q.get()  ## get 메소드를 사용해서 queue객체에서 제일 먼저 들어간 값을 가져옵니다.
        if len(original_get)==size: ## 받아온 값으로 퀸을 전부 배열할 수 있으면, 그에 맞는 체스판을 만들고 add_solution 메소드로 정답을 추가합니다.
            board=get_board(size)
            for i in range(size):
                board[original_get[i]][i]=1
            add_solution(board)
            continue

        ##받아온 값으로 체스판을 다 만들지 못했을떄 체스판을 완성하기 위한 코드

        copy_get=copy.deepcopy(original_get) # 받아온 값을 여러번 이용하기위해 deepcopy메소드를 사용하여 copy합니다. *주의* 그냥 "="으로 복사하면 값이 변할떄마다 따라서 변함
        board=get_board(size)
        for i in range(len(copy_get)):##받아온 값으로 체스판을 만듧니다.
            board[copy_get[i]][i]=1
        for i in range(size):
            if is_safe(board,i,len(copy_get),size): ## 체스판을 만들수 있다면, 
                original_get=copy.deepcopy(copy_get) ## 아까 복사해둔 값으로 재복사해서 
                original_get.append(i) ##그 값에 체스판을 조금더 완성시킨후 
                q.put(original_get)## queue 객체에 push합니다.
               
    return 





        
    

                



size = take_input()

solutions = []

bfs_solve(size)

print_solutions(solutions, size)

print("Total solutions = {}".format(len(solutions)))
