# Generated by Django 4.2.2 on 2023-08-24 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_leave_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='leave',
            name='start_date',
            field=models.DateField(),
        ),
    ]
