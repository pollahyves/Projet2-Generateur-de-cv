# Generated by Django 4.0 on 2023-01-13 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reunion', '0002_alter_membre_date_naissance_alter_membre_profession'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membre',
            name='nom',
        ),
        migrations.AlterField(
            model_name='membre',
            name='username',
            field=models.CharField(max_length=25, null=True, unique=True),
        ),
    ]
