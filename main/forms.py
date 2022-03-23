from django.forms import ModelForm, BooleanField  # Импортируем true-false поле
from .models import Post


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['author', 'type', 'categories', 'heder','text']  # не забываем включить галочку в поля иначе она не будет показываться на странице!