from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from Fruitipedia.fruits.forms import CategoryAddForm, AddFruitForm, EditFruitForm, DeleteFruitForm
from Fruitipedia.fruits.models import Fruit


def index(request):
    return render(request, 'common/index.html')


def dashboard(request):
    fruits = Fruit.objects.all()

    context = {
        'fruits': fruits
    }

    return render(request, 'common/dashboard.html', context)


class CreateFruitView(CreateView):
    model = Fruit
    form_class = AddFruitForm
    template_name = 'fruits/create-fruit.html'
    success_url = reverse_lazy('dashboard')


def edit_view(request, id):
    fruit = Fruit.objects.get(id=id)

    if request.method == 'GET':
        form = EditFruitForm(instance=fruit)
    else:
        form = EditFruitForm(request.POST, instance=fruit)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form,
        'fruit': fruit
    }

    return render(request, 'fruits/edit-fruit.html', context)


def details_view(request, id):
    fruit = Fruit.objects.get(id=id)

    context = {
        'fruit': fruit
    }

    return render(request, 'fruits/details-fruit.html', context)


def delete_view(request, id):
    fruit = Fruit.objects.get(id=id)

    if request.method == 'GET':
        form = DeleteFruitForm(instance=fruit)
    else:
        form = DeleteFruitForm(request.POST, instance=fruit)
        fruit.delete()
        return redirect('dashboard')

    context = {
        'form': form,
        'fruit': fruit
    }

    return render(request, 'fruits/delete-fruit.html', context)


def create_category(request):
    if request.method == 'GET':
        form = CategoryAddForm()
    else:
        form = CategoryAddForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'form': form
    }

    return render(request, 'categories/create-category.html', context)
