from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic import (
    CreateView,
    TemplateView,
    ListView,
    UpdateView,
    DeleteView,
)
from .models import Vivero
from .forms import (
    DepartamentoMunicipioVivero,
    FormularioVivero,
    FormularioMunicipio,
    FormularioDepartamento,
)


# Create your views here.
