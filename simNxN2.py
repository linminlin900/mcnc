#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 00:20:33 2018

@author: shawn
"""
import time
import numpy as np
import scipy as sp
from scipy import ndimage


### Make your own grid for testing
def make_grid():
    grid = np.zeros((5,5), dtype=np.int)
    grid[0,1:4] = 1
    return grid


### Creates a grid of n dimensions
def init_grid(n):
    return np.zeros((n,n), dtype=np.int)


### Generates randomised iterable coordinates with every point
def gen_moves(n):
    moves = np.random.permutation(n**2)
    x = np.array(moves % n,dtype=int)
    y = np.array(moves/n,dtype=int)
    #print(np.array(list(zip(x,y))))
    return zip(x,y)


### Checks if the grid has any winning positions
def check_win(grid_to_check, m,player):
    ### Creates structure elements to check against
    struc_row = np.ones((1,m),dtype=np.int)
    struc_diag = np.diag(struc_row[0])
    ### Replaces the non player turn tokens with 0
    ### since the checking function operates on binary images
    grid = np.copy(grid_to_check)
    grid[grid == -player] = 0
    #print(grid)
    ### Checks for the structure (win positions) in the grid
    if np.any(ndimage.binary_hit_or_miss(grid, struc_row).astype(np.int)):
        return True
    if np.any(ndimage.binary_hit_or_miss(grid, struc_diag).astype(np.int)):
        return True
    
    ### Rotate grid clockwise by 90 deg and checks again
    grid = np.array(list(zip(*reversed(grid))))
    if np.any(ndimage.binary_hit_or_miss(grid, struc_row).astype(np.int)):
        return True
    if np.any(ndimage.binary_hit_or_miss(grid, struc_diag).astype(np.int)):
        return True
    return False


### Given n and m, plays a random game and returns the turn in which
### game is won. 0 is for draws
def play_game(n,m):
    grid,moves = init_grid(n),gen_moves(n)
    turn = 0
    min_move = 2*m-1
    for move in moves:
        turn += 1
        #print(turn)
        player = 2*(turn % 2) - 1
        grid[move[0],move[1]] = player
        #print(grid)

        if turn > min_move:
            if check_win(grid,m,player):
                #print('detected')
                return turn
    return 0

### Main function
def simulate(trials,n,m):
    start = time.time()
    score = np.array((),dtype=np.int)
    for trial in range(0,trials):
        ### Adds the turn in which game is won
        score = np.append(score,[play_game(n,m)])
    
    turn,occurences = np.unique(score,return_counts=True)
    result = np.array(list(zip(turn,occurences)))
    
    draw = occurences[turn==0][0]
    p1_win = np.sum(occurences[turn%2==1])
    p2_win = np.sum(occurences[turn%2==0])- draw
    
    print('Games: ',trials)
    print('M,N: ', m,n)
    print('Draw: ',draw)
    print('P1 Win: ', p1_win)
    print('P2 Win: ', p2_win)
    print('Time taken v2:',time.time()-start)
    return result
    
#print(make_grid())
#print(check_win(make_grid(),3))
#print(gen_moves(4))
simulate(1000,8,5)

        
        
        
        
        
        
        
        
        