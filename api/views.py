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
    serializer = BookSerializer(BookHelper.get_all_books(db),many=True)
    return Response(serializer.data)
