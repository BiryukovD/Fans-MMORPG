from django.core.mail import send_mail
from django.db.models.signals import post_save, pre_init
from django.dispatch import receiver
from django.template.loader import render_to_string
from Fans_MMORPG import settings
from app.models import Message, Post, MyUser


@receiver(post_save, sender=Message)
def my_handler(sender, instance, **kwargs):
    post = Post.objects.get(id=instance.post_id)
    email = MyUser.objects.get(id=post.user_id).email

    html_content = render_to_string('you have got mail.html',
                                    {'post': post})

    send_mail(
        'К вашей статье поступило сообщение!',
        '',
        settings.EMAIL_HOST_USER,
        [email],
        html_message=html_content,
        fail_silently=False

    )
