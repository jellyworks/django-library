from django.db import models
from datetime import datetime

class Student(models.Model):
    no = models.AutoField(primary_key=True)
    name=models.CharField(max_length=128, null=False)
    major=models.CharField(max_length=128, null=False)
    grade=models.IntegerField(null=True)
    gender=models.CharField(max_length=1, null=True)
    class Meta:
        db_table="students"

class Book(models.Model):
    isbn=models.CharField(max_length=128, null=False, primary_key=True)
    title=models.CharField(max_length=128, null=False)
    class Meta:
        db_table="books"

class Rental(models.Model):
    no = models.ForeignKey(Student, on_delete=models.CASCADE)
    #protect, setnull
    isbn = models.ForeignKey(Book, on_delete=models.CASCADE)
    title=models.CharField(max_length=128, null=False)
    # rent_date = models.DateTimeField(auto_now_add=True, default=datetime.now)
    class Meta:
        db_table="rentals"
