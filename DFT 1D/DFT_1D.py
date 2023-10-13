from matplotlib import pyplot as plt
from math import cos, sin, pi

def fungsi_kotak(batas_atas, batas_bawah):
    '''Fungsi kotak akan ditampilkan dalam sinyal diskret dengan frekuensi 5Hz (dalam 1 detik diwakili oleh 5 sinyal diskrit)'''
    sisi_kiri = [0 for i in range(30)]
    kotak_kiri = [1 for i in range(batas_atas*5)]
    nol = [1]
    kotak_kanan = kotak_kiri[:]
    sisi_kanan = sisi_kiri[:]
    fungsi = sisi_kiri+kotak_kiri+nol+kotak_kanan+sisi_kanan
    plt.subplot(2, 1, 1)
    plt.stem(list(range(-(30+5*batas_atas), (30+5*batas_atas)+1)), fungsi, 'b', markerfmt='o', basefmt='b')
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
    plt.subplot(2, 1, 2)
    plt.stem(sumbu_x, normalisasi, 'b', markerfmt='o', basefmt='b')
    plt.stem(cermin_sumbu_x, cermin_normalisasi, 'b', markerfmt='o', basefmt='b')
    plt.show()
    return normalisasi+cermin_normalisasi

a = fungsi_kotak(3, 3) #batas atas dan batas bawah dari fungsi kotak diubah disini
b = dft(a)

plt.show()