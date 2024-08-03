from django.core.exceptions import ValidationError


class DigitOnlyValidator:
    def __init__(self, message: str):
        self.message = message

    def __call__(self, value):
        if not value.isdigit():
            raise ValidationError(self.message)

    def deconstruct(self):
        return (
            'main_app.validators.DigitOnlyValidator',
            (self.message, ),
            {}
        )