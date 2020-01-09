

from django.shortcuts import render
import pickle
import os

# Create your views here.
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from text.models import HousingData
from text.forms import HousingDataForm

def HousingDataCreateView(request):

    if request.method == "POST":
        form = HousingDataForm(request.POST)

        if form.is_valid():
            X = list(form.cleaned_data.values())
            print([X])
            cwd = os.getcwd()
            filename = os.path.join(cwd, 'text', 'mlmodels', 'boston_final_model.sav')
            loaded_model = pickle.load(open(filename, 'rb'))
            result = loaded_model.predict([X])

        return render(request, 'text/housingdata_result.html', {'result': result})

    else:
        form = HousingDataForm()
        return render(request, 'text/housingdata_form.html', {'form': form})

def TextModelsView(request):
    return render(request, 'text/text.html')

#def HousingDataCreateView(CreateView):
#    model = HousingData
#    form_class = HousingDataForm

#    template_name = 'text/housingdata_form.html'

