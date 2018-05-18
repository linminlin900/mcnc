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

np.random.seed(0)

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
    ### Replaces the non player turn tokens with 0
    ### since the checking function operates on binary images
    grid = np.copy(grid_to_check)
    grid[grid == -player] = 0
    ### Checks for the structure (win positions) in the grid
    print(grid)
    ### Makes a 1D array with the diagonal elements
    grid_diag = np.reshape(np.diag(grid),(1,m))
    if np.any(ndimage.binary_hit_or_miss(grid, struc_row).astype(np.int)):
        return True
    if np.any(ndimage.binary_hit_or_miss(grid_diag, struc_row).astype(np.int)):
        return True
    
    ### Rotate grid clockwise by 90 deg and checks again
    grid = np.array(list(zip(*reversed(grid))))
    grid_diag = np.reshape(np.diag(grid),(1,m))
    if np.any(ndimage.binary_hit_or_miss(grid, struc_row).astype(np.int)):
        return True
    if np.any(ndimage.binary_hit_or_miss(grid_diag, struc_row).astype(np.int)):
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
                #print(grid)
                #print('detected')
                #print(turn) 
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

    try: 
        draw = occurences[turn==0][0]
    except:
        draw = 0
    p1_win = np.sum(occurences[turn%2==1])
    p2_win = np.sum(occurences[turn%2==0])- draw

 
    print('Games: ',trials)
    print('M,N: ', m,n)
    print('Draw: ',draw)
    print('P1 Win: ', p1_win)
    print('P2 Win: ', p2_win)
    print('Time taken v2:',time.time()-start)
    return np.array((p1_win,p2_win))
    
#print(make_grid())
#print(check_win(make_grid(),3))
#print(gen_moves(4))
np.random.seed(7)
print(simulate(500,3,3))

        
        
        
        
        
        
        
        
        