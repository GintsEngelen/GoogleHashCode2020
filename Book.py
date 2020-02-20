class Book:
    def __init__(self, book_id, score):
        self._book_id = book_id
        self._score = score

    def __str__(self):
        return "book: " + str(self._book_id) + " " + str(self._score)
