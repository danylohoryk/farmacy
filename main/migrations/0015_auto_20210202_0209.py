# Generated by Django 3.1.6 on 2021-02-02 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_auto_20210202_0208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmacy',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Найменування'),
        ),
    ]
