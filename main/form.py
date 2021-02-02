from django.forms import ModelForm
from main.models import Farmacy


class FarmacyForm(ModelForm):
    use_required_attribute = False

    class Meta:
        model = Farmacy
        exclude = ['name', 'expiration_date', 'temp_from', 'temp_to', 'image']
