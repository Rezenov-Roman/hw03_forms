from django.contrib.auth import get_user_model
from django import forms
from .models import Post, Group


User = get_user_model()


class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('text', 'group',)
        labels = {
            'text': 'Автор',
            'group': 'Название группы',
        }
        help_texts = {
            'text': 'Напишите пост здесь',
            'group': 'Выберите свою группу',
        }
