# Generated by Django 3.2.7 on 2021-09-13 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20210913_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(null=True, verbose_name='Срок выполнения'),
        ),
    ]
