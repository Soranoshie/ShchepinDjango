# Generated by Django 4.1.5 on 2023-01-16 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_geography_models_salary_geography_models_vacancy'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profession',
        ),
        migrations.AlterModelOptions(
            name='demand_models',
            options={'ordering': ['year', 'average_salary', 'average_salary_profession', 'count_vacancies', 'count_vacancies_profession'], 'verbose_name': 'Востребованность', 'verbose_name_plural': 'Востребованность'},
        ),
    ]
