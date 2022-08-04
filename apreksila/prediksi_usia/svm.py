from pandas import read_csv
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.svm import SVC
import pandas as pd
import pickle

df = pd.read_excel(r'C:\Users\Dana\Desktop\Kuliah\semester 9\Skripsi\Data Penelitian\Dataset Fix.xlsx', sheet_name = 'FixData')


X = df[['Tekanan Darah', 'Riwayat Persalinan', 'Riwayat Abortus', 'Malnutrisi', 'Penyakit Lain', 'Masalah Saat Hamil ini']]
y = df['Usia Kelahiran']
print(X)
X = X.values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size =0.3, random_state = 1)

model = svm.SVC(kernel='rbf')
model.fit(X, y)

y_pred = model.predict(X_test)

print("Accuracy: ", accuracy_score(y_test, y_pred))

print(classification_report(y_test, y_pred))
pd.to_pickle(model,r'E:\Datasets\new_model.pickle')

model = pd.read_pickle(r'E:\Datasets\new_model.pickle')
Tekanan_Darah = float(input("Enter Teka1nan_Darah anda berdasarkan Kategori: "))
Riwayat_Persalinan = float(input("Enter Riwayat_Persalinan: "))
Riwayat_Abortus = float(input("Enter Riwayat_Abortus: "))
Malnutrisi = float(input("Enter Malnutrisi: "))
Penyakit_Lain= float(input("Enter Penyakit_Lain: "))
Masalah_Saat_Hamil_ini = float(input("Enter Masalah_Saat_Hamil ini: "))

result = model.predict([[Tekanan_Darah,Riwayat_Persalinan,Riwayat_Abortus,Malnutrisi,Penyakit_Lain, Masalah_Saat_Hamil_ini]])  # input must be 2D array
print(result)
