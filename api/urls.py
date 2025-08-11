from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.studentsView, name="students"),
    path('students/<int:id>/', views.studentDetailView),
]