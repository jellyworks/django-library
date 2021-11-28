from django.urls import path
from . import views

app_name ='rent'
urlpatterns = [
    path('students', views.StudentView.as_view()),
    path('students/<int:sid>', views.StudentView.as_view()),
    path('books', views.BookView.as_view()),
    path('rentals', views.RentalView.as_view()),

]