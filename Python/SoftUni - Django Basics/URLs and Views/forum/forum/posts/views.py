from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    context = {
        'current_time': datetime.now(),
        "person": {
            "age": 20,
            "height": 190,
        },
        "ids": ["0238543", "6549135", "5421684"],
        "some_text": "Hello there",
        "users": [
            "pesho",
            "dian",
            "ivan",
            "mitko",
            "maria"
        ]
    }

    return render(request, 'base.html', context)


def dashboard(request):
    context = {
        "posts": [
            {
                "title": "How to create django project?",
                "author": "Diyan Kalaydzhiev",
                "content": "I **really** don't how to create a project",
                "created_at": datetime.now(),
            },
            {
                "title": "How to create django project 1?",
                "author": "",
                "content": "### I really don't know how to create a project",
                "created_at": datetime.now(),
            },
            {
                "title": "How to create django project 2?",
                "author": "Diyan Kalaydzhiev",
                "content": "",
                "created_at": datetime.now(),
            },
        ]
    }

    return render(request, 'posts/dashboard.html', context)
