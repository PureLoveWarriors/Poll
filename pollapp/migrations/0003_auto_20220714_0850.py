# Generated by Django 3.2.6 on 2022-07-14 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollapp', '0002_auto_20220714_0849'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='updated_datetime',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='created_datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
