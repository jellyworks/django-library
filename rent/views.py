from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import serializers

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import StudentSerializer
from .serializers import BookSerializer
from .serializers import RentalSerializer
from rest_framework import status
from .models import Student
from .models import Book
from .models import Rental
class StudentView(APIView):

    def post(self, request):
        student_serializer = StudentSerializer(data=request.data)
        if student_serializer.is_valid():
            student_serializer.save()
            return Response( {'result':'success', 'data':student_serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'result:':'fail',
                                'data':student_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)   

    def get(self, request, **kwargs):
        if kwargs.get('sid') is None:
            student_serializer = StudentSerializer(Student.objects.all(), many=True)
            return Response({'users':student_serializer.data,
                             'count':Student.objects.count()}, status=status.HTTP_200_OK)
        else:
            sid = kwargs.get('sid')
            rentals = Rental.objects.filter(no=sid)
            rentals_serializer = RentalSerializer(rentals, many=True)
            user_one_serializer = StudentSerializer(Student.objects.get(no=sid))
            return Response({'student':user_one_serializer.data,
                             'books':rentals_serializer.data
                            }, status=status.HTTP_200_OK)

class BookView(APIView):
    def post(self, request):
        book_serializer = BookSerializer(data=request.data)
        if book_serializer.is_valid():
            book_serializer.save()
            return Response( {'result':'success', 'data':book_serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({'result:':'fail',
                                'data':book_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)  

class RentalView(APIView):
    def post(self, request):
        rental_serializer = RentalSerializer(data=request.data)
        if rental_serializer.is_valid():
            rental_serializer.save()
            return Response( {'result':'success', 'data':rental_serializer.data
                            }, status=status.HTTP_201_CREATED)
        else:
            return Response({'result:':'fail',
                                'data':rental_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)    
    def get(self, request, **kwargs):
        if kwargs.get('sid') is None:
            rental_serializer = RentalSerializer(Rental.objects.all(), many=True)
            return Response({'users':rental_serializer.data,
                             'count':Rental.objects.count()}, status=status.HTTP_200_OK)
        else:
            sid = kwargs.get('sid')
            rentals = Rental.objects.get(no=sid)
            rentals_serializer = RentalSerializer(rentals)
            user_one_serializer = StudentSerializer(Student.objects.get(no=sid))
            return Response({'student':user_one_serializer.data,
                             'books':rentals_serializer.data
                            }, status=status.HTTP_200_OK)