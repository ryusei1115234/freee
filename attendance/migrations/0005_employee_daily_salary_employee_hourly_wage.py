# Generated by Django 4.0.2 on 2022-03-07 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0004_employee_transportation_expenses'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='daily_salary',
            field=models.CharField(default=True, max_length=100),
        ),
        migrations.AddField(
            model_name='employee',
            name='hourly_wage',
            field=models.CharField(default=1000, max_length=100),
        ),
    ]
