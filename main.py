from Library import Library
from Book import Book

with open("a_example.txt", 'r', encoding='utf-8') as infile, open("a_example_output.txt", 'w', encoding='utf-8') as outfile:
    counter = 0;

    line1 = [int(number) for number in infile.readline().split()]
    booksAmount = line1[0]
    librariesAmount = line1[1]
    daysForScanning = line1[2]

    librariesBooksAmount = []
    librariesBooks = []
    librariesSignUpTime = []
    librariesShippingCapacity = []
    bookScores = [int(number) for number in infile.readline().split()]

    libraryInfo = [int(number) for number in infile.readline().split()]

    while libraryInfo:
        librariesBooksAmount.append(libraryInfo[0])
        librariesSignUpTime.append(libraryInfo[1])
        librariesShippingCapacity.append(libraryInfo[2])

        booksInLibrary = [int(number) for number in infile.readline().split()]
        librariesBooks.append(set(booksInLibrary))

    libraryScores = []
    for i in range(librariesAmount):
        libraryScores.append(libraries[i].scoreTotal(daysForScanning))

    print(libraryScores)

