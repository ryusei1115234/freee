# Generated by Django 4.0.2 on 2022-03-07 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0013_basic_inf_alter_employee_hourly_wage_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basic_inf',
            name='actual_working_hour',
        ),
        migrations.RemoveField(
            model_name='basic_inf',
            name='hourly_wage',
        ),
        migrations.RemoveField(
            model_name='basic_inf',
            name='sum_pay',
        ),
        migrations.RemoveField(
            model_name='basic_inf',
            name='transportation_expenses',
        ),
    ]
