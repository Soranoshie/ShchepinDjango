from django.shortcuts import render
from .api import *
from .models import *
from datetime import datetime


def index(request):
    return render(request, 'app/index.html', {'title': "Профессия C#-программиста"})


def demand(request):
    db_headers = ["Год", "Средняя зарплата", "Средняя зарплата - C#", "Количество вакансий", "Количество вакансий - C#"]
    db = Demand_models.objects.all()
    return render(request, 'app/demand.html',  {'title': "Востребованность", 'db': db, 'db_headers': db_headers})


def geography(request):
    db_headers_salary = ["Город", "Уровень зарплат"]
    db_headers_vacancy = ["Город", "Доля вакансий"]
    db_salary = Geography_models_salary.objects.all()
    db_vacancy = Geography_models_vacancy.objects.all()
    return render(request, 'app/geography.html', {'title': "География", 'db_salary': db_salary,
                'db_vacancy': db_vacancy, 'db_headers_salary': db_headers_salary,
                'db_headers_vacancy': db_headers_vacancy})


def skills(request):
    return render(request, 'app/skills.html', {'title': "Навыки"})


def recentv(request):
    vacancy = VacancyParser.get_vacancies_by_date()[:10]

    return render(request, 'app/recentv.html', {'title': "Последние вакансии", 'vacancy': vacancy})