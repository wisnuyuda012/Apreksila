from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.svm import SVC
import pandas as pd
from pandas import read_csv
import pickle



# from sklearn import svm
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score, classification_report
# from sklearn.svm import SVC
# import pandas as pd
# from pandas import read_csv
# import pickle

df = pd.read_csv(r'E:\Sistem Tugas Akhir\apreksila\dataset.csv')

X = df[['tek_darah', 'r_persalinan', 'r_abortus', 'malnutrisi', 'peny_lain', 'masalah_saathamil']]
y = df['usia_kelahiran']

print(df)

X=X.values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=110, train_size=80, random_state=1)

print("Jumlah data test nya adalah", y_test.shape)
print("Jumlah data trainingnya adalah", y_train.shape)
model = svm.SVC(kernel='rbf')
model.fit(X, y)
print('test')

y_pred = model.predict(X_test)

print("Accuracy nya \n", accuracy_score(y_test, y_pred))

print(classification_report(y_test, y_pred))

pd.to_pickle(model, r'E:\Sistem Tugas Akhir\apreksila\new_model.pickle')

model = pd.read_pickle(r'E:\Sistem Tugas Akhir\apreksila\new_model.pickle')

tekanan_darah = float(input("Enter Tekanan Darah :"))
riwayat_persalinan = float(input("Enter Riwayat Persalinan :"))
riwayat_abortus = float(input("Enter Riwayat Abortus :"))
malnutrisi = float(input("Enter Kandungan Nutrisi anda: "))
penyakit_lain = float(input("Enter Penyakit lain yang diderita: "))
masalah_saat_hamil = float(input("Enter Masalah yang dialami saat hamil: "))

result = model.predict([[tekanan_darah, riwayat_persalinan, riwayat_abortus, malnutrisi, penyakit_lain, masalah_saat_hamil]])

print("Hasil prediksi Usia Kelahiran = ",result)