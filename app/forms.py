from django import forms
from django.core.exceptions import ValidationError
from tinymce.widgets import TinyMCE
from django.utils.translation import gettext_lazy as _
from .models import Post, MyUser, Category
from allauth.account.forms import SignupForm


class PostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'size': '60', 'placeholder': 'Заголовок статьи'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Выберите категорию")

    class Meta:
        model = Post
        widgets = {'content': TinyMCE(attrs={'cols': 80, 'rows': 30})}
        fields = ['title', 'picture', 'content', 'category']
        labels = {'category': 'Категория'}


class MyCustomSignupForm(SignupForm):
    picture = forms.ImageField(label='Фото профиля')

    def custom_signup(self, request, user):
        user.picture = self.cleaned_data['picture']
        user.save()


