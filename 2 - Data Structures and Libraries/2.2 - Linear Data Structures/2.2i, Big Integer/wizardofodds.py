import sys
from math import *
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))

[N, K] = inlt()
if K >= log2(N): print("Your wish is granted!")
else: print("You will become a flying monkey!")