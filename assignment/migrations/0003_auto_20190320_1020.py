# Generated by Django 2.1.5 on 2019-03-20 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0002_submit_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submit',
            name='language',
            field=models.PositiveSmallIntegerField(choices=[(1, 'HTML'), (2, 'CSS'), (3, 'Python'), (4, 'Normal Text')]),
        ),
    ]
