from django.shortcuts import render

from toDoProject.toDoApp.models import ToDoList


def index_view(request):
    title_filter = request.GET.get('title_filter', '')

    tasks = ToDoList.objects.filter(title__icontains=title_filter)

    context = {
        'title_filter': title_filter,
        'tasks': tasks,
    }

    return render(request, 'index.html', context)