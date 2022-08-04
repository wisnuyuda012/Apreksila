# Generated by Django 3.2 on 2022-05-17 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='prediksi_usiaKelahiran',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tek_darah', models.IntegerField(choices=[(1, 'tinggi'), (2, 'rendah'), (3, 'normal')])),
                ('r_persalinan', models.IntegerField(choices=[(1, 'Riwayat Persalinan Premature'), (2, 'Riwayat Persalinan Postdate'), (3, 'Riwayat Persalinan Caecar'), (4, 'Tidak Ada'), (5, 'Riwayat Persalinan Normal')])),
                ('r_abortus', models.IntegerField(choices=[(1, 'Ada'), [2, 'Tidak Ada']])),
                ('malnutrisi', models.IntegerField(choices=[(1, 'Kurang'), (2, 'Lebih'), (3, 'Normal')])),
                ('peny_lain', models.IntegerField(choices=[(1, 'Anemia'), (2, 'Hipertensi'), (3, 'Diabetes'), (4, 'Jantung'), (5, 'Asma'), (6, 'HIV'), (7, 'Tidak Ada')])),
                ('masalah_saathamil', models.IntegerField(choices=[(1, 'Perdarahan'), (2, 'Pre Eklamsia Berat'), (3, 'Pre Eklamsia Ringan'), (4, 'Hipertensi Gestasional'), (5, 'Tidak Ada')])),
                ('usia_kelahiran', models.IntegerField(choices=[(1, 'Premature'), (2, 'Postmature'), (3, 'Normal')])),
            ],
            options={
                'db_table': 'prediksi_usiaKelahiran',
            },
        ),
    ]
