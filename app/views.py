from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PostForm
from .models import Post, MyUser, Category, Message


# Create your views here

class PostList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    ordering = 'time_in'
    paginate_by = 3


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

    def post(self, request, *args, **kwargs):
        text_of_message = self.request.POST.get('text_of_message', 'Undefinded')
        from datetime import datetime
        current_datetime = datetime.now()
        Message.objects.create(text=text_of_message, user_id=self.request.user.pk, post_id=self.get_object().pk, time_in=current_datetime) #FIXME

        return HttpResponseRedirect(f"{self.request.path}")



class PostCreate(CreateView):
    model = Post
    template_name = 'create_post.html'
    form_class = PostForm
    success_url = reverse_lazy("posts")


class PostEdit(UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = PostForm


class PostDelete(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('posts')


class MessagesList(ListView):
    model = Message
    template_name = 'messages.html'
    context_object_name = 'messages'
    ordering = 'time_in'
    paginate_by = 10
