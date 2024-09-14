from django.contrib import admin

from toDoProject.toDoApp.models import ToDoList


@admin.register(ToDoList)
class ToDoListAdmin(admin.ModelAdmin):
    pass
