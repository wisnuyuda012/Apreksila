
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='form_prediksi'),
    path('prediksi/', views.index, name='form_prediksi'),
    path('results/', views.prediksi_usia, name='submit_predict'),
]

