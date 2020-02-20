class Library:
    def __init__(self, signtime, booksPerDay, bookSet):
        self._signtime = signtime
        self._booksPerDay = booksPerDay
        self._bookSet = bookSet

    def __str__(self):
        return "Library: " + str(self._signtime) + " " + str(self._booksPerDay) + " " + str(self._bookSet)

    def scoreTotal(self, totalDays):
        shipDays = totalDays - self._signtime
        bookTuples = []
        for book in self._bookSet:
            bookTuples.append((book._book_id, book._score))

        bookTuples.sort(key=lambda tup: tup[1], reverse=True)

        totalBooksToShip = shipDays * self._booksPerDay
        shippableBooksTuple = bookTuples[0:totalBooksToShip]
        return (shippableBooksTuple, sum([pair[1] for pair in shippableBooksTuple]))






