# Generated by Django 3.2.17 on 2023-02-19 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-created_at',)},
        ),
    ]
