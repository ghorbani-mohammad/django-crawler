# Generated by Django 3.0.5 on 2020-06-28 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0007_auto_20200528_0231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agencypagestructure',
            name='last_crawl',
            field=models.DateTimeField(null=True),
        ),
    ]
