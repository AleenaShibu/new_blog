from django.urls import path
from .views import HomePostView,DetailPostView

urlpatterns = [
    path('',HomePostView.as_view(),name = 'lists'),
    path('detail/<int:pk>/',DetailPostView.as_view(),name = 'detail')
    ]

