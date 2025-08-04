from django.urls import path
from . import views  

urlpatterns = [
path('', views.index, name='index'),
path('books', views.books, name='books'),
path('udate/<int:id>', views.update, name='update'),
path('delet/<int:id>', views.delet, name='delet'),
  path('login/', views.login_view, name='login'),





]
