from matplotlib import pyplot as plt
from math import cos, sin, pi, log

def fungsi_kotak(batas_atas, batas_bawah):
    '''Fungsi kotak akan ditampilkan dalam sinyal diskret dengan frekuensi 5Hz (dalam 1 detik diwakili oleh 5 sinyal diskrit)'''
    sisi_kiri = [0 for i in range(30)]
    kotak_kiri = [1 for i in range(batas_atas*5)]
    nol = [1]
    kotak_kanan = kotak_kiri[:]
    sisi_kanan = sisi_kiri[:]
    fungsi = sisi_kiri+kotak_kiri+nol+kotak_kanan+sisi_kanan
    return fungsi

def dft(x_n):
    N = len(x_n)
    X_k = [x for x in range(N)]
    flag = 0
    for k, nilai_X_k in enumerate(X_k):
        for n, nilai_x_n in enumerate(x_n):
            flag1 = nilai_x_n*(cos(2*pi*k*n/N)-1j*sin(2*pi*k*n/N))
            flag += flag1
            flag1 = 0
        X_k[k] = flag
        flag = 0
    magnitude = [abs(i) for i in X_k]
    nyquist_limit = N//2
    magnitude = magnitude[:nyquist_limit]
    magnitude = [2*i for i in magnitude]
    normalisasi = [i/N for i in magnitude]
    cermin_normalisasi = normalisasi[:]
    cermin_normalisasi.reverse()
    sumbu_x = list(range(len(normalisasi)))
    cermin_sumbu_x = sumbu_x[:]
    cermin_sumbu_x.reverse()
    cermin_sumbu_x = [-1*i for i in cermin_sumbu_x]
    return cermin_normalisasi+normalisasi

signal = fungsi_kotak(3, 3)
dftPertama = dft(signal)
dftKuadrat = [i**2 for i in dftPertama]
dftLog = [log(i) for i in dftKuadrat]
dftKedua = dft(dftLog)
cepstrum = [i**2 for i in dftKedua]

plt.subplot(1, 2, 1)
plt.title('sinyal awal')
plt.stem(signal, 'b', markerfmt='o', basefmt='b')

plt.subplot(1, 2, 2)
plt.title('MFCC')
plt.stem(cepstrum, 'b', markerfmt='o', basefmt='b')
plt.show()
