# Generated by Django 2.0.5 on 2019-08-07 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_report_categoty'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='categoty',
            new_name='category',
        ),
    ]
