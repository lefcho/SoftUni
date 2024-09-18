from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from urlsAndViews.uavApp.models import Department


def index(request):
    return HttpResponse("<h1>Hello</h1>")


def view_with_name(request, variable):
    return render(request, 'name_template.html', {'variable': variable})


def view_with_args_and_kwargs(request, *args, **kwargs):
    return HttpResponse(f"<h1>Args: {args}, Kwargs: {kwargs}</h1>")


def view_with_pk(request, pk):
    return JsonResponse({'pk': pk})


def slug_view(request, pk, slug):
    # department = Department.objects.filter(pk=pk, slug=slug)
    #
    # if not department:
    #     raise Http404

    department = get_object_or_404(Department, pk=pk, slug=slug)

    return HttpResponse(f"<h1>Department from slug: {department}</h1>")


def show_archive(request, archive_year):
    return HttpResponse(f"<h1>Chosen year: {archive_year}</h1>")


def redirect_to_softuni(request):
    return redirect('https://softuni.bg')


def redirect_view(request):
    return redirect('primary', pk=1)
