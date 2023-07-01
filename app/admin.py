from django.contrib import admin
from .models import MyUser, Post, Category, Message
# Register your models here.

admin.site.register(MyUser)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Message)
