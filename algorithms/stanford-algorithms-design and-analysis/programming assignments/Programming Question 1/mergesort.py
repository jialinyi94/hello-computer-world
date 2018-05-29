"""
Core algorithm: MergeSort
Created on Tue May 29 12:19:47 2018

@author: jialinyi
"""


def MergeArray(B, C):
    A = []
    B_copy, C_copy = B[:], C[:]

    while len(B_copy) > 0 and len(C_copy) > 0:
        if B_copy[0] <= C_copy[0]:
            item = B_copy.pop(0)
        else:
            item = C_copy.pop(0)
        A.append(item)

    if not B_copy:
        return A + C_copy
    else:
        return A + B_copy


def MergeSort(A):
    if len(A) < 2:
        return A
    else:
        index = int(len(A)/2)
        B = A[:index]
        C = A[index:]
        B_sorted = MergeSort(B)
        C_sorted = MergeSort(C)
        A_sorted = MergeArray(B_sorted, C_sorted)
    return A_sorted


if __name__ == '__main__':
    import numpy as np
    A = np.random.randn(200)
    A = np.ndarray.tolist(A)
    A_sorted = MergeSort(A)
    A.sort()
    print(A_sorted == A)
