# Generated by Django 4.0.4 on 2022-05-21 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedbacks', '0006_feedbackitemmodel_item'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feedbackmodel',
            options={'verbose_name': 'feedback', 'verbose_name_plural': 'feedbacks'},
        ),
        migrations.AlterField(
            model_name='feedbackmodel',
            name='name',
            field=models.CharField(default='', max_length=40, verbose_name='subject'),
        ),
    ]
