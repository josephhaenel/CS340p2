import matplotlib.pyplot as plt
import numpy as np
import time
import os
import BST
import RB

selectedFile = ''
numFiles = 0
treeType = 'BST'

# Required Outputs:
# (i)   whether or not the word was found in the file
# (ii)  the time taken to construct the dictionary from the selected data structure on the selected file
# (iii) the time taken to execute the user’s search query on the selected data structure on that file


def main():

    # Getting Tree Type
    while True:
        # Get the tree type
        treeType = input('Select tree type (BST/R-B/BOTH): ')
        treeType = treeType.upper()  # Capitalize input to remove case sensitivity
        if treeType != 'BST' and treeType != 'R-B' and treeType != 'BOTH':  # Tree type is invalid
            print('Invalid tree type, please select either BST, R-B, or BOTH.')
        else:
            break  # Tree Type is valid

    # Getting selected file type
    while True:
        # Get the file name
        selectedFile = input('Select The File (PERM/SORTED/BOTH/OTHER): ')
        # Capitalize input to remove case sensitivity
        selectedFile = selectedFile.upper()
        if selectedFile != 'PERM' and selectedFile != 'SORTED' and selectedFile != 'BOTH' and selectedFile != 'OTHER':  # File type is invalid
            print('Invalid file, please select either PERM, SORTED, BOTH, or OTHER.')
        else:
            break  # File type is valid

    if selectedFile == 'BOTH':
        print('\n*** Selected file will be for both files ***\n')

    fileName = ''
    if selectedFile == 'OTHER':
        while (True):  # Get file name
            fileName = input(
                'Enter file name or path from "\CS340_P2": ')
            try:
                fileDestination = os.path.join(
                    *[os.path.dirname(__file__), fileName])  # Getting file destination

                # Atempting to open file
                fileObject = open(fileDestination, 'r')

                fileObject.close()

                break
            except IOError:  # File failed to be opened
                print(
                    "Could NOT open file, please make sure the file is in CS340_P2 and is spelled correctly")

    # Get the file from PERM or SORTED to add
    if selectedFile == 'PERM' or selectedFile == 'SORTED' or selectedFile == 'BOTH':
        while True:
            # Get the number of files
            numFiles = int(
                input('Input the number of file you wish to look at (1-10): '))
            allowedNums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Valid numbers
            if numFiles not in allowedNums:  # Invalid number of files
                print('Invalid number of files, please select a number 1-10.')
            else:
                break  # Number of files is valid

    for i in range(2):  # Loop for BST and R-B Tree Posibilities
        if i == 0 and (treeType == 'BST' or treeType == 'BOTH'):  # Do BST Stuff
            if selectedFile == 'OTHER':  # Different file
                try:
                    fileDestination = os.path.join(
                        *[os.path.dirname(__file__), fileName])  # Getting file destination

                    # Atempting to open file
                    fileObject = open(fileDestination, 'r')

                    wordList = fileObject.readlines()  # Reading in lines from file

                    fileObject.close()  # Closing file

                    startTime = time.time()  # Getting start time

                    BST.myTree = BST.Tree()

                    for word in wordList:
                        BST.myTree.treeInsert(BST.Node(word.strip()))

                    endTime = time.time()

                    totalTime = startTime - endTime

                    print("Time taken to construct BST from",
                          fileName, ":", totalTime)
                    searchVal = '0'

                    while (True):
                        choice = input(
                            '''
    ---------- Menu ----------
    | 1 : Search             |
    | 2 : InOrderTraversal   |
    | 3 : PrintParentKey     |
    | 4 : PrintLeftChild     |
    | 5 : PrintRightChild    |
    | 6 : PrintPathToRoot    |
    | 7 : Exit               |
    --------------------------
    ''')
                        match choice:
                            case '1':
                                while True:
                                    searchVal = input(
                                        'Input a word to search for in tree (-1 to exit, CASE SENSITIVE): ')
                                    if searchVal == '-1':
                                        break
                                    startTime = time.time()
                                    found = BST.myTree.search(
                                        BST.myTree.root, searchVal)
                                    endTime = time.time()
                                    totalTime = endTime - startTime

                                    if found != None:
                                        print(searchVal, 'was found in the tree in',
                                              totalTime, 'seconds')
                                    else:
                                        print(searchVal, 'was NOT found in the tree in',
                                              totalTime, 'seconds')
                            case '2':
                                val = BST.myTree.inOrderTraversal(
                                    BST.myTree.root)
                                fileOut = open('BSTTraversal.txt', 'w')
                                for line in val:
                                    fileOut.writelines(line + '\n')

                                fileOut.close()
                            case '3':
                                val = input(
                                    'Enter a key to print the parent key of: ')
                                BST.myTree.printParentKey(val)
                            case '4':
                                val = input(
                                    'Enter a key to print the left child of: ')
                                BST.myTree.printLeftChild(val)
                            case '5':
                                val = input(
                                    'Enter a key to print the right child of: ')
                                BST.myTree.printRightChild(val)
                            case '6':
                                val = input(
                                    'Enter a key to print the path to root of: ')
                                BST.myTree.printPathToRoot(val)
                            case '7':
                                break

                    break

                except IOError:  # File failed to be opened
                    print(
                        "Could NOT open file, please make sure the file is in CS340_P2 and is spelled correctly")

            for j in range(2):  # Loop for PERM and SORTED possibilities
                # Set PERM BST Values
                if j == 0 and (selectedFile == 'PERM' or selectedFile == 'BOTH'):
                    fileType = 'perm'
                    fileSize = 15
                # Set SORTED BST Values
                elif j == 1 and (selectedFile == 'SORTED' or selectedFile == 'BOTH'):
                    fileType = 'sorted'
                    fileSize = 15
                else:
                    continue
                for k in range(numFiles - 1):  # num of files to iterate over
                    fileSize += 15

                fileDestination = os.path.join(
                    *[os.path.dirname(__file__), 'wordlist', fileType, fileType + str(fileSize) + 'K.txt'])

                try:
                    # Reading from files
                    fileObject = open(fileDestination, "r")  # Open file

                    wordList = fileObject.readlines()  # Read in word from file

                    fileObject.close()  # Close the file

                    startTime = time.time()

                    BST.myTree = BST.Tree()

                    for word in wordList:
                        BST.myTree.treeInsert(BST.Node(word.strip()))

                    endTime = time.time()

                    totalTime = endTime - startTime

                    print('Time taken to construct BST tree with', numFiles * 15, 'k words',
                          'from', fileType, ':', totalTime)  # Printing time taken for construction

                    searchVal = '0'

                    while (True):
                        choice = input(
                            '''
    ---------- Menu ----------
    | 1 : Search             |
    | 2 : InOrderTraversal   |
    | 3 : PrintParentKey     |
    | 4 : PrintLeftChild     |
    | 5 : PrintRightChild    |
    | 6 : PrintPathToRoot    |
    | 7 : Exit               |
    --------------------------
    ''')
                        match choice:
                            case '1':
                                while True:
                                    searchVal = input(
                                        'Input a word to search for in tree (-1 to exit): ').upper()
                                    if searchVal == '-1':
                                        break
                                    startTime = time.time()
                                    found = BST.myTree.search(
                                        BST.myTree.root, searchVal)
                                    endTime = time.time()
                                    totalTime = endTime - startTime

                                    if found != None:
                                        print(searchVal, 'was found in the tree in',
                                              totalTime, 'seconds')
                                    else:
                                        print(searchVal, 'was NOT found in the tree in',
                                              totalTime, 'seconds')
                            case '2':
                                val = BST.myTree.inOrderTraversal(
                                    BST.myTree.root)
                                fileOut = open('BSTTraversal.txt', 'w')
                                for line in val:
                                    fileOut.writelines(line + '\n')

                                fileOut.close()
                                print(
                                    '\nIn order traversal outputted to BSTTraversal.txt')

                            case '3':
                                val = input(
                                    'Enter a key to print the parent key of: ')
                                BST.myTree.printParentKey(val)
                            case '4':
                                val = input(
                                    'Enter a key to print the left child of: ')
                                BST.myTree.printLeftChild(val)
                            case '5':
                                val = input(
                                    'Enter a key to print the right child of: ')
                                BST.myTree.printRightChild(val)
                            case '6':
                                val = input(
                                    'Enter a key to print the path to root of: ')
                                BST.myTree.printPathToRoot(val)
                            case '7':
                                break
                            case _:
                                print('\n*** Invalid selection, try again. ***')

                except IOError:
                    print(fileDestination + ' failed to open')

        # Do R-B Stuff ---------------------------=========================
        if i == 1 and (treeType == 'R-B' or treeType == 'BOTH'):
            if selectedFile == 'OTHER':  # Different file
                try:
                    fileDestination = os.path.join(
                        *[os.path.dirname(__file__), fileName])  # Getting file destination

                    # Atempting to open file
                    fileObject = open(fileDestination, 'r')

                    wordList = fileObject.readlines()  # Reading in lines from file

                    fileObject.close()  # Closing file

                    startTime = time.time()  # Getting start time

                    RB.myTree = RB.RedBlackTree()

                    for word in wordList:
                        RB.myTree.RBInsert(RB.Node(word.strip()))

                    endTime = time.time()

                    totalTime = startTime - endTime

                    print("Time taken to construct R-B from",
                          fileName, ":", totalTime)
                    searchVal = '0'

                    while (True):
                        choice = input(
                            '''
    ---------- Menu ----------
    | 1 : Search             |
    | 2 : InOrderTraversal   |
    | 3 : PrintParentKey     |
    | 4 : PrintLeftChild     |
    | 5 : PrintRightChild    |
    | 6 : PrintPathToRoot    |
    | 7 : PrintColor         |
    | 8 : PrintParentColor   |
    | 9 : PrintUncleColor    |
    | 10: PrintDepth         |
    | 11: Exit               |
    --------------------------
    ''')
                        match choice:
                            case '1':
                                while True:
                                    searchVal = input(
                                        'Input a word to search for in tree (-1 to exit, CASE SENSITIVE): ')
                                    if searchVal == '-1':
                                        break
                                    startTime = time.time()
                                    found = RB.myTree.RBSearch(searchVal)
                                    endTime = time.time()
                                    totalTime = endTime - startTime

                                    if found != None:
                                        print(searchVal, 'was found in the tree in',
                                              totalTime, 'seconds')
                                    else:
                                        print(searchVal, 'was NOT found in the tree in',
                                              totalTime, 'seconds')
                            case '2':
                                val = RB.myTree.InOrderTreeTraversal(
                                    RB.myTree.root)
                                fileOut = open('RBTraversal.txt', 'w')
                                for line in val:
                                    fileOut.writelines(line + '\n')

                                fileOut.close()

                                print(
                                    '\nIn order tree traversal outputted to RBTraversal.txt')
                            case '3':
                                val = input(
                                    'Enter a key to print the parent key of: ')
                                RB.myTree.PrintParentKey(val)
                            case '4':
                                val = input(
                                    'Enter a key to print the left child of: ')
                                RB.myTree.PrintLeftChild(val)
                            case '5':
                                val = input(
                                    'Enter a key to print the right child of: ')
                                RB.myTree.PrintRightChild(val)
                            case '6':
                                val = input(
                                    'Enter a key to print the path to root of: ')
                                RB.myTree.PrintPathToRoot(val)
                            case '7':
                                val = input(
                                    'Enter a key to print the color of: ')
                                RB.myTree.PrintColor(val)
                            case '8':
                                val = input(
                                    'Enter a key to print the parents color of: ')
                                RB.myTree.PrintParentColor(val)
                            case '9':
                                val = input(
                                    'Enter a key to print uncle color of: ')
                                RB.myTree.PrintUncleColor(val)
                            case '10':
                                val = input(
                                    'Enter a key to print the depth of: ')
                                if val is not None:
                                    RB.myTree.PrintDepth(val)
                                else:
                                    RB.myTree.PrintDepth()
                            case '11':
                                break
                            case _:
                                print('*** Invalid input, please try again. ***')

                except IOError:  # File failed to be opened
                    print(
                        "Could NOT open file, please make sure the file is in CS340_P2 and is spelled correctly")

            for j in range(2):  # Loop for PERM and SORTED possibilities
                # Set PERM RB Values
                if j == 0 and (selectedFile == 'PERM' or selectedFile == 'BOTH'):
                    fileType = 'perm'
                    fileSize = 15
                # Set SORTED RB Values
                elif j == 1 and (selectedFile == 'SORTED' or selectedFile == 'BOTH'):
                    fileType = 'sorted'
                    fileSize = 15
                else:
                    continue
                for k in range(numFiles - 1):  # num of files to iterate over
                    fileSize += 15

                fileDestination = os.path.join(
                    *[os.path.dirname(__file__), 'wordlist', fileType, fileType + str(fileSize) + 'K.txt'])

                try:
                    # Reading from files
                    fileObject = open(fileDestination, "r")  # Open file

                    wordList = fileObject.readlines()  # Read in word from file

                    fileObject.close()  # Close the file

                    startTime = time.time()

                    RB.myTree = RB.RedBlackTree()

                    for word in wordList:
                        RB.myTree.RBInsert(RB.Node(word.strip()))

                    endTime = time.time()

                    totalTime = endTime - startTime

                    print('Time taken to construct R-B tree with', numFiles * 15, 'k words',
                          'from', fileType, ':', totalTime)  # Printing time taken for construction

                    searchVal = '0'

                    while (True):
                        choice = input(
                            '''
    ---------- Menu ----------
    | 1 : Search             |
    | 2 : InOrderTraversal   |
    | 3 : PrintParentKey     |
    | 4 : PrintLeftChild     |
    | 5 : PrintRightChild    |
    | 6 : PrintPathToRoot    |
    | 7 : PrintColor         |
    | 8 : PrintParentColor   |
    | 9 : PrintUncleColor    |
    | 10: PrintDepth         |
    | 11: Exit               |
    --------------------------
    ''')
                        match choice:
                            case '1':
                                while True:
                                    searchVal = input(
                                        'Input a word to search for in tree (-1 to exit, CASE SENSITIVE): ')
                                    if searchVal == '-1':
                                        break
                                    startTime = time.time()
                                    found = RB.myTree.RBSearch(searchVal)
                                    endTime = time.time()
                                    totalTime = endTime - startTime

                                    if found != None:
                                        print(searchVal, 'was found in the tree in',
                                              totalTime, 'seconds')
                                    else:
                                        print(searchVal, 'was NOT found in the tree in',
                                              totalTime, 'seconds')
                            case '2':
                                val = RB.myTree.InOrderTreeTraversal(
                                    RB.myTree.root)
                                if j == 0:
                                    fileOut = open('PERM_RBTraversal.txt', 'w')
                                    print('\nOutputted to PERM_RBTraversal.txt')
                                else:
                                    fileOut = open(
                                        'SORTED_RBTraversal.txt', 'w')
                                    print('\nOutputted to SORTED_RBTraversal.txt')
                                for line in val:
                                    fileOut.writelines(line + '\n')

                                fileOut.close()
                            case '3':
                                val = input(
                                    'Enter a key to print the parent key of: ')
                                RB.myTree.PrintParentKey(val)
                            case '4':
                                val = input(
                                    'Enter a key to print the left child of: ')
                                RB.myTree.PrintLeftChild(val)
                            case '5':
                                val = input(
                                    'Enter a key to print the right child of: ')
                                RB.myTree.PrintRightChild(val)
                            case '6':
                                val = input(
                                    'Enter a key to print the path to root of: ')
                                RB.myTree.PrintPathToRoot(val)
                            case '7':
                                val = input(
                                    'Enter a key to print the color of: ')
                                RB.myTree.PrintColor(val)
                            case '8':
                                val = input(
                                    'Enter a key to print the parents color of: ')
                                RB.myTree.PrintParentColor(val)
                            case '9':
                                val = input(
                                    'Enter a key to print uncle color of: ')
                                RB.myTree.PrintUncleColor(val)
                            case '10':
                                val = input(
                                    'Enter a key to print the depth of: ')
                                if val is not None:
                                    RB.myTree.PrintDepth(val)
                                else:
                                    RB.myTree.PrintDepth()
                            case '11':
                                break
                            case _:
                                print(
                                    '*** Invalid input, please try again. ***')

                except IOError:
                    print(fileDestination + ' failed to open')


if __name__ == '__main__':
    main()


# BST.my_tree = BST.Tree()
# BST.my_tree.treeInsert(BST.Node(5))
# BST.my_tree.treeInsert(BST.Node(3))
# BST.my_tree.treeInsert(BST.Node(7))
# BST.my_tree.treeInsert(BST.Node(2))
# BST.my_tree.treeInsert(BST.Node(1))
# BST.my_tree.treeInsert(BST.Node(0))

# BST.my_tree.printPathToRoot(0)
