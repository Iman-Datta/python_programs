import sys                                              # List & Tuple
library: list = []                                      # List
book_id: int = 100
status: bool = False
def check_book() -> int:
    no_book = len(library)
    if no_book == 0:
        return 0
    else:
        return no_book

while True:
    print('1: Add book: ')
    print('2: Display all book: ')
    print('3: Delete a book: ')
    print('4: Search a book: ')
    print('5: Exit: ')
    choice = int(input('Enter your choice: '))
    if choice == 1:                                     
        print('Book Id: {}'.format(book_id))
        bkname = input('Enter a book name: ')
        bkcost = int(input('Enter book price: '))
        bk = (book_id, bkname, bkcost)
        print(bk)
        library.append(bk)
        book_id += 1
    elif choice == 2:
        if check_book() == 0:
            print("There is no book, press 1")
        else:
            i: int = 0
            for i in range(len(library)):
                # print('Book ID: {} Name: {} Cost: {}'.format(library[i][0],library[i][1],library[i][2]))
                print('Book ID: ' + library[i][0] + 'Name: ' + library[i][1] + 'Cost: ' + library[i][2])
    elif choice == 3:
        if check_book() == 0:
            print("There is no book, press 1")
        else:
            no_book = check_book()
            bk_index = int(input('Enter a book ID to be deleted: '))
            for i in range(0, no_book):
                if library[i][0] == bk_index:
                    status = True
                    print("Deleted book is {}".format(library.pop(i)))
                    break
            if status == False:
                print("Book with index {} does not exsit".format(bk_index))
    elif choice == 4:
        if check_book() == 0:
            print("There is no book, press 1")
        else:
            search = int(input("Enter a book ID to be searched: "))
            sc_book = check_book()
            for i in range(0,sc_book):
                if library[i][0] == search:
                   status = True
                   print("The name of the searched book is {} & the cost of the book is {}".format(library[i][1], library[i][2]))
                   break
            if status == False:
                    print("Book with index {} does not exsit".format(search))
    else:
        sys.exit(1)