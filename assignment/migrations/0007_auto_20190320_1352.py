# Generated by Django 2.1.5 on 2019-03-20 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0006_submitimage_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submit',
            name='language',
            field=models.PositiveSmallIntegerField(choices=[(1, 'HTML'), (2, 'CSS'), (3, 'Python'), (4, '일반 텍스트'), (5, '링크'), (6, '이미지')]),
        ),
    ]
