# Generated by Django 3.0.5 on 2020-09-03 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0026_structure_news_meta_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='structure',
            name='news_meta_code',
        ),
    ]