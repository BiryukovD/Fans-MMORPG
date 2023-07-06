import django_filters
from .models import Message, Post


class MessageFilter(django_filters.FilterSet):
    # post_id = django_filters.(method='get_qs')
    #
    # def get_qs(self, queryset, name, value):
    #     qs = Post.objects.filter(id=self.request.user.id)
    #     return qs

    class Meta:
        model = Message
        fields = ['post_id']



