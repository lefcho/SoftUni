from django import forms

from albums.models import Album
from examPrep1.mixins import PlaceholderMixin


class BaseAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ('owner', )


class AddAlbumForm(PlaceholderMixin, BaseAlbumForm):
    pass


class EditAlbumForm(PlaceholderMixin, BaseAlbumForm):
    pass


class DeleteAlbumForm(BaseAlbumForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.keys():
            self.fields[field].widget.attrs['readonly'] = True
