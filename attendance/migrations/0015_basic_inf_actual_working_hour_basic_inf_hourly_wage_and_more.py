# Generated by Django 4.0.2 on 2022-03-07 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0014_remove_basic_inf_actual_working_hour_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='basic_inf',
            name='actual_working_hour',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='basic_inf',
            name='hourly_wage',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='basic_inf',
            name='sum_pay',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='basic_inf',
            name='transportation_expenses',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
