from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='index'),
    path('update', views.update, name='update'),
    path('home', views.homepage, name='home'),
    path('catagories/<int:id>', views.homepage, name='catagories'),
    path('products/<int:id>', views.product_detail, name='product_detail'),
]