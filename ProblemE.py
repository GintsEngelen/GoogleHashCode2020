import numpy as np

with open("e_so_many_books.txt.txt", 'r', encoding='utf-8') as infile, open("e_so_many_books_output.txt", 'w', encoding='utf-8') as outfile:

    [booksAmount, librariesAmount, daysForScanning] = [int(number) for number in infile.readline().split()]

    # This array will contain the score of each book on a row,
    # and this row is duplicated to match the amount of libraries
    bookScores = np.column_stack((
        np.arange(booksAmount, dtype=int),
        np.array(infile.readline().split(), dtype=int)
    ))

    libraryInfo = np.zeros((librariesAmount, 3), dtype=int)

    # The goal is to have a matrix with dimensions(libraries, book_ids), and True if that book is in that library
    libraryBooks = []
    library_Id_Score_TotalSentBooks = np.concatenate((
        np.arange(librariesAmount, dtype=float).reshape(librariesAmount, 1),
        np.zeros((librariesAmount, 2), dtype=float)),
        axis=1)

    for i in range(librariesAmount):

        libraryInfo[i] = np.array([infile.readline().split()], dtype=int)
        libraryBooksIndexes = [int(number) for number in infile.readline().split()]

        libraryBooks.append(set(libraryBooksIndexes))

    def updateScores(library_ids=np.arange(librariesAmount)):
        for i in library_ids:
            library_Id_Score_TotalSentBooks[i, 1] = len(libraryBooks[i])

    output = list()

    while daysForScanning > 0:
        updateScores()
        bestLibrary = np.argmax(library_Id_Score_TotalSentBooks[:, 1])
        booksToScan = libraryBooks[bestLibrary]

        output.append([bestLibrary, len(booksToScan)] + list(booksToScan))

        for i in range(0, librariesAmount):
            libraryBooks[i] = libraryBooks[i] - booksToScan

        daysForScanning -= libraryInfo[bestLibrary, 1]
        if (daysForScanning - 1) % 100 == 0:
            print("Days Left: " + str(daysForScanning))

    outfile.write(str(len(output)) + "\n")
    for line in output:
        outfile.write(str(line[0]) + " " + str(line[1]) + "\n")

        allowSpaceBeforeNumber = False
        for item in line[2:]:
            if allowSpaceBeforeNumber:
                outfile.write(" ")
            else:
                allowSpaceBeforeNumber = True
            outfile.write(str(item))
        outfile.write("\n")