# Generated by Django 3.1.6 on 2021-02-02 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20210202_0201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='farmacy',
            name='В акушерсько-гінекологічній практиці при неспецифічних запальних захворюваннях геніталій та передпологовій підготовці вагітних групи ризику із порушенням чистоти вагінального секрету до III―IV ступеня',
        ),
        migrations.RemoveField(
            model_name='farmacy',
            name='Виробник',
        ),
        migrations.RemoveField(
            model_name='farmacy',
            name='Вік дитини',
        ),
        migrations.RemoveField(
            model_name='farmacy',
            name='Гостра вірусна діарея',
        ),
        migrations.RemoveField(
            model_name='farmacy',
            name='Гостра та хронічна бактеріальна діарея',
        ),
        migrations.RemoveField(
            model_name='farmacy',
            name='Гострі та хронічні шлунково-кишкові захворювання, пов’язані з інтоксикацією',
        ),
        migrations.RemoveField(
            model_name='farmacy',
            name='Дисбіоз кишечнику',
        ),
        migrations.RemoveField(
            model_name='farmacy',
            name='Для дорослих',
        ),
        migrations.RemoveField(
            model_name='farmacy',
            name='Для дітей',
        ),
        migrations.RemoveField(
            model_name='farmacy',
            name='Для профілактики патологічних колонізацій у кишечнику в новонароджених',
        ),
        migrations.RemoveField(
            model_name='farmacy',
            name='Для підвищення імунітету новонароджених',
        ),
        migrations.RemoveField(
            model_name='farmacy',
            name='Діарея мандрівника',
        ),
        migrations.RemoveField(
            model_name='farmacy',
            name='Діарея у дітей грудного та дошкільного віку, в тому числі при годуванні через зонд',
        ),
        migrations.RemoveField(
            model_name='farmacy',
            name='Діарея, пов’язана з довгостроковим ентеральним харчуванням',
        ),
        migrations.RemoveField(
            model_name='farmacy',
            name='Лікування транзиторних дисфункцій кишечнику (як діареї, так і запору), пов’язаних зі зміною харчового раціону',
        ),
        migrations.RemoveField(
            model_name='farmacy',
            name='Неспецифічний виразковий коліт у стадії ремісії',
        ),
        migrations.RemoveField(
            model_name='farmacy',
            name='Опреділення віку',
        ),
        migrations.RemoveField(
            model_name='farmacy',
            name='Попередження та лікування діареї, спричиненої застосуванням антибіотиків або інших синтетичних протимікробних препаратів',
        ),
        migrations.RemoveField(
            model_name='farmacy',
            name='Порушеннями з боку кишечнику в осіб, які перенесли гострі кишкові інфекції, спричинені патогенними і умовно-патогенними бактеріями',
        ),
        migrations.RemoveField(
            model_name='farmacy',
            name='Профілактика та лікування гострих гастроентеритів у дітей та дорослих',
        ),
        migrations.RemoveField(
            model_name='farmacy',
            name='Профілактика та лікування колітів, пов’язаних з прийомом антибіотиків',
        ),
        migrations.RemoveField(
            model_name='farmacy',
            name='Псевдомембранозний коліт і захворювання, зумовлені Clostridium difficile',
        ),
        migrations.RemoveField(
            model_name='farmacy',
            name='Підвищення толерантності до лактози молока',
        ),
        migrations.RemoveField(
            model_name='farmacy',
            name='Підтримуюча терапія при кропив’янці, екземі, дитячому діатезі, атопічному дерматиті',
        ),
        migrations.RemoveField(
            model_name='farmacy',
            name='Синдром  подразненого кишечника',
        ),
        migrations.RemoveField(
            model_name='farmacy',
            name='Температура зберігання від',
        ),
        migrations.RemoveField(
            model_name='farmacy',
            name='Температура зберігання до',
        ),
        migrations.RemoveField(
            model_name='farmacy',
            name='Термін придатності',
        ),
        migrations.RemoveField(
            model_name='farmacy',
            name='У комплексному лікуванні захворювань шлунка і дванадцятипалої кишки, асоційованих із Helicobacter pylori',
        ),
        migrations.RemoveField(
            model_name='farmacy',
            name='Умови відпуску',
        ),
        migrations.RemoveField(
            model_name='farmacy',
            name='Форма випуску',
        ),
        migrations.RemoveField(
            model_name='farmacy',
            name='Форма реєстрації',
        ),
        migrations.RemoveField(
            model_name='farmacy',
            name='Хронічні запори',
        ),
        migrations.RemoveField(
            model_name='farmacy',
            name='Хронічні коліти різної етіології, у тому числі неспецифічні виразкові коліти',
        ),
        migrations.AddField(
            model_name='farmacy',
            name='Vacation_conditions',
            field=models.CharField(blank=True, choices=[('без рецепту', 'без рецепту'), ('за рецептом', 'за рецептом')], max_length=50, verbose_name='Умови відпуску'),
        ),
        migrations.AddField(
            model_name='farmacy',
            name='a',
            field=models.BooleanField(default=False, verbose_name='Дисбіоз кишечнику'),
        ),
        migrations.AddField(
            model_name='farmacy',
            name='adult',
            field=models.BooleanField(default=False, verbose_name='Для дорослих'),
        ),
        migrations.AddField(
            model_name='farmacy',
            name='age_choice',
            field=models.CharField(blank=True, choices=[('днів', 'днів'), ('місяців', 'місяців'), ('років', 'років')], max_length=50, verbose_name='Опреділення віку'),
        ),
        migrations.AddField(
            model_name='farmacy',
            name='b',
            field=models.BooleanField(default=False, verbose_name='Гострі та хронічні шлунково-кишкові захворювання, пов’язані з інтоксикацією'),
        ),
        migrations.AddField(
            model_name='farmacy',
            name='c',
            field=models.BooleanField(default=False, verbose_name='Попередження та лікування діареї, спричиненої застосуванням антибіотиків або інших синтетичних протимікробних препаратів'),
        ),
        migrations.AddField(
            model_name='farmacy',
            name='children',
            field=models.BooleanField(default=False, verbose_name='Для дітей'),
        ),
        migrations.AddField(
            model_name='farmacy',
            name='children_age',
            field=models.IntegerField(blank=True, null=True, verbose_name='Вік дитини'),
        ),
        migrations.AddField(
            model_name='farmacy',
            name='d',
            field=models.BooleanField(default=False, verbose_name='Гостра вірусна діарея'),
        ),
        migrations.AddField(
            model_name='farmacy',
            name='e',
            field=models.BooleanField(default=False, verbose_name='Хронічні коліти різної етіології, у тому числі неспецифічні виразкові коліти'),
        ),
        migrations.AddField(
            model_name='farmacy',
            name='expiration_date',
            field=models.CharField(blank=True, max_length=50, verbose_name='Термін придатності'),
        ),
        migrations.AddField(
            model_name='farmacy',
            name='f',
            field=models.BooleanField(default=False, verbose_name='Синдром  подразненого кишечника'),
        ),
        migrations.AddField(
            model_name='farmacy',
            name='form',
            field=models.CharField(blank=True, choices=[('сузпензія оральна', 'сузпензія оральна'), ('капсули', 'капсули'), ('порошок для оральної сузпензії', 'порошок для оральної сузпензії'), ('ліофілізований порошок', 'ліофілізований порошок'), ('таблетки', 'таблетки'), ('краплі', 'краплі'), ('порошок', 'порошок'), ('розчин оральний', 'розчин оральний'), ('краплі оральні', 'краплі оральні')], max_length=50, verbose_name='Форма випуску'),
        ),
        migrations.AddField(
            model_name='farmacy',
            name='g',
            field=models.BooleanField(default=False, verbose_name='Псевдомембранозний коліт і захворювання, зумовлені Clostridium difficile'),
        ),
        migrations.AddField(
            model_name='farmacy',
            name='h',
            field=models.BooleanField(default=False, verbose_name='Діарея, пов’язана з довгостроковим ентеральним харчуванням'),
        ),
        migrations.AddField(
            model_name='farmacy',
            name='i',
            field=models.BooleanField(default=False, verbose_name='Діарея мандрівника'),
        ),
        migrations.AddField(
            model_name='farmacy',
            name='j',
            field=models.BooleanField(default=False, verbose_name='Профілактика та лікування гострих гастроентеритів у дітей та дорослих'),
        ),
        migrations.AddField(
            model_name='farmacy',
            name='k',
            field=models.BooleanField(default=False, verbose_name='Неспецифічний виразковий коліт у стадії ремісії'),
        ),
        migrations.AddField(
            model_name='farmacy',
            name='l',
            field=models.BooleanField(default=False, verbose_name='Хронічні запори'),
        ),
        migrations.AddField(
            model_name='farmacy',
            name='m',
            field=models.BooleanField(default=False, verbose_name='Підтримуюча терапія при кропив’янці, екземі, дитячому діатезі, атопічному дерматиті'),
        ),
        migrations.AddField(
            model_name='farmacy',
            name='manufacturer',
            field=models.CharField(blank=True, choices=[('імпортний', 'імпортний'), ('вітчизняний', 'вітчизняний')], max_length=50, verbose_name='Виробник'),
        ),
        migrations.AddField(
            model_name='farmacy',
            name='n',
            field=models.BooleanField(default=False, verbose_name='Профілактика та лікування колітів, пов’язаних з прийомом антибіотиків'),
        ),
        migrations.AddField(
            model_name='farmacy',
            name='o',
            field=models.BooleanField(default=False, verbose_name='В акушерсько-гінекологічній практиці при неспецифічних запальних захворюваннях геніталій та передпологовій підготовці вагітних групи ризику із порушенням чистоти вагінального секрету до III―IV ступеня'),
        ),
        migrations.AddField(
            model_name='farmacy',
            name='p',
            field=models.BooleanField(default=False, verbose_name='Лікування транзиторних дисфункцій кишечнику (як діареї, так і запору), пов’язаних зі зміною харчового раціону'),
        ),
        migrations.AddField(
            model_name='farmacy',
            name='q',
            field=models.BooleanField(default=False, verbose_name='Порушеннями з боку кишечнику в осіб, які перенесли гострі кишкові інфекції, спричинені патогенними і умовно-патогенними бактеріями'),
        ),
        migrations.AddField(
            model_name='farmacy',
            name='r',
            field=models.BooleanField(default=False, verbose_name='У комплексному лікуванні захворювань шлунка і дванадцятипалої кишки, асоційованих із Helicobacter pylori'),
        ),
        migrations.AddField(
            model_name='farmacy',
            name='registration_form',
            field=models.CharField(blank=True, choices=[('Лікарський засіб', 'Лікарський засіб'), ('Дієтична добавка', 'Дієтична добавка')], max_length=50, verbose_name='Форма реєстрації'),
        ),
        migrations.AddField(
            model_name='farmacy',
            name='s',
            field=models.BooleanField(default=False, verbose_name='Діарея у дітей грудного та дошкільного віку, в тому числі при годуванні через зонд'),
        ),
        migrations.AddField(
            model_name='farmacy',
            name='t',
            field=models.BooleanField(default=False, verbose_name='Для підвищення імунітету новонароджених'),
        ),
        migrations.AddField(
            model_name='farmacy',
            name='temp_from',
            field=models.IntegerField(default=0, verbose_name='Температура зберігання від'),
        ),
        migrations.AddField(
            model_name='farmacy',
            name='temp_to',
            field=models.IntegerField(default=0, verbose_name='Температура зберігання до'),
        ),
        migrations.AddField(
            model_name='farmacy',
            name='u',
            field=models.BooleanField(default=False, verbose_name='Для профілактики патологічних колонізацій у кишечнику в новонароджених'),
        ),
        migrations.AddField(
            model_name='farmacy',
            name='v',
            field=models.BooleanField(default=False, verbose_name='Підвищення толерантності до лактози молока'),
        ),
        migrations.AddField(
            model_name='farmacy',
            name='w',
            field=models.BooleanField(default=False, verbose_name='Гостра та хронічна бактеріальна діарея'),
        ),
        migrations.AlterField(
            model_name='farmacy',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Найменування ш'),
        ),
    ]
