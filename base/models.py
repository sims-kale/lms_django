from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    isbn = models.CharField(max_length=255, primary_key=True)
    publishyear = models.IntegerField()
    genre = models.CharField(max_length=255)


class Admins(models.Model):
    Admin_Name = models.CharField(max_length=255)
    Email_id = models.CharField(max_length=255)
    passwords = models.CharField(max_length=255)
