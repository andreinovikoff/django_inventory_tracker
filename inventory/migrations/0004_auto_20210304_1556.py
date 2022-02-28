# Generated by Django 3.1.7 on 2021-03-04 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_auto_20210304_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='title',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]