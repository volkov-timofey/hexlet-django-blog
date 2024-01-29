from django.urls import path

from hexlet_django_blog.article import views

urlpatterns = [
    path('articles/<tags>/<int:article_id>', views.index, name='article'),
]