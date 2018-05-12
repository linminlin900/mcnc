#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import scipy as sp
import math
import pandas as pd
import random as rd
import time

"""
Created on Fri May 11 18:58:46 2018

@author: shawn

For a 3 X 3 Grid with the following setup:

  a | b | c       Crosses: 1
 ---|---|---
  d | e | f       Naughts: 1
 ---|---|---
  g | h | i       Blank: 0

grid information will be stored as a 1 X 9 array.
Cross (1) will always start first

So, initial empty board state will look as such:
    
    [0,0,0,0,0,0,0,0,0]

and placing a cross in the centre (position e):
    
    [0,0,0,0,1,0,0,0,0]
This is not used
    
There are 8 possible win positions, represented by the array

    [R1 R2 R3 C1 C2 C3 D1 D2]
    
where R - row, C - Column, D - Diagonal, and
1,2,3 - row/column/diag number (D1 is a-e-j and D2 is c-e-h)
    
Each grid position will have an associated array showing its contribution to each of the win positions
"""

win_con = {'a':np.array([1,0,0,1,0,0,1,0]),
           'b':np.array([1,0,0,0,1,0,0,0]),
           'c':np.array([1,0,0,0,0,1,0,1]),
           'd':np.array([0,1,0,1,0,0,0,0]),
           'e':np.array([1,1,1,1,1,1,1,1]),
           'f':np.array([0,1,0,0,0,1,0,0]),
           'g':np.array([0,0,1,1,0,0,0,1]),
           'h':np.array([0,0,1,0,1,0,0,0]),
           'i':np.array([0,0,1,0,0,1,1,0])}




def init_grid(grid_size=8):
    grid = np.zeros(grid_size)
    return grid
    
    
def generate_moves(grid_size=3):
    coordinates = ['a','b','c','d','e','f','g','h','i']
    ''' This is to generate (x,y) coordinates
    for x in range(grid_size):
        for y in range(grid_size):
            coordinates.append((x,y))
    '''
    rd.shuffle(coordinates,rd.random)
    return coordinates


def check_win(grid_score):
    # checks if the score reaches 3 (cross wins) or -3 (naughts wins) 
    # else no result
    if np.amax(grid_score) == 3:
        return 0
    if np.amin(grid_score) == -3:
        return 1
    else: 
        return 2
    

    
def simulate(trials):
    start = time.time()
    n = 0
    score = np.array([0,0])
    ## score keeps the win ratio [crosses,naughts]
    for n in range(0, trials):
        print(100*n/trials,"%")
        grid_score = init_grid()
        moves = generate_moves()
        turn = 0
        # print(moves)
        for move in moves:
            turn += 1
            # print(move)
            if turn % 2 == 1:
                grid_score = np.add(grid_score,win_con[move])
            else:
                grid_score = np.subtract(grid_score,win_con[move])
            # print(grid_score)
            if turn>4:
                outcome = check_win(grid_score)
                if outcome != 2:
                    score[outcome] += 1
                    #print(score)
                    break
    cross_score = score[0]
    naught_score = score[1]
    draw_score = trials - (cross_score + naught_score)
    time_taken = time.time() - start
    
    print("Games: ", trials)
    print("Cross: ",cross_score)
    print("Naughts: ", naught_score)
    print("Draws: ", draw_score)
    print("Time taken: ", time_taken, "s")
            
            
simulate(5000)






















