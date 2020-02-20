from Library import Library
from Book import Book
import numpy as np

with open("a_example.txt", 'r', encoding='utf-8') as infile, open("a_example_output.txt", 'w', encoding='utf-8') as outfile:
    counter = 0;

    line1 = [int(number) for number in infile.readline().split()]
    booksAmount = line1[0]
    librariesAmount = line1[1]
    daysForScanning = line1[2]

    bookScores = [int(number) for number in infile.readline().split()]

    libraries = []
    libraryInfo = [int(number) for number in infile.readline().split()]

    while libraryInfo:
        booksInLibrary = [int(number) for number in infile.readline().split()]
        bookIdsSet = set(booksInLibrary)
        bookSet = []

        for book_id in bookIdsSet:
            bookSet.append(Book(book_id, bookScores[book_id]))

        libraries.append(Library(libraryInfo[1], libraryInfo[2], bookSet))

        libraryInfo = [int(number) for number in infile.readline().split()]

    libraryScores = []
    for i in range(librariesAmount):
        libraryScores.append(libraries[i].scoreTotal(daysForScanning))

    print(libraryScores)

