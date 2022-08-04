from django.shortcuts import render
from prediksi_usia.models import prediksi_usiaKelahiran

def index(request):
    return render(request, 'index.html')

def guide(request):
    return render(request, 'guide.html')
