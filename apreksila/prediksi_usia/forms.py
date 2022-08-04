
from django import forms



from .models import prediksi_usiaKelahiran

class prediksi_usiaKelahiranForm(forms.ModelForm):
    class Meta:
        model= prediksi_usiaKelahiran
        fields=['tek_darah', 'r_persalinan', 'r_abortus', 'malnutrisi', 'peny_lain', 'masalah_saathamil']
