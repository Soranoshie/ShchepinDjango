from django.db import models


class Profession(models.Model):
    title = models.CharField('Название', max_length=50)
    description = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'


class Demand_models(models.Model):
    year = models.IntegerField('Год', max_length=4)
    average_salary = models.IntegerField('Средняя зарплата', max_length=10)
    average_salary_profession = models.IntegerField('Средняя зарплата - C#', max_length=10)
    count_vacancies = models.IntegerField('Количество вакансий', max_length=7)
    count_vacancies_profession = models.IntegerField('Количество вакансий - C#', max_length=7)

    def __str__(self):
        return str(self.year)

    class Meta:
        verbose_name = 'Востребованность'
        verbose_name_plural = 'Востребованность'


class Geography_models_salary(models.Model):
    town = models.CharField('Город', max_length=20)
    salary_level = models.IntegerField('Уровень зарплат', max_length=10)

    def __str__(self):
        return self.town

    class Meta:
        verbose_name = 'Георграфия - зарплата'
        verbose_name_plural = 'Георграфия - зарплата'


class Geography_models_vacancy(models.Model):
    town = models.CharField('Город', max_length=20)
    vacancy_rate = models.CharField('Доля вакансий', max_length=7)

    def __str__(self):
        return self.town

    class Meta:
        verbose_name = 'Георграфия - вакансии'
        verbose_name_plural = 'Георграфия - вакансии'
