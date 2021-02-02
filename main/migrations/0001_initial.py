# Generated by Django 3.1.1 on 2020-09-21 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farmacy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('expiration_date', models.CharField(max_length=50)),
                ('form', models.CharField(choices=[('сузпензія оральна', 'сузпензія оральна'), ('капсули', 'капсули'), ('порошок для оральної сузпензії', 'порошок для оральної сузпензії'), ('ліофілізований порошок', 'ліофілізований порошок'), ('таблетки', 'таблетки'), ('краплі', 'краплі'), ('порошок', 'порошок'), ('розчин оральний', 'розчин оральний'), ('краплі оральні', 'краплі оральні')], max_length=50)),
                ('temp_from', models.IntegerField(default=0)),
                ('temp_to', models.IntegerField(default=0)),
                ('manufacturer', models.CharField(choices=[('імпортний', 'імпортний'), ('вітчизняний', 'вітчизняний')], max_length=50)),
                ('Vacation_conditions', models.CharField(choices=[('без рецепту', 'без рецепту'), ('за рецептом', 'за рецептом')], max_length=50)),
                ('registration_form', models.CharField(choices=[('Лікарський засіб', 'Лікарський засіб'), ('Дієтична добавка', 'Дієтична добавка')], max_length=50)),
                ('adult', models.BooleanField(default=False)),
                ('children', models.BooleanField(default=False)),
                ('children_age', models.IntegerField(blank=True, null=True)),
                ('age_choice', models.CharField(choices=[('днів', 'днів'), ('місяців', 'місяців'), ('років', 'років')], max_length=50)),
            ],
        ),
    ]
