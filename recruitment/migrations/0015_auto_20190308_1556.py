# Generated by Django 2.1.5 on 2019-03-08 06:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0014_evaluationquestion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answerevaluation',
            name='score',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)]),
        ),
    ]
