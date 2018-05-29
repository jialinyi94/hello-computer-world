"""
Programming Assignment 1: Count Inversions
Created on Tue May 29 13:15:47 2018

@author: jialinyi
"""


def MergeSplitInv(B, C):
    A = []
    B_copy, C_copy = B[:], C[:]
    counts = 0
    while len(B_copy) > 0 and len(C_copy) > 0:
        if B_copy[0] <= C_copy[0]:
            item = B_copy.pop(0)
        else:
            counts += len(B_copy)
            item = C_copy.pop(0)
        A.append(item)

    if not B_copy:
        return A + C_copy, counts
    else:
        return A + B_copy, counts


def MergeSortInvCount(A):
    if len(A) < 2:
        return A, 0
    else:
        index = int(len(A)/2)
        B = A[:index]
        C = A[index:]
        B_sorted, counts_b = MergeSortInvCount(B)
        C_sorted, counts_c = MergeSortInvCount(C)
        A_sorted, counts_split = MergeSplitInv(B_sorted, C_sorted)
    return A_sorted, counts_b + counts_c + counts_split


def main():
    text_file = open("IntegerArray.txt", "r")
    text_list = text_file.readlines()
    int_list = list(map(int, text_list))
    list_sorted, inversions = MergeSortInvCount(int_list)
    print("The inversions are", inversions)
if __name__ == '__main__':
    main()
