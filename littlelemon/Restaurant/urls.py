from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.MenuView.as_view(), name='menu'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view()),
    
]
