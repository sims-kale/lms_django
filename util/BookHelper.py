from base.models import Book,Admin


# def getAdmins(db):
#     mycursor = db.cursor()
#     mycursor.execute("select * from library.admins")
#     result = mycursor.fetchall()
#     admins = []
#     for i in result:
#         admins.append(Admin(Admin_Name=i[0],Email_id=i[1],passwords = i[2]))
#         return admins
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
    print(sql)
    mycursor.execute(sql)
    db.commit()
    if mycursor.rowcount != 0:
        return "Book Inserted"
    else:
        return "Invalid Data"


def updateBook(db, book):
    deleteBook(db,book["isbn"])
    insertBook(db,book)
    print('Update Called')
    return "Book Updated"
    # mycursor = db.cursor()
    # sql = "DELETE FROM books WHERE isbn = " + isbn
    # sql1 = "insert into books values ( '" + book["isbn"] + "','" + book["title"] + "','" + book["author"] + "','" + book[
    #     "publisher"] + "'," + str(book["publishyear"]) + ",'" + book["genre"] + "');"
    # print(sql);
    # mycursor.execute(sql,sql1)
    # db.commit()
    # if mycursor.rowcount != 0:
    #     return "Book Updated"
    # else:
    #     return "Invalid Data"