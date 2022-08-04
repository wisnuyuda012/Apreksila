from django.db import models

# Create your models here.
class prediksi_usiaKelahiran(models.Model):
    TINGGI = 1
    RENDAH = 2
    NORMAL = 3

    OPSI_TEKANAN_DARAH = [
        (TINGGI, 'tinggi'),
        (RENDAH, 'rendah'),
        (NORMAL, 'normal'),
    ]

    tek_darah= models.IntegerField(choices=OPSI_TEKANAN_DARAH)
    PREMATURE = 1
    POSTDATE = 2
    CAECAR = 3
    BELUM = 4
    NORMAL = 5

    OPSI_PERSALINAN=[
        (PREMATURE, 'Riwayat Persalinan Premature'),
        (POSTDATE, 'Riwayat Persalinan Postdate'),
        (CAECAR, 'Riwayat Persalinan Caecar'),
        (BELUM, 'Tidak Ada'),
        (NORMAL, 'Riwayat Persalinan Normal'),
    ]
    r_persalinan=models.IntegerField(choices=OPSI_PERSALINAN)

    ADA=1
    TIDAK=2
    OPSI_ABORTUS=[
        (ADA, 'Ada'),
        [TIDAK, 'Tidak Ada']
    ]
    r_abortus=models.IntegerField(choices=OPSI_ABORTUS)
    KURANG = 1
    LEBIH = 2
    NORMAL = 3

    OPSI_MALNUTRISI=[
        (KURANG, 'Kurang'),
        (LEBIH, 'Lebih'),
        (NORMAL, 'Normal'),
    ]
    malnutrisi=models.IntegerField(choices=OPSI_MALNUTRISI)
    
    ANEMIA=1
    HIPERTENSI=2
    DIABETES=3
    JANTUNG=4
    ASMA=5
    HIV=6 
    TIDAK=7 
    OPSI_PENYAKIT=[
        (ANEMIA, 'Anemia'),
        (HIPERTENSI,'Hipertensi'),
        (DIABETES, 'Diabetes'),
        (JANTUNG, 'Jantung'),
        (ASMA, 'Asma'),
        (HIV, 'HIV'),
        (TIDAK,'Tidak Ada'),
    ]
    peny_lain=models.IntegerField(choices=OPSI_PENYAKIT)

    PERDARAHAN=1
    PREEKLAMSIA_BERAT=2
    PREEKLAMSIA_RINGAN=3 
    HIPERTENSI_GESTASIONAL=4 
    TIDAK_ADA=5 

    OPSI_MASALAH_HAMIL=[
        (PERDARAHAN, 'Perdarahan'),
        (PREEKLAMSIA_BERAT, 'Pre Eklamsia Berat'),
        (PREEKLAMSIA_RINGAN,'Pre Eklamsia Ringan'),
        (HIPERTENSI_GESTASIONAL,'Hipertensi Gestasional'),
        (TIDAK_ADA, 'Tidak Ada'),
    ]
    masalah_saathamil=models.IntegerField(choices=OPSI_MASALAH_HAMIL)
    PREMATURE='Premature'
    POSTMATURE='Postmature'
    NORMAL='Normal'
    OPSI_USIAKELAHIRAN=[
        (PREMATURE,'Premature'),
        (POSTMATURE,'Postmature'),
        (NORMAL, 'Normal'),
    ]
    usia_kelahiran=models.CharField(
        max_length=10,
        choices=OPSI_USIAKELAHIRAN, default=NORMAL)



    class Meta:
        db_table = 'prediksi_usiaKelahiran'

    def __str__(self):
        return self.usia_kelahiran