# Generated by Django 5.0.6 on 2024-06-01 14:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentcars', '0005_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(3)])),
                ('phone', models.CharField(max_length=9, validators=[django.core.validators.MinLengthValidator(9)])),
                ('codphone', models.CharField(choices=[('+375', '+375'), ('80', '80')], default='+375', max_length=4)),
                ('ClientChoice', models.CharField(default='Нужна помощь в подборе', max_length=66)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
