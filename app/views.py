from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .filters import MessageFilter
from .forms import PostForm
from .models import Post, MyUser, Category, Message


class PostList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    ordering = 'time_in'
    paginate_by = 5


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            text_of_message = self.request.POST.get('text_of_message', 'Undefinded')
            from django.utils import timezone
            current_datetime = timezone.now()
            Message.objects.create(text=text_of_message, user_id=self.request.user.pk, post_id=self.get_object().pk,
                                   time_in=current_datetime)

            return render(request, 'message_sent_successfully.html')
        else:
            return redirect('/accounts/login/')



class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'create_post.html'
    form_class = PostForm
    success_url = reverse_lazy("my_posts")

    def form_valid(self, form):
        post = form.save(commit=False)  # object of model Post
        # print(post.category)
        post.user_id = self.request.user.id
        return super().form_valid(form)


class PostEdit(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = PostForm
    success_url = reverse_lazy('my_posts')

    def form_valid(self, form):
        post = form.save(commit=False)  # object of model Post
        # print(post.category)
        post.user_id = self.request.user.id
        return super().form_valid(form)


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('my_posts')


class MessagesList(LoginRequiredMixin, ListView):
    model = Message
    template_name = 'messages.html'
    context_object_name = 'messages'
    ordering = 'time_in'
    paginate_by = 5

    def get_queryset(self):
        posts_of_user = Post.objects.filter(user_id=self.request.user.pk)
        list_of_pk_posts = [post.id for post in posts_of_user]
        qs_messages_of_user = Message.objects.filter(post_id__in=list_of_pk_posts)
        self.filterset = MessageFilter(self.request.GET, request=self.request, queryset=qs_messages_of_user)

        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class MyPostsList(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'my_posts.html'
    context_object_name = 'posts'
    ordering = 'time_in'
    paginate_by = 3

    def get_queryset(self):
        posts_of_user = Post.objects.filter(user_id=self.request.user.pk)

        return posts_of_user


@login_required
def delete_message(request, pk):
    item = Message.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
    return redirect('/messages/')


@login_required
def mark_as_read(request, pk):
    item = Message.objects.get(id=pk)
    if request.method == "POST":
        item.is_read = True
        item.save()
        email = MyUser.objects.get(id=item.user_id).email
        post_name = Post.objects.get(id=item.post_id).title
        send_mail(
            "Ваше сообщение прочитано!",
            f"Вы отправляли сообщение к статье {post_name}. Данное сообщение было прочитано автором статьи.",
            "dim.bir2017@yandex.ru",
            [email],
            fail_silently=False,
        )
    return redirect('/messages/')
