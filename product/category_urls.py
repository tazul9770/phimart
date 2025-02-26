from django.urls import path
from product import views

urlpatterns = [
    path('', views.view_category, name='view-category'),
    path('<int:pk>/', views.view_specific_category, name='specific-category')
]