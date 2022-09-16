from django.db import transaction
from rest_framework.response import Response
from rest_framework.decorators import api_view
from util import dbhandler
from util import BookHelper
from base.models import Book
from .serializers import BookSerializer

import json


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

# @api_view(['UPDATE'])
# def updateBook(request):
#     db = dbhandler.connect()
#     print(request.data)
#     BookHelper.updateBook(db, request.data)
#     return Response('Book Inserted')

@api_view(['DELETE'])
def deleteBook(request):
    db = dbhandler.connect()
    print(request.data)
    if request.data["isbn"]:
        return Response(BookHelper.deleteBook(db, request.data["isbn"]))
    else:
        return Response("Invalid ISBN")
