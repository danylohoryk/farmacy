from django.shortcuts import render
from .form import FarmacyForm
from .models import Farmacy
from django.http import HttpResponse


def index(request):
    form = FarmacyForm(request.POST or None)
    farmacy = Farmacy.objects.all()
    filter_dict = {}
    if request.method == 'POST':
        for i in request.POST:
            filter_dict[i] = request.POST.get(i)
            if filter_dict[i] == '':
                del filter_dict[i]
        del filter_dict['csrfmiddlewaretoken']
        farmacy = Farmacy.objects.filter(**filter_dict)
        return render(request, 'main.html', {'form': form, 'farmacy': farmacy})
    return render(request, 'main.html', {'form': form, 'farmacy': farmacy})
