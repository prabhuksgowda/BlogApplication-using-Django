from django.urls import path
from .views import UserRegisterView, UserEditView,  PasswordsChangeView
from .views import HomeView, PostDetailView ,AddPost, EditPost, DeletePostView
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',HomeView.as_view(), name='index' ),
    path('post_detail/<int:pk>',PostDetailView.as_view(), name='post_detail'),
    path('addpost/',AddPost.as_view(), name='addpost'),
    path('editpost/<int:pk>',EditPost.as_view(), name='editpost'),
    path('deletepost/<int:pk>/remove',DeletePostView.as_view(), name='deletepost'),
    path('category/<str:cats>/',views.CategoryView, name='category' ),
    path('profile/',views.profile, name='profile'),
    #path('mypost/',views.myPost, name='mypost'),

    #path('like/<int:pk>', LikeView, name='likepost'),

    path('register/',UserRegisterView.as_view(), name='register'),
    path('editprofile/',UserEditView.as_view(), name='editprofile'),
    path('password/',PasswordsChangeView.as_view(template_name='registration/changepassword.html')),



]