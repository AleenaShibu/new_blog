from django.urls import path
from .views import HomePostView,DetailPostView,AddPostView,UpdatePostView,DeletePostView

urlpatterns = [
    path('',HomePostView.as_view(),name = 'lists'),
    path('detail/<int:pk>/',DetailPostView.as_view(),name = 'detail'),
    path('addpost/',AddPostView.as_view(),name = 'addpost'),
    path('update/<int:pk>/',UpdatePostView.as_view(),name ='updatepost'),
    path('delete/<int:pk>/',DeletePostView.as_view(),name = 'deletepost'),
    ]

