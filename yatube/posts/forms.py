from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import Post, Group


User = get_user_model()
CHOICES_GROUPS = {
    #'cats': cats,
    #'dogs': dogs,
}

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('text', 'group',) 
    text = forms.CharField(widget=forms.Textarea, label='Текст поста')
    group = forms.ChoiceField(required = False, label='Group', choices=CHOICES_GROUPS)