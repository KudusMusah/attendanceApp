# Generated by Django 4.2.2 on 2023-08-27 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_alter_attendance_check_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='check_in',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
