import sys

sys.setrecursionlimit(5000)

def recursion(condicion):
    if condicion == 0:
        return True
    else:
        return recursion(condicion -1)
recursion(5)