# Generated by Django 2.1.5 on 2019-03-27 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0010_assignmentsubmitinformation_field_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignmentsubmitinformation',
            name='language',
            field=models.PositiveSmallIntegerField(choices=[(1, 'HTML'), (2, 'CSS'), (3, 'Python'), (4, '일반 텍스트'), (5, '링크'), (6, '이미지')]),
        ),
    ]