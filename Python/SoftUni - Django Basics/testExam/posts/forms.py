from posts.models import Post
from django import forms


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image_url', 'content']
        labels = {
            'title': 'Title:',
            'image_url': 'Post Image URL:',
            'content': 'Content:',
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Put an attractive and unique title...',
            }),
            'content': forms.Textarea(attrs={
                'placeholder': 'Share some interesting facts about your adorable pets...',
            }),
        }
        help_texts = {
            'image_url': 'Share your funniest furry photo URL!',
        }
        error_messages = {
            'title': {
                'unique': "Oops! That title is already taken. How about something fresh and fun?",
            },
        }


class PostCreateForm(PostBaseForm):
    pass


class PostEditForm(PostBaseForm):
    pass


class PostDeleteForm(PostBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.keys():
            self.fields[field].widget.attrs['readonly'] = True
