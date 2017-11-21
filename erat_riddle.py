#!/usr/bin/env python2
import sys
N=37
M=23
L=59
K=271

def pretty_string(*args):
    result=""
    for arg in args:
        if arg in ["+","="]:
            arg = " "+arg+" "
        result += str(arg)
    return result

def riddle(x,y,z,t,summ):
    i = 0 
    for xi in range(1000/x):
        for yi in range(1000/y):
           for zi in range(1000/z):
               for ti in range(1000/t):
                   if (x*xi + y*yi + z*zi + t*ti) == summ:
                       print pretty_string(x,"x",xi,"+",y,"x",yi,"+",z,"x",zi,"+",t,"x",ti,"=",summ)
                       i += 1
    if i == 0:
        print "No solution"

if __name__ == "__main__":
    if len(sys.argv) == 2:
        riddle(N,M,L,K,int(sys.argv[1]))
        exit(0)
    if len(sys.argv) == 6:
        riddle(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]))
        exit(0)
    print "you need to enter summ or all 4 weights and summ"       
