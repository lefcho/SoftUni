from django import forms

from authors.models import Author


class BaseAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'passcode', 'pets_number',]
        labels = {
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'passcode': 'Passcode:',
            'pets_number': 'Pets Number:',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={
                'placeholder': 'Enter your first name...',
            }),
            'last_name': forms.TextInput(attrs={
                'placeholder': 'Enter your last name...',
            }),
            'passcode': forms.PasswordInput(attrs={
                'placeholder': 'Enter 6 digits...',
            }),
            'pets_number': forms.NumberInput(attrs={
                'placeholder': 'Enter the number of your pets...',
            }),
        }
        help_texts = {
            'passcode': 'Your passcode must be a combination of 6 digits'
        }


class AuthorCreateForm(BaseAuthorForm):
    pass


class AuthorEditForm(BaseAuthorForm):
    class Meta(BaseAuthorForm.Meta):
        fields = ['first_name', 'last_name', 'pets_number','info', 'image_url',]
        widgets = {
            **BaseAuthorForm.Meta.widgets,
            'info': forms.Textarea(attrs={
                'placeholder': 'Share something about yourself...',
            }),
            'image_url': forms.URLInput(attrs={
                'placeholder': 'Enter a URL to your profile image...',
            }),
        }

        labels = {
            **BaseAuthorForm.Meta.labels,
            'info': 'Info:',
            'image_url': 'Profile Image URL:',
        }
