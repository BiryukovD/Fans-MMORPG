from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField


# Create your models here.
class MyUser(AbstractUser):
    picture = models.ImageField(upload_to='users', verbose_name='Фото профиля')

    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователь'
        ordering = ['-date_joined']

    def __str__(self):
        return f'{self.username}'


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название категории')
    picture = models.ImageField(upload_to='category', verbose_name='Фото категории')

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'Категория'
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = HTMLField()
    picture = models.ImageField(upload_to='posts', verbose_name='Заглавное фото')
    time_in = models.DateTimeField(auto_now=True, verbose_name='Время публикации')

    class Meta:
        verbose_name_plural = 'Статьи'
        verbose_name = 'Статья'
        ordering = ['-time_in']

    def __str__(self):
        return f'{self.title}'



class Message(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Текст')
    is_read = models.BooleanField(default=False, verbose_name='Прочитано')
    time_in = models.DateTimeField(verbose_name='Время отправки')

    class Meta:
        verbose_name_plural = 'Сообщения'
        verbose_name = 'Сообщение'
        ordering = ['-time_in']

    def __str__(self):
        return f'{self.text}'
