# Generated by Django 3.0.5 on 2020-11-27 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0038_auto_20201127_1746'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='url',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='page',
            name='url',
            field=models.CharField(max_length=2000, unique=True),
        ),
    ]