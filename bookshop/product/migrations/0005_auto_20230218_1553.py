# Generated by Django 3.2.17 on 2023-02-18 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20230218_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='isbn',
        ),
        migrations.AddField(
            model_name='product',
            name='isbn13',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]