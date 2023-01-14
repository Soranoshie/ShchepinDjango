from django.shortcuts import render
from .models import *

def index_page(request):
    data = {
        'professions': Profession.objects.get(id=1)
    }
    return render(request, 'app/index.html', context=data)


def demand_page(request):
    data = {
        'professions': Profession.objects.get(id=1)
    }
    return render(request, 'app/demand.html', context=data)


def geography_page(request):
    data = {
        'professions': Profession.objects.get(id=1)
    }
    return render(request, 'app/geography.html', context=data)


def skills_page(request):
    data = {
        'professions': Profession.objects.get(id=1)
    }
    return render(request, 'app/skills.html', context=data)


def recentv_page(request):
    data = {
        'professions': Profession.objects.get(id=1)
    }
    return render(request, 'app/recentv.html', context=data)