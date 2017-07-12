# -*- coding: utf-8 -*-

def bubble_sort(A,n):
    m=n

    while m>1:
        k=0
        while k<m-1:
            if A[k]>A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]
            k=k+1
        m=m-1
    return A

if __name__ == '__main__':
    A=[53, 89, 41, 31, 26]
    print(bubble_sort(A, 5))
