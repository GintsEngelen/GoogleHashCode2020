import numpy as np

with open("f_libraries_of_the_world.txt", 'r', encoding='utf-8') as infile, open("f_libraries_of_the_world_output.txt", 'w', encoding='utf-8') as outfile:

    [booksAmount, librariesAmount, daysForScanning] = [int(number) for number in infile.readline().split()]

    # This array will contain the score of each book on one row,and this row is duplicated so that we end up with a 2D array
    # where each row number corresponds to a library ID, and each row contains the scores for all books, where the column
    # index corresponds to the book id. Later, we make an array of equal dimensions, 'libraryBooks',  where instead of
    # book scores, we will simply write True or False, depending on whether the library at the given row has the book
    # with ID equal to the column index. This will later be used as a mask for the first array, in order to easily
    # calculate the total score of all books that a library has.
    bookScores = np.column_stack((
        np.arange(booksAmount, dtype=int),
        np.array(infile.readline().split(), dtype=int)
    ))

    libraryInfo = np.zeros((librariesAmount, 3), dtype=int)

    # The goal is to have a matrix with dimensions(libraries, book_ids), and True if that book is in that library
    libraryBooks = np.zeros((librariesAmount, booksAmount), dtype=bool)
    library_Id_Score_TotalSentBooks = np.concatenate((
        np.arange(librariesAmount, dtype=float).reshape(librariesAmount, 1),
        np.zeros((librariesAmount, 2), dtype=float)),
        axis=1)

    for i in range(librariesAmount):

        libraryInfo[i] = np.array([infile.readline().split()], dtype=int)
        libraryBooksIndexes = np.array([infile.readline().split()], dtype=int)

        libraryBooks[i, libraryBooksIndexes] = True

    # This function will change depending on the dataset
    def updateScores(daysForScanning, library_ids=np.arange(librariesAmount)):
        for i in library_ids:
            totalBookScanningCapacity = (daysForScanning - libraryInfo[i, 1]) * libraryInfo[i, 2]
            library_Id_Score_TotalSentBooks[i, 2] = totalBookScanningCapacity

            library_Id_Score_TotalSentBooks[i, 1] = np.sum(
                np.sort(bookScores[:, 1][libraryBooks[i]][::-1])[0:totalBookScanningCapacity]) / daysForScanning

    output = list()


    while daysForScanning > 0:
        updateScores(daysForScanning)
        bestLibrary = np.argmax(library_Id_Score_TotalSentBooks[:, 1])
        containedBooks = bookScores[libraryBooks[bestLibrary]]
        reverseSortedBooks = containedBooks[containedBooks[:, 1].argsort()][::-1]
        booksToScan = reverseSortedBooks[0:libraryInfo[bestLibrary, 0]]
        if booksToScan.shape[0] == 0: break
        libraryBooks[:, booksToScan[:, 0]] = False
        libraryBooks[bestLibrary, :] = False

        output.append([bestLibrary, booksToScan.shape[0]] + list(booksToScan[:, 0]))
        print(daysForScanning)
        daysForScanning -= libraryInfo[bestLibrary, 1]

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