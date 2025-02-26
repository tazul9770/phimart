from django.urls import path
from product import views

urlpatterns = [
    path('', views.view_product, name='view-product'),
    path('<int:id>/', views.view_specific_product, name='specific-list')
]
