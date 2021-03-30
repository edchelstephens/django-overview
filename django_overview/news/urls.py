"""URLconf for news app."""

from django.urls import path

from news import views

urlpatterns = [
    path('articles/<int:year>/', views.year_archive),
    path('articles/<int:year>/<int:month>/', views.month_archive),
    path('article/<int:pk>/', views.article_detail),
]