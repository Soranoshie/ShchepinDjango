# Generated by Django 4.1.5 on 2023-01-16 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demand_models',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(max_length=4, verbose_name='Год')),
                ('average_salary', models.IntegerField(max_length=10, verbose_name='Средняя зарплата')),
                ('average_salary_profession', models.IntegerField(max_length=10, verbose_name='Средняя зарплата')),
                ('count_vacancies', models.IntegerField(max_length=7, verbose_name='Количество вакансий')),
                ('count_vacancies_profession', models.IntegerField(max_length=7, verbose_name='Количество вакансий - C#')),
            ],
            options={
                'verbose_name': 'География',
            },
        ),
        migrations.AlterModelOptions(
            name='profession',
            options={'verbose_name': 'Профессия', 'verbose_name_plural': 'Профессии'},
        ),
    ]
