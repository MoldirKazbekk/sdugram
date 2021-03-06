# Generated by Django 4.0.2 on 2022-03-18 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=65, null=True)),
                ('password', models.CharField(max_length=150, null=True)),
                ('firstName', models.CharField(max_length=200, null=True)),
                ('lastName', models.CharField(max_length=200, null=True)),
                ('age', models.IntegerField(null=True)),
                ('phone', models.CharField(max_length=12, null=True)),
                ('city', models.CharField(max_length=40, null=True)),
                ('photo', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]
