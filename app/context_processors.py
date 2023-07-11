from .models import Post, Message


def number_messages_of_user(request):
    posts_of_user = Post.objects.filter(user_id=request.user.pk)
    list_of_pk_posts = [post.id for post in posts_of_user]
    number_messages_of_user = Message.objects.filter(post_id__in=list_of_pk_posts, is_read=False).count()
    return {
        'number_messages_of_user': number_messages_of_user
    }
