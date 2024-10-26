from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.text import slugify


@deconstructible
class AlphaNumericalValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = 'Must contain only numbers, letters and underscore'
        else:
            self.__message = value

    def __call__(self, value, *args, **kwargs):
        slugged_value = slugify(value)
        if '-' in value or value.lower() != slugged_value:
            raise ValidationError(self.message)
