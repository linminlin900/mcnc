import numpy as np
import math
import random as rd
import time
import itertools

'''
"For a n x n x n grid with the following setup:

         ________________
        / 1 / 0 / 0 /-1 /|
       /___/___/___/___/ |      Crosses: 1 (starts first)
      /-1 / 1 / 0 / 1 /  |
     /___/___/___/___/   |      Naughts: -1
    / 0 /-1 / 1 /-1 /    |
   /___/___/___/___/     |      Blank: 0
  / 0 / 0 / 0 /-1 /      |
 /___/___/___/___/       |
|       |________|_______|
|       / 0 / 0 /|-1/ 0 /|
|      /___/___/_|_/___/ |
|     / 1 / 1 /-1|/ 1 /  |
|    /___/___/___|___/   |
|   / 0 /-1 /-1 /|0 /    |
|  /___/___/___/_|_/     |
| / 0 / 0 /-1 / 0|/      |
|/___/___/___/___|       |
|       |________|_______|
|       / 1 /-1 /|0 / 0 /|
|      /___/___/_|_/___/ |
|     / 1 / 1 /-1|/ 0 /  |
|    /___/___/___|___/   |
|   / 0 /-1 / 1 /|0 /    |
|  /___/___/___/_|_/     |
| / 0 / 0 / 0 / 1|/      |
|/___/___/___/___|       |
|       |________|_______|
|       /-1 / 0 /|0 / 0 /
|      /___/___/_|_/___/
|     / 1 / 1 / 1|/ 1 /
|    /___/___/___|___/
|   /-1 /-1 / 0 /|0 /
|  /___/___/___/_|_/
| /-1 / 0 / 0 / 1|/
|/___/___/___/___|

grid information will be stored as a n x n x n array.
Game is won when m crosses/naughts in a row are 
placed horizontally, vertically or diagonally 
'''


### Initialize a 3d n x n x n array of 0s
def init_grid(n=3):
    return np.zeros(((n, n, n)))

def generate_moves(n):
    return np.random.permutation(n**3)

def play_move(grid,n,move,turn):
    x = int(move % n**2 % n)
    y = int(move % n**2 / n)
    z = int(move/n**2)
    player = 2 * (turn % 2) - 1
    grid[x,y,z] += player
    return grid

### Rotates the given grid by 90 deg clockwise in direction 1
def rotate_grid1(grid):
    return np.rot90(grid,axes = (2, 1))


### Rotates the given grid by 90 deg clockwise in direction 2
def rotate_grid2(grid):
    return np.rot90(grid,axes = (0, 1))


### Rotates the given grid by 90 deg clockwise in direction 3
def rotate_grid3(grid):
    return np.rot90(grid,axes = (0, 2))


### Rotates the given grid by 90 deg clockwise in direction 4
def rotate_grid4(grid):
    return np.rot90(np.rot90(grid, 1, axes=(0, 1)), 1, axes=(2, 1))


### Rotates the given grid by 90 deg clockwise in direction 5
def rotate_grid5(grid):
    return np.rot90(np.rot90(grid, 1, axes=(0, 1)), 1, axes=(0, 2))



def check_rows(subgrid, m):
    col_sum = np.sum(subgrid, axis=0)
    col_sum = col_sum.reshape(m**2,)
    col_sum = set(col_sum)
    if m in col_sum:
        return 0
    if -m in col_sum:
        return 1
    trace = np.trace(subgrid)
    trace = set(trace)
    if trace == m:
        return 0
    elif trace == -m:
        return 1
    return 2

### Splits n x n grid into (n-m+1) x (n-m+1) x(n-m+1) of m x m subgrids,
### then checks win condition for each subgrid
def check_win(grid,n,m):
    for i,j,k in itertools.product(range(n-m+1),range(n-m+1),range(n-m+1)):
        subgrid = grid[0+i:m+i,0+j:m+j,0+k:m+k]
        outcome = check_rows(subgrid,m)
        if outcome != 2:
            return outcome
        outcome = check_rows(rotate_grid1(subgrid), m)
        if outcome != 2:
            return outcome
        outcome = check_rows(rotate_grid2(subgrid), m)
        if outcome != 2:
            return outcome
        outcome = check_rows(rotate_grid3(subgrid), m)
        if outcome != 2:
            return outcome
        outcome = check_rows(rotate_grid4(subgrid), m)
        if outcome != 2:
            return outcome
        outcome = check_rows(rotate_grid5(subgrid), m)
        if outcome != 2:
            return outcome
    return 2


def play_game(score, n, m):
    grid, moves = init_grid(n), generate_moves(n)
    turn = 0
    for move in moves:
        turn += 1
        grid = play_move(grid, n, move, turn)

        min_move = m * 2 - 1
        if turn > min_move:
            outcome = check_win(grid, n, m)
            if outcome != 2:
                score[outcome] += 1
                break
    return score


def main(trials, n, m):
    start = time.time()
    score = [0, 0]
    trial = 0
    for trial in range(0, trials):
        score = play_game(score, n, m)

    cross_score = score[0]
    naught_score = score[1]
    draw_score = trials - (cross_score + naught_score)
    time_taken = time.time() - start

    print("Games: ", trials)
    print("Cross: ", cross_score / trials)
    print("Naughts: ", naught_score / trials)
    print("Draws: ", draw_score / trials)
    print("Time taken: ", time_taken, "s")


main(20,6,4))