# -*- coding: utf-8 -*-

def linear_search(A, n, v):
    k = 0
    while k < n:
        if A[k] == v:
            return "Found"
        k = k+1
    return "Not found"

def sentinel_linear_search(A, n, v):
    A.append(v)
    k = 0
    while A[k] != v:
        k = k+1
    if k < n:
        return "Found"
    return "Not found"

def binary_search(A, n, v):
    a = 0
    b = n

    while a<b:
        k = int((a+b)/2)

        if A[k] == v:
            return "Found"
        elif A[k] < v:
            a = k+1
        else:
            b = k-1
    
    return "Not found"

if __name__ == '__main__':
    # linear series
    #A=[31,41,59,26,53]
    #print(sentinel_linear_search(A, 5, 26))

    # Binary series
    A = [26,31,41,53,77,89,93,97]
    print( binary_search(A, 8, 77) )