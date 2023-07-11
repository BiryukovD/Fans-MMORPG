import django_filters
from .models import Message, Post


def qs_posts_of_user(request):
    qs = Post.objects.filter(user_id=request.user.id)
    return qs


class MessageFilter(django_filters.FilterSet):
    post_id = django_filters.ModelChoiceFilter(queryset=qs_posts_of_user, empty_label="Выберите статью")

    class Meta:
        model = Message
        fields = ['post_id']

