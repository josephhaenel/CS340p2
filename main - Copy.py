import matplotlib.pyplot as plt
import numpy as np
import time
import os

infinity = 'zzzzzzzzzz'
heapSize = 0

# Number of files to iterate through in each folder (10 files in Perm and 10 in Sorted)
numFiles = 10


# Insertion Sort
def insertionSort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j

        while i > 0 and A[i - 1] > key:
            A[i] = A[i - 1]
            # if i != 0:
            i = i - 1
        A[i] = key
# End of Insertion Sort

# Merge Sort


def mergeSort(Array, start, end):
    if start < end:
        mid = int(((start + (end)) / 2))
        mergeSort(Array, start, mid)
        mergeSort(Array, mid + 1, end)
        merge(Array, start, mid, end)


def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q

    L = [''] * n1
    R = [''] * n2
    for i in range(0, n1):
        L[i] = A[p + i]
    for j in range(0, n2):
        R[j] = A[q + j + 1]
    L.append(infinity)
    R.append(infinity)
    i = 0
    j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1
# End of Merge Sort

# Heap Sort


def buildMaxHeap(A):
    heapSize = len(A)
    for i in range(int((len(A) / 2) - 1), -1, -1):
        maxHeapify(A, i, heapSize)


def heapSort(A):
    heapSize = len(A)
    buildMaxHeap(A)
    for i in range(len(A) - 1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heapSize -= 1
        maxHeapify(A, 0, heapSize)


def maxHeapify(A, i, heapSize):
    l = 2 * i + 1
    r = 2 * i + 2
    if l < heapSize and A[l] > A[i]:
        largest = l
    else:
        largest = i
    if r < heapSize and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        maxHeapify(A, largest, heapSize)
# End of Heap Sort

# Main function


def main():
    for t in range(2):  # For loop to enter PERM and SORTED

        # If statements to enter PERM or SORTED depending on t variable
        if t == 0:
            sortList = "PERM"
            sortFileType = "perm"
            sortOutFile = 'PERM_OUT'
        elif t == 1:
            sortList = "SORTED"
            sortFileType = "sorted"
            sortOutFile = 'SORT_OUT'
        for j in range(3):
            if j == 0:
                sortType = 'IS'
            elif j == 1:
                sortType = 'MS'
            elif j == 2:
                sortType = 'HS'

            # X and Y lists for graphing purposes
            x1 = [0]
            y1 = [0]

            # File size
            fileSize = 0

            for i in range(numFiles):
                fileSize += 15  # Adding 15 to file size each loop
                # Setting file name to search for
                fileName = sortFileType + str(fileSize) + 'K.txt'

                fileDestination = os.path.join(
                    *[os.path.dirname(__file__), 'wordlists', sortList, fileName])  # Getting file location using current file system location depending on OS

                try:

                    # Reading from Files

                    # Opening file to read in
                    fileObject = open(fileDestination, "r")

                    word_list = fileObject.readlines()  # Reading in lines from file

                    fileObject.close()  # Closing file

                    start_time = time.time()  # Getting start time for graphing purposes

                    # Doing different sorts depending on loop variable j
                    if j == 0:
                        insertionSort(word_list)
                    elif j == 1:
                        n = len(word_list) - 1
                        mergeSort(word_list, 0, n)
                    elif j == 2:
                        heapSort(word_list)

                    end_time = time.time()  # Getting end time for graphing purposes

                    # Appending x and y variables to list for graphing purposes
                    x1.append(fileSize)
                    y1.append(end_time - start_time)

                    # Writing to Files

                    fileName = sortType + str(fileSize) + 'K.txt'

                    fileDestination = os.path.join(
                        *[os.path.dirname(__file__), 'wordlists', sortOutFile, fileName])

                    fileObject = open(fileDestination, 'w')

                    for line in word_list:
                        fileObject.writelines(line)

                    fileObject.close()

                # If file failed to open (path not found) output...
                except IOError:
                    print(fileName + ' failed to open')

            if j == 0:
                plt.plot(x1, y1, label="Insertion Sort")
            elif j == 1:
                plt.plot(x1, y1, label="Merge Sort")
            elif j == 2:
                plt.plot(x1, y1, label="Heap Sort")

        plt.rcParams['figure.figsize'] = [10, 6]  # Setting size of plot
        plt.rcParams["figure.autolayout"] = True

        plt.xlabel('Words Sorted (thousands)')  # Graph x Label
        plt.ylabel('Time Taken (seconds)')  # Graph Y Label
        if t == 0:
            plt.title("Permuted Sorting Time")
        elif t == 1:
            plt.title("Sorted Sorting Time")
        plt.legend()
        plt.show()


if __name__ == '__main__':
    main()
