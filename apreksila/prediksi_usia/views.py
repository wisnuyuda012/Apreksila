from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from .models import prediksi_usiaKelahiran
from apreksila.settings import DATABASES
import os
from apreksila.settings import BASE_DIR

##classify
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, f1_score
from sklearn.svm import SVC
import pandas as pd
import pickle

def index(request):
    return render(request, 'prediksi_usia/index.html')

def prediksi_usia(request):

    with open(os.path.join(BASE_DIR, 'dataset 260.csv'), "rb") as f:
             df = pd.read_csv(f)
        #Make Prediction

    X = df[['tek_darah', 'r_persalinan', 'r_abortus', 'malnutrisi', 'peny_lain', 'masalah_saathamil']]
    y = df['usia_kelahiran']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=110, random_state=1)

    model1 = svm.SVC(kernel='rbf')
    model1.fit(X,y)
    y_pred = model1.predict(X_test)

    hasil = classification_report(y_test, y_pred, output_dict=True)

    hasil_precision1 = '%.2f'%hasil['Normal']['precision']
    hasil_precision2 = '%.2f'%hasil['Premature']['precision']
    hasil_precision3 = '%.2f'%hasil['Postmature']['precision']
    hasil_recall1 = '%.2f'%hasil['Normal']['recall']
    hasil_recall2 = '%.2f'%hasil['Premature']['recall']
    hasil_recall3 = '%.2f'%hasil['Postmature']['recall']
    hasil_f1score1 = '%.2f'%hasil['Normal']['f1-score']
    hasil_f1score2 = '%.2f'%hasil['Premature']['f1-score']
    hasil_f1score3 = '%.2f'%hasil['Postmature']['f1-score']
    hasil_acuracy = '%.2f'%hasil['accuracy']

    hasil_avgscore1 = '%.2f'%hasil['macro avg']['precision']
    hasil_avgscore2 = '%.2f'%hasil['macro avg']['recall']
    hasil_avgscore3 = '%.2f'%hasil['macro avg']['f1-score']
    #pd.to_pickle(model, r'E:\Sistem Tugas Akhir\apreksila\new_model.pickle')
    if request.method == 'POST':
        tek_darah = int(request.POST.get('tek_darah'))
        r_persalinan = int(request.POST.get('r_persalinan'))
        r_abortus = int(request.POST.get('r_abortus'))
        malnutrisi = int(request.POST.get('malnutrisi'))
        peny_lain = int(request.POST.get('peny_lain'))
        masalah_saathamil = int(request.POST.get('masalah_saathamil'))

        #model = pd.read_pickle(r'E:\Sistem Tugas Akhir\apreksila\new_model.pickle')

        with open(os.path.join(BASE_DIR, 'new_model.pickle'), "rb") as f:
            model = pickle.load(f)
        #Make Prediction
        result = model.predict([[tek_darah, r_persalinan, r_abortus, malnutrisi, peny_lain, masalah_saathamil]])

        usia_kelahiran = result[0]
        prediksi ={
            'precision1' : hasil_precision1,
            'precision2' : hasil_precision2,
            'precision3' : hasil_precision3,
            'recall1' : hasil_recall1,
            'recall2' : hasil_recall2,
            'recall3' : hasil_recall3,
            'accuracy'  : hasil_acuracy,
            'f1_score1' : hasil_f1score1,
            'f1_score2' : hasil_f1score2,
            'f1_score3' : hasil_f1score3,
            'hasil_precision' : hasil_avgscore1,
            'hasil_recall' : hasil_avgscore2,
            'hasil_f1score' : hasil_avgscore3,
            'pred': usia_kelahiran,
        }

        # prediksi_usiaKelahiran.objects.create(tek_darah=tek_darah, r_persalinan=r_persalinan, r_abortus=r_abortus, malnutrisi=malnutrisi, peny_lain=peny_lain, masalah_saathamil=masalah_saathamil, usia_kelahiran=usia_kelahiran)

        # return JsonResponse({'result': usia_kelahiran, 'tek_darah': tek_darah,'r_persalinan': r_persalinan, 'r_abortus': r_abortus, 'malnutrisi': malnutrisi, 'peny_lain': peny_lain, 'masalah_saathamil': masalah_saathamil},safe=False)

    return render(request, 'prediksi_usia/results.html', prediksi)