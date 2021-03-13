import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def sumup(i, j, arr) :
    total = []
    stop = j + 3
    #print("i & j : " + str(i) + str(j))
    while j < stop :
        total.append(arr[i][j])
        total.append(arr[i + 2][j])
        if j == stop - 2 :
            total.append(arr[i + 1][j])
        j += 1
    return sum(total)

def hourglassSum(arr):
    res = 0
    i = 0
    stop = len(arr[0]) - 2
    grt = -sys.maxint - 1
    while i < stop :
        j = 0
        while j < stop :
            hold = sumup(i, j, arr)
            if grt < hold :
                grt = hold
            j += 1
        i += 1
    return grt
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in xrange(6):
        arr.append(map(int, raw_input().rstrip().split()))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
