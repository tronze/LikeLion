# Generated by Django 2.1.5 on 2019-03-09 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0016_applicant_links'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='major',
            field=models.CharField(default='', max_length=100),
        ),
    ]
