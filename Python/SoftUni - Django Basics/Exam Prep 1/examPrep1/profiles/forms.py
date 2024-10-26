from django import forms

from examPrep1.mixins import PlaceholderMixin
from profiles.models import Profile


class BaseProfileForm(PlaceholderMixin, forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileCreateForm(BaseProfileForm):
    pass
