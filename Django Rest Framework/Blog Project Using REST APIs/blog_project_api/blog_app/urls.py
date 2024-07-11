from django.urls import path
from .views import BlogPostListCreate, BlogPostRetrieveUpdateDestroy, blog_list

urlpatterns = [
    path('posts/', BlogPostListCreate.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', BlogPostRetrieveUpdateDestroy.as_view(), name='post-detail'),
    path('', blog_list, name='blog-list'),
]