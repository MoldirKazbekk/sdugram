# Generated by Django 4.0.2 on 2022-04-22 16:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_messages_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='date',
            field=models.DateTimeField(verbose_name=datetime.datetime(2022, 4, 22, 16, 59, 13, 542185)),
        ),
    ]
