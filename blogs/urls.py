from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.BlogsView.as_view(), name="blogs"),
    path('comments/', views.CommentsView.as_view(), name="comments"),
    path('blogs/<int:id>/', views.BlogsDetailsView.as_view()),
    path('comments/<int:id>/', views.CommentsDetailsView.as_view()),
]
