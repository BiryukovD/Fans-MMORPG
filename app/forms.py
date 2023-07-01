from django import forms
from django.core.exceptions import ValidationError
from tinymce.widgets import TinyMCE

from .models import Post, MyUser
from allauth.account.forms import SignupForm


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        widgets = {'content': TinyMCE(attrs={'cols': 80, 'rows': 30})}
        fields = ['title', 'picture', 'content', 'category', 'user']


class MyCustomSignupForm(SignupForm):
    picture = forms.ImageField(label='Фото профиля')

    def save(self, request):
        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MyCustomSignupForm, self).save(request)
        user.picture = self.cleaned_data['picture']
        # Add your own processing here.
        user.save()
        # You must return the original result.
        return user


