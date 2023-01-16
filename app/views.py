from django.shortcuts import render
from .models import *


def index(request):
    return render(request, 'app/index.html', {'title': "Профессия C#-программиста"})


def demand(request):
    db_headers = ["Год", "Средняя зарплата", "Средняя зарплата - C#", "Количество вакансий", "Количество вакансий - C#"]
    db = Demand_models.objects.all()
    return render(request, 'app/demand.html',  {'title': "Востребованность", 'db': db, 'db_headers': db_headers})


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