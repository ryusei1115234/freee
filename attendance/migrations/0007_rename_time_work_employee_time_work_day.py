# Generated by Django 4.0.2 on 2022-03-07 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0006_rename_daily_salary_employee_time_work'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='time_work',
            new_name='time_work_day',
        ),
    ]