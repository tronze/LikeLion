# Generated by Django 2.1.5 on 2019-03-17 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lisg_calendar', '0002_absent_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='absent',
            name='exemption',
            field=models.BooleanField(default=False),
        ),
    ]
