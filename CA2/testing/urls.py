from django.urls import path
from . import views
urlpatterns = [
    # path("", views.book_list, name='book_list'),
    path('add/', views.add_book, name='add_book'),
    path('detail/<int:id>/', views.book_detail, name='book_detail'),
    path('delete/<int:id>/', views.delete_book, name='delete_book'),
    path('update/<int:id>/', views.update_book, name='update_book'),
    path('', views.home, name='home'),
    path('set_theme/', views.set_theme, name='set_theme'),
    path('read_theme/', views.read_theme, name='read_theme'),
    path('clear_theme/', views.clear_theme, name='clear_theme'),
    path('set_counter/', views.visit_counter, name='visit_counter'),
    path('clear_counter/', views.reset, name='reset'),
]