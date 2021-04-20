from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import SignUpForm, EditProfileForm, PasswordChangeingForm
from django.contrib.auth.views import PasswordChangeView
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.contrib.auth.models import Group


# Create your views here.

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('index')
    
class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/editprofile.html'
    success_url = reverse_lazy('index')

    def get_object(self):
        return self.request.user

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeingForm
    success_url = reverse_lazy('editprofile')


class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-id']
    #ordering = ['-date']



class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class AddPost(CreateView):
    model = Post
    #form_class = PostForm
    template_name = 'addpost.html'
    fields = '__all__'
    #labels = {'title':'Post Title', 'title_tag':'Title Tag Line', 'author':'Author', 'content':'Post Content'}
    success_url = '/'

class EditPost(UpdateView):
    model = Post
    template_name = 'editpost.html'
    fields = ['title','title_tag', 'category','content']
    success_url = '/'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'deletepost.html'
    success_url = '/'


def CategoryView(request, cats):
    category_posts=Post.objects.filter(category=cats)
    return render(request, 'category.html', {'cats':cats.title(), 'category_posts':category_posts})


# def LikeView(request,pk):
#     post = get_object_or_404(Post, id=request.POST.get('post_id'))
#     post.likes.add(request.user)
#     return HttpResponseRedirect(reverse('post_detail', args=[str(pk)] ))


def profile(request):
    if request.user.is_authenticated:
        post = Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        gps = user.groups.all()
        return render(request,'registration/profile.html',{'posts':post,'full_name':full_name,'groups':gps})
    else:
        return HttpResponseRedirect('/login/')