from django.contrib import admin
from .models import prediksi_usiaKelahiran
# Register your models here.

@admin.register(prediksi_usiaKelahiran)
class prediksi_usiaKelahiranAdmin(admin.ModelAdmin):
    list_display = ('tek_darah', 'r_persalinan', 'r_abortus', 'malnutrisi', 'peny_lain', 'masalah_saathamil', 'usia_kelahiran')
    search_fields = ('usia_kelahiran', 'tek_darah')