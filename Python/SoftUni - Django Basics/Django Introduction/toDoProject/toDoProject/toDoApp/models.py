from django.db import models


class ToDoList(models.Model):
    title = models.CharField(
        max_length=100,
    )

    description = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=True,
    )