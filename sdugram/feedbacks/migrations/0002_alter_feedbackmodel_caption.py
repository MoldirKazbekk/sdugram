# Generated by Django 4.0.1 on 2022-03-29 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedbackmodel',
            name='caption',
            field=models.TextField(default='Empty'),
        ),
    ]
