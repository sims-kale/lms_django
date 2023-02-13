from django.db import transaction
from rest_framework.response import Response
from rest_framework.decorators import api_view
from util import dbhandler
from util import BookHelper
from util import adminhandler
from base.models import Book
from .serializers import BookSerializer, AdminSerializer

import json


@api_view(['GET'])
def getAdmin(request):
    db = dbhandler.connect()
    serializer = AdminSerializer(adminhandler.getAdmin(db), many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getData(request):
    db = dbhandler.connect()
    serializer = BookSerializer(BookHelper.get_all_books(db), many=True)
    return Response(serializer.data)


@api_view(['POST'])
def insertBook(request):
    db = dbhandler.connect()
    print(request.data)
    BookHelper.insertBook(db, request.data)
    return Response('Book Inserted')


@api_view(['PUT'])
def updateBook(request):
    db = dbhandler.connect()
    print(request.data)
    # serializer = BookSerializer(BookHelper.get_all_books(db), many=True)
    return Response(BookHelper.updateBook(db, request.data))


@api_view(['DELETE'])
def deleteBook(request):
    db = dbhandler.connect()
    print(request.data)
    if request.data["isbn"]:
        return Response(BookHelper.deleteBook(db, request.data["isbn"]))
    else:
        return Response("Invalid ISBN")


@api_view(['GET'])
def auth(request):
    email = request.data["email"]
    password = request.data["password"]
    db = dbhandler.connect()
    db = dbhandler.connect()
    mycursor = db.cursor(buffered=True)
    sql = "select * from admins where email_id= '" + email + "' and passwords='" + password + "';"
    print(sql)
    mycursor.execute(sql)
    db.commit()
    if mycursor.rowcount == 1:
        return Response("1")
    else:
        return Response("0")
