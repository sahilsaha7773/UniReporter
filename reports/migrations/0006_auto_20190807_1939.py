# Generated by Django 2.0.5 on 2019-08-07 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0005_auto_20190807_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='category',
            field=models.CharField(choices=[('story', 'Story'), ('report', 'Reports'), ('poems', 'Poems'), ('art', 'Art')], default='report', max_length=100),
        ),
    ]
