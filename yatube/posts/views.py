from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template = 'posts/index.html'
    return render(request, template)


def group_list(request):
    template1 = 'posts/group_list.html'
    return render(request, template1)


def group_posts(request, any_slag):
    return HttpResponse('Список мороженого')
