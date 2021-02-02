from django.db import models
import os


class Farmacy(models.Model):
    image = models.ImageField(upload_to='main', blank=True, null=True)
    name = models.CharField(verbose_name='Найменування', max_length=100)
    FORM_CHOICE = [('сузпензія оральна', 'сузпензія оральна'),
                   ('капсули', 'капсули'),
                   ('порошок для оральної сузпензії', 'порошок для оральної сузпензії'),
                   ('ліофілізований порошок', 'ліофілізований порошок'),
                   ('таблетки', 'таблетки'),
                   ('краплі', 'краплі'),
                   ('порошок', 'порошок'),
                   ('розчин оральний', 'розчин оральний'),
                   ('краплі оральні', 'краплі оральні')
                   ]
    expiration_date = models.CharField(verbose_name='Термін придатності', max_length=50, blank=True)
    form = models.CharField(verbose_name='Форма випуску', max_length=50, choices=FORM_CHOICE, blank=True)
    temp_from = models.IntegerField(verbose_name='Температура зберігання від', blank=True, null=True)
    temp_to = models.IntegerField(verbose_name='Температура зберігання до', blank=True, null=True)
    MANUFACTURER_CHOICE = [('імпортний', 'імпортний'), ('вітчизняний', 'вітчизняний')]
    manufacturer = models.CharField(verbose_name='Виробник', max_length=50, choices=MANUFACTURER_CHOICE, blank=True)
    CONDITIONS_CHOICE = [('без рецепту', 'без рецепту'), ('за рецептом', 'за рецептом')]
    Vacation_conditions = models.CharField(verbose_name='Умови відпуску', max_length=50, choices=CONDITIONS_CHOICE, blank=True)
    REGISTRATION_CHOICE = [('Лікарський засіб', 'Лікарський засіб'), ('Дієтична добавка', 'Дієтична добавка')]
    registration_form = models.CharField(verbose_name='Форма реєстрації', max_length=50, choices=REGISTRATION_CHOICE,
                                         blank=True)
    adult = models.BooleanField(verbose_name='Для дорослих', default=False)
    children = models.BooleanField(verbose_name='Для дітей', default=False)
    children_age = models.IntegerField(verbose_name='Вік дитини', null=True, blank=True)
    AGE_CHOICE = [('днів', 'днів'), ('місяців', 'місяців'), ('років', 'років')]
    age_choice = models.CharField(verbose_name='Опреділення віку', max_length=50, choices=AGE_CHOICE, blank=True)
    Bacillus_clausii = models.BooleanField(default=False)
    Bacillus_coagulans = models.BooleanField(default=False)
    Bacillus_subtilis = models.BooleanField(default=False)
    Bacillus_licheniformis = models.BooleanField(default=False)
    Bifidobacterium_bifidum = models.BooleanField(default=False)
    Bifidobacterium_breve = models.BooleanField(default=False)
    Bifidobacterhim_laclis = models.BooleanField(default=False)
    Bifidobacterium_BB_12 = models.BooleanField(default=False)
    Bifidobacterium_longum = models.BooleanField(default=False)
    Bifidobacterium_infantis = models.BooleanField(default=False)
    Bifidobacterium_animalis_subsp_lactis = models.BooleanField(default=False)
    Lactobacillus_casei = models.BooleanField(default=False)
    Lactobacillus_salivarius = models.BooleanField(default=False)
    Lactobacillus_plantarum = models.BooleanField(default=False)
    Lactobacillus_delbrueckii = models.BooleanField(default=False)
    Lactobacillus_reuteri = models.BooleanField(default=False)
    Lactobacillus_paracasei = models.BooleanField(default=False)
    Lactobacillus_gasseri = models.BooleanField(default=False)
    Lactobacillus_helveticus_R0052 = models.BooleanField(default=False)
    Lactobacillus_fermentum = models.BooleanField(default=False)
    Lactobacillus_rhamnosus_R0011 = models.BooleanField(default=False)
    Lactobacillus_acidophilus = models.BooleanField(default=False)
    Enterococcus_faecium = models.BooleanField(default=False)
    Saccharomyces_boulardii = models.BooleanField(default=False)
    Escherichia_coli_infv_NISSLE_1917 = models.BooleanField(default=False)
    Streptococcus_thermophilus = models.BooleanField(default=False)
    Streptococcus_salivarius_subsp_Thermophilus = models.BooleanField(default=False)
    a = models.BooleanField(verbose_name='Дисбіоз кишечнику', default=False)
    b = models.BooleanField(verbose_name='Гострі та хронічні шлунково-кишкові захворювання, пов’язані з інтоксикацією',
                            default=False)
    c = models.BooleanField(
        verbose_name='Попередження та лікування діареї, спричиненої застосуванням антибіотиків або інших синтетичних протимікробних препаратів',
        default=False)
    d = models.BooleanField(verbose_name='Гостра вірусна діарея', default=False)
    e = models.BooleanField(verbose_name='Хронічні коліти різної етіології, у тому числі неспецифічні виразкові коліти',
                            default=False)
    f = models.BooleanField(verbose_name='Синдром  подразненого кишечника', default=False)
    g = models.BooleanField(verbose_name='Псевдомембранозний коліт і захворювання, зумовлені Clostridium difficile',
                            default=False)
    h = models.BooleanField(verbose_name='Діарея, пов’язана з довгостроковим ентеральним харчуванням', default=False)
    i = models.BooleanField(verbose_name='Діарея мандрівника', default=False)
    j = models.BooleanField(verbose_name='Профілактика та лікування гострих гастроентеритів у дітей та дорослих', default=False)
    k = models.BooleanField(verbose_name='Неспецифічний виразковий коліт у стадії ремісії', default=False)
    l = models.BooleanField(verbose_name='Хронічні запори', default=False)
    m = models.BooleanField(verbose_name='Підтримуюча терапія при кропив’янці, екземі, дитячому діатезі, атопічному дерматиті',
                            default=False)
    n = models.BooleanField(verbose_name='Профілактика та лікування колітів, пов’язаних з прийомом антибіотиків', default=False)
    o = models.BooleanField(
        verbose_name='В акушерсько-гінекологічній практиці при неспецифічних запальних захворюваннях геніталій та передпологовій підготовці вагітних групи ризику із порушенням чистоти вагінального секрету до III―IV ступеня',
        default=False)
    p = models.BooleanField(
        verbose_name='Лікування транзиторних дисфункцій кишечнику (як діареї, так і запору), пов’язаних зі зміною харчового раціону',
        default=False)
    q = models.BooleanField(
        verbose_name='Порушеннями з боку кишечнику в осіб, які перенесли гострі кишкові інфекції, спричинені патогенними і умовно-патогенними бактеріями',
        default=False)
    r = models.BooleanField(
        verbose_name='У комплексному лікуванні захворювань шлунка і дванадцятипалої кишки, асоційованих із Helicobacter pylori',
        default=False)
    s = models.BooleanField(verbose_name='Діарея у дітей грудного та дошкільного віку, в тому числі при годуванні через зонд',
                            default=False)
    t = models.BooleanField(verbose_name='Для підвищення імунітету новонароджених', default=False)
    u = models.BooleanField(verbose_name='Для профілактики патологічних колонізацій у кишечнику в новонароджених',
                            default=False)
    v = models.BooleanField(verbose_name='Підвищення толерантності до лактози молока', default=False)
    w = models.BooleanField(verbose_name='Гостра та хронічна бактеріальна діарея', default=False)

    def __str__(self):
        return str(self.name)
