"""
Advent of Code Day 1 Part 1
"""      

# read the input text file of the given data
with open('day1\input.txt', 'r') as f:
    lines = f.readlines()
    # read each line and store in an array named data
    data = [int(entry.strip()) for entry in lines]


# set the first value, and set the count to be 0
first_val = data[0]
count = 0
# iterate in the entire list and check each value
# increase the counter by one if it satisfy the criteria
for entry in data[1:]:
    if entry > first_val:
        count += 1
    first_val = entry



print("Solution of Part 1 is",count)



"""
Advent of Code Part 2 
"""

import numpy as np

sliding_windows = np.convolve(data, np.ones(3), 'valid')

first_val = sliding_windows[0]
count2 = 0
for entry in sliding_windows[1:]:
    if entry > first_val:
        count2 += 1
    first_val = entry

print("The measurement",count2) 

