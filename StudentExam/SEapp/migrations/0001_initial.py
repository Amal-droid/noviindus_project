# Generated by Django 4.0.3 on 2022-05-26 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Examsubjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subject1', models.CharField(max_length=20)),
                ('Subject2', models.CharField(max_length=20)),
                ('Subject3', models.CharField(max_length=20)),
                ('Subject4', models.CharField(max_length=20)),
            ],
        ),
    ]
