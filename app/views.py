from django.shortcuts import render
from .models import *


def index(request):
    return render(request, 'app/index.html', {'title': "Профессия C#-программиста"})
    # data = {
    #     'professions': Profession.objects.get(id=1)
    # }
    # return render(request, 'app/index.html', context=data)


def demand(request):
    return render(request, 'app/demand.html', {'title': "Востребованность"})
    # data = {
    #     'professions': Profession.objects.get(id=1)
    # }
    # return render(request, 'app/demand.html', context=data)


def geography(request):
    return render(request, 'app/geography.html', {'title': "География"})
    # data = {
    #     'professions': Profession.objects.get(id=1)
    # }
    # return render(request, 'app/geography.html', context=data)


def skills(request):
    return render(request, 'app/skills.html', {'title': "Навыки"})
    # data = {
    #     'professions': Profession.objects.get(id=1)
    # }
    # return render(request, 'app/skills.html', context=data)


def recentv(request):
    return render(request, 'app/recentv.html', {'title': "Последние вакансии"})
    # data = {
    #     'professions': Profession.objects.get(id=1)
    # }
    # return render(request, 'app/recentv.html', context=data)