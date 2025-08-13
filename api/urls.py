from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.studentsView, name="students"),
    path('students/<int:primary_key>/', views.studentDetailView),

    #class based view here Employee is class
    path('employee/',views.Employees.as_view()),
    path('employee/<int:primary_key>/', views.EmployeesDetailsView.as_view()),

    
]