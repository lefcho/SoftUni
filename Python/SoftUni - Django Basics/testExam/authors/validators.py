from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class OnlyLettersValidator:
    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = "Your name must contain letters only!"
        else:
            self.__message = value

    def __call__(self, value, *args, **kwargs):
        if not value.isalpha():
            raise ValidationError(self.message)


@deconstructible
class ExactDigitsValidator:
    def __init__(self, exact_digits, message=None):
        self.exact_digits = exact_digits
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = f"Your passcode must be exactly {self.exact_digits} digits!"
        else:
            self.__message = value

    def __call__(self, value, *args, **kwargs):
        if len(value) != self.exact_digits:
            raise ValidationError(self.message)