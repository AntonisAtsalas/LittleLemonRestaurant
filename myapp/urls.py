from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="home"),
    path('about', views.about, name='about'),
    path('menu', views.menu, name='menu'),
    path('book', views.form_view, name='book'), 
    path('books', views.books),
    path('booking', views.form_view),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),

]