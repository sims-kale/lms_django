from rest_framework import serializers
from base.models import Book, Admins


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admins
        fields = '__all__'
