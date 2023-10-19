import time
import random

# Sample lists of integers for L
L = [
    [random.randint(1, 50) for _ in range(5)],
    [random.randint(1, 50) for _ in range(10)],
    [random.randint(1, 50) for _ in range(15)],
    [random.randint(1, 50) for _ in range(20)],
    [random.randint(1, 50) for _ in range(25)]
]

# Your bubble_sort and merge_sort functions should be defined above this

bubbletime, mergetime = [], []

for lst in L:
    # Bubble sort time
    bubblelist = lst.copy()
    start_time = time.time()
    bubble_sort(bubblelist)
    end_time = time.time()
    bubbletime.append(end_time - start_time)
    
    # Merge sort time
    mergelist = lst.copy()
    start_time = time.time()
    merge_sort(mergelist)
    end_time = time.time()
    mergetime.append(end_time - start_time)

# Rest of your code (like plotting) can follow here
