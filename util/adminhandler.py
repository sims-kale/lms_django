from base.models import Admins


def getAdmin(db):
    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM library.admins")
    myresult = mycursor.fetchall()
    admins = []
    for x in myresult:

        admins.append(Admins(Admin_Name=x[0], Email_id=x[1], passwords=x[2]))
    return admins
