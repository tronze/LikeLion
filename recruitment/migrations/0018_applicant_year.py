# Generated by Django 2.1.5 on 2019-03-09 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0017_applicant_major'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='year',
            field=models.CharField(default='', max_length=8),
        ),
    ]
