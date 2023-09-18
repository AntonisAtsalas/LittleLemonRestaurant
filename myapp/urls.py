from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('home', views.home, name="home"),
    path('about', views.about, name='about'),
    path('menu', views.menu, name='menu'),
    path('book', views.book, name='book'), 
    path('dishes/<str:dish>', views.menuitems),
    path('drinks/<str:drink>', views.drinks, name="drink"), 
    path('form', views.form_view),
    path('booking', views.form_view),
    path('menucards', views.menu_by_id)

]