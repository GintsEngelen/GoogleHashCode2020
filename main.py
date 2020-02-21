import numpy as np

with open("a_example.txt", 'r', encoding='utf-8') as infile, open("a_example_output.txt", 'w', encoding='utf-8') as outfile:
    counter = 0;

    [booksAmount, librariesAmount, daysForScanning] = [int(number) for number in infile.readline().split()]
    bookScores = np.array([infile.readline().split()])

    libraryInfo = np.zeros((librariesAmount, 3))
    libraryBooks = np.zeros((librariesAmount, booksAmount), dtype=bool)

    for i in range(librariesAmount):

        libraryInfo[i] = np.array([infile.readline().split()], dtype=int)
        libraryBooksIndexes = np.array([infile.readline().split()], dtype=int)

        libraryBooks[i, libraryBooksIndexes] = True

    print(libraryInfo)
    print(libraryBooks)

    print()
