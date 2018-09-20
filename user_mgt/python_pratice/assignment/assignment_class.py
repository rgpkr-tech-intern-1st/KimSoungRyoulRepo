class Library:

    def __init__(self, name=None, book_list=list()):
        self.name = name
        self.book_list = book_list

    def add_book(self, book):
        for book_in_list in self.book_list:
            if book.title == book_in_list.title:
                raise ValueError('이미 존재하는 책입니다')
                break
        else:
            self.book_list.append(book)

    def remove_book(self, book):
        self.book_list.remove(book)

    @property
    def info(self):
        print(*self.book_list)

        return self.book_list


class Book:

    def __init__(self, title, location):
        self.title = title
        self.location = location

    def __str__(self):
        return '(책 :' + self.title + ' "location: "' + self.location + ') '

    @property
    def is_borrowed(self):
        return True if not self.location == 'Library' else False


class User:
    def __init__(self, name, book_list):
        self.name = name
        self.book_list = book_list

    def __repr__(self):
        return f'Library ({self.name}) [id: ({id(self)})]'

    def borrow_book(self, library, book_name):
        for book in library.book_list:
            if book.title == book_name:
                library.book_list.remove(book)
                self.book_list.append(book)
                return book

    def return_book(self, library, book_name):

        for book in self.book_list:
            if book.title == book_name:
                self.book_list.remove(book)
                library.book_list.append(book)
                return book


if __name__ == '__main__':
    library = Library(name='중랑구립도서관',
                      book_list=[
                          Book(title='상실의시대', location='Library'),
                          Book(title='칼의노래', location='Library'),
                          Book(title='조대협의 서버사이드 아키텍쳐', location='Library'),
                          Book(title='인사이드 피플웨어', location='Library'),
                          Book(title='Enterprise Application Architecture Pattern', location='Library')
                      ]
                      )

    library.add_book(Book(title='칼의노래', location='Library'))

    user1 = User(name='KSR', book_list=[])

    print('대출하기전 책 리스트  : ', *library.book_list)

    book = user1.borrow_book(library, '인사이드 피플웨어')
    print(book)
    print('대출 후 책 리스트  : ', *library.book_list)
    print('user1 의 소유리스트 : ', *user1.book_list)
    library.info

    book = user1.return_book(library, '인사이드 피플웨어')
    print(book)
    library.info
   