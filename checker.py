#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 18 16:30:17 2018

@author: shawn
"""

import simulatornxn as v1
import simNxN2 as v2
import numpy as np
import scipy as sp
import time
import timeit


### Make your own grid for testing
def make_grid():
    grid = np.zeros((5,5), dtype=np.int)

    return grid


def gen_moves(n):
    moves = np.random.permutation(n**2)
    x = np.array(moves % n,dtype=int)
    y = np.array(moves/n,dtype=int)
    #print(np.array(list(zip(x,y))))
    return zip(x,y)


def play_game(score,n,m):
    grid, moves = v1.init_grid(n), v1.generate_moves(n)
    turn = 0
    for move in moves:
        turn += 1
        grid = v1.play_move(grid,n,move,turn)

    return


def time_function(function,n):
    start = time.time()
    for i in range(0,n):
        function
    return time.time()-start
print(time_function(gen_moves(6),1000))



def check_single_game(seeds):
    trials = 1
    n = 3
    m = 3
    for seed in range(0,seeds):
        np.random.seed(seed)
        if not np.array_equal(v1.simulate(trials,n,m), v2.simulate(trials,n,m)):
            print(v1.simulate(trials,n,m))
            print(v2.simulate(trials,n,m))
            print(seed)
        return
    

grid = np.array(([ 0, -1,  1],[-1,  1, -1],[ 1,  0, -1]))
grid = np.array(list(zip(*reversed(grid))))
grid[grid == -1] = 0
grid = np.reshape(np.diag(grid),(1,3))
print(grid)
grid1 = np.ones((3,3),dtype=np.int)
print(grid1)
grid2 = np.diag(np.ones(3,dtype=np.int))
struc_row = np.ones((1,3),dtype=np.int)
struc_diag = np.diag(struc_row[0])
#outcome = v2.check_win(grid,3,1)
print(ndimage.binary_hit_or_miss(grid, struc_row).astype(np.int))


    
    
    
    
    
    
    
    
    
    
    
