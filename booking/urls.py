# booking/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('masters/', views.master_list, name='master_list'),
    path('services/', views.service_list, name='service_list'),
    path('about/', views.about_us, name='about_us'),
    path('book/', views.book_appointment, name='book_appointment'),
    path('masters/<int:master_id>/review/', views.add_review, name='add_review'),
    path('reviews/', views.reviews, name='reviews'),
     path('master_reviews/<int:master_id>/', views.master_reviews, name='master_reviews'),
     path('review/<int:review_id>/', views.review_detail, name='review_detail'),

]
