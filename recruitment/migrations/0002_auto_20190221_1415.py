# Generated by Django 2.1.5 on 2019-02-21 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='application',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruitment.Application'),
        ),
    ]
