# Generated by Django 2.2.6 on 2019-10-04 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdflist', '0003_auto_20191004_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdffile',
            name='item_slug',
            field=models.CharField(blank=True, max_length=254, unique=True),
        ),
    ]
