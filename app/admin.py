from django.contrib import admin
from app.models import *


class Demand_modelsAdmin(admin.ModelAdmin):
    list_display = ('year', 'average_salary', 'average_salary_profession', 'count_vacancies',
                    'count_vacancies_profession')
    list_display_links = ('year',)
    search_fields = ('year',)


class Geography_models_salaryAdmin(admin.ModelAdmin):
    list_display = ('town', 'salary_level')
    list_display_links = ('town',)
    search_fields = ('town',)


class Geography_models_vacancyAdmin(admin.ModelAdmin):
    list_display = ('town', 'vacancy_rate')
    list_display_links = ('town',)
    search_fields = ('town',)


admin.site.register(Demand_models, Demand_modelsAdmin)
admin.site.register(Geography_models_salary, Geography_models_salaryAdmin)
admin.site.register(Geography_models_vacancy, Geography_models_vacancyAdmin)