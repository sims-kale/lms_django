from base.models import Book

def get_all_books(db):
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM library.books")
    myresult = mycursor.fetchall()
    books = []
    for x in myresult:
        # print(x)
        books.append(Book(title=x[1],author=x[3],publisher=x[2],  isbn=x[0],genre=x[5],publishyear=x[4]))
    return books
