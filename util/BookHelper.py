from base.models import Book


def get_all_books(db):
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM library.books")
    myresult = mycursor.fetchall()
    books = []
    for x in myresult:
        # print(x)
        books.append(Book(title=x[1], author=x[3], publisher=x[2], isbn=x[0], genre=x[5], publishyear=x[4]))
    return books


def deleteBook(db, isbn):
    mycursor = db.cursor()
    sql = "DELETE FROM books WHERE isbn = " + isbn

    mycursor.execute(sql)
    db.commit()
    if mycursor.rowcount != 0:
        return "Book deleted"
    else:
        return "Book Does not exist in database"


def insertBook(db, book):
    mycursor = db.cursor()

    sql = "insert into books values ( '" + book["isbn"] + "','" + book["title"] + "','" + book["author"] + "','" + book[
        "publisher"] + "'," + str(book["publishyear"]) + ",'" + book["genre"] + "');"
    print(sql);
    mycursor.execute(sql)
    db.commit()
    if mycursor.rowcount != 0:
        return "Book Inserted"
    else:
        return "Invalid Data"


# def updateBook(db, data):
#
#     return None