from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
# router.register('employee', views.EmployeeViewSet, basename='employee')


urlpatterns = [
    path('students/', views.studentsView, name="students"),
    path('students/<int:primary_key>/', views.studentDetailView),

    #class based view here Employee is class
    # path('employee/',views.Employees.as_view()),
    # path('employee/<int:id>/', views.EmployeesDetailsView.as_view()),

    path('', include(router.urls)),
    path('blogs/', views.BlogsView.as_view(), name="blogs"),
    path('comments/', views.CommentsView.as_view(), name="comments"),
    path('blogs/<int:id>/', views.BlogsDetailsView.as_view()),
    path('comments/<int:id>/', views.CommentsDetailsView.as_view()),


]