# Generated by Django 5.0.6 on 2024-06-02 04:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rentcars', '0007_alter_userclient_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userclient',
            name='codphone',
        ),
    ]
