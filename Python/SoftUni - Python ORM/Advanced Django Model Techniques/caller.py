import os
import django
from django.core.exceptions import ValidationError


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()
