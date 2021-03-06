# Generated by Django 2.1.5 on 2019-03-13 04:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0021_auto_20190311_0742'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.localtime)),
            ],
        ),
        migrations.AddField(
            model_name='interviewee',
            name='accepted',
            field=models.BooleanField(default=False),
        ),
    ]
