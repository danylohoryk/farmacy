# Generated by Django 3.1.1 on 2020-12-14 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20201122_1607'),
    ]

    operations = [
        migrations.DeleteModel(
            name='File',
        ),
        migrations.AlterField(
            model_name='farmacy',
            name='Виробник',
            field=models.CharField(blank=True, choices=[('імпортний', 'імпортний'), ('вітчизняний', 'вітчизняний')], max_length=50),
        ),
        migrations.AlterField(
            model_name='farmacy',
            name='Опреділення віку',
            field=models.CharField(blank=True, choices=[('днів', 'днів'), ('місяців', 'місяців'), ('років', 'років')], max_length=50),
        ),
        migrations.AlterField(
            model_name='farmacy',
            name='Умови відпуску',
            field=models.CharField(blank=True, choices=[('без рецепту', 'без рецепту'), ('за рецептом', 'за рецептом')], max_length=50),
        ),
        migrations.AlterField(
            model_name='farmacy',
            name='Форма випуску',
            field=models.CharField(blank=True, choices=[('сузпензія оральна', 'сузпензія оральна'), ('капсули', 'капсули'), ('порошок для оральної сузпензії', 'порошок для оральної сузпензії'), ('ліофілізований порошок', 'ліофілізований порошок'), ('таблетки', 'таблетки'), ('краплі', 'краплі'), ('порошок', 'порошок'), ('розчин оральний', 'розчин оральний'), ('краплі оральні', 'краплі оральні')], max_length=50),
        ),
        migrations.AlterField(
            model_name='farmacy',
            name='Форма реєстрації',
            field=models.CharField(blank=True, choices=[('Лікарський засіб', 'Лікарський засіб'), ('Дієтична добавка', 'Дієтична добавка')], max_length=50),
        ),
    ]
