# Generated by Django 4.1.5 on 2023-01-16 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_demand_models_alter_profession_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='demand_models',
            options={'verbose_name': 'Востребованность', 'verbose_name_plural': 'Востребованность'},
        ),
        migrations.AlterField(
            model_name='demand_models',
            name='average_salary_profession',
            field=models.IntegerField(max_length=10, verbose_name='Средняя зарплата - C#'),
        ),
    ]