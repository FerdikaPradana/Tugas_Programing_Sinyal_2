import matplotlib.pyplot as plt
import matplotlib.cm as cm
from math import cos, sin, pi


def fungsi_kotak(batas_atas, batas_bawah):
    '''Fungsi kotak akan ditampilkan dalam sinyal diskret dengan frekuensi 10 Hz (dalam 1 detik diwakili oleh 10 sinyal diskrit)'''
    sisi_kiri = [0 for i in range(30)]
    kotak_kiri = [1 for i in range(int(batas_atas*5))]
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

def initialize_image(x_p, y_p):
    image = []
    for i in range(y_p):
        x_colors = []
        for j in range(x_p):
            x_colors.append(0)
        image.append(x_colors)
    return image

def color_points(sigx, sigy, x_p, y_p):
    image = initialize_image(len(x_p), len(y_p))
    for i in range(len(y_p)):
        for j in range(len(x_p)):
            image[i][j] = x_p[i]*y_p[j]
    plt.subplot(1, 2, 2)
    plt.imshow(image, origin='lower', extent=(0, len(x_p), 0, len(y_p)),
        cmap=cm.Greys_r, interpolation='nearest')
    plt.colorbar()
    image = initialize_image(len(x_p), len(y_p))
    for i in range(len(y_p)):
        for j in range(len(x_p)):
            image[i][j] = sig_x[i]*sig_y[j]
    plt.subplot(1, 2, 1)
    plt.imshow(image, origin='lower', extent=(0, len(x_p), 0, len(y_p)),
        cmap=cm.Greys_r, interpolation='nearest')
    plt.colorbar()
    plt.show()

sig_x = fungsi_kotak(0.5, 0.5) #sinyal pada sumbu x
sig_y = fungsi_kotak(0.5, 0.5) #sinyal pada sumbu y

DFT_x = dft(sig_x) #DFT pada sumbu x
DFT_y = dft(sig_y) #DFT pada sumbu y

color_points(sig_x, sig_y, DFT_x, DFT_y)