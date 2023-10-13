# TUGAS PROGRAMING SINYAL 2

Nama:Ferdika Pradana Putra Hidayat

NRP: 5009211026

## Konvolusi
Kode Python:

```
def konvolusi(sig1, sig2):
    x_n = sig1[:]
    h_n = sig2[:]
    h_n.reverse()
    panjang_y_n = len(x_n) + len(h_n) -1
    y_n = []
    for i in range(panjang_y_n-len(h_n)):
        h_n.append(0)
    for i in range(panjang_y_n-len(x_n)):
        x_n.insert(0, 0)
    for i in range(panjang_y_n):
        flag = 0
        for j in range(panjang_y_n):
            flag += x_n[j]*h_n[j]
        y_n.append(flag)
        flag = 0
        h_n.insert(0, 0)
    return y_n

print('Nama: Ferdika Pradana Putra Hidayat')
print('NRP: 5009211026')

sig1 = [2, 1, 2, 1, 1, 0]
sig2 = [1, 0, 1, 2, 2, 1]
print(konvolusi(sig1, sig2))
```
Hasil running:
<img align="center" src="https://github.com/FerdikaPradana/Tugas_Programing_Sinyal_2/blob/main/konvolusi/Screenshot%20(552).png" width="600px" alt="lalit's Github Stats">

## Transformasi Fourier Diskret Satu Dimensi
Kode python

```
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
```
Berikut adalah pasangan sinyal kotak (gambar atas) dan transformasi fourier diskritnya (gambar bawah):

1) Sinyal kotak dengan f(t) = 1 untuk -A<t<A dan 0 untuk t yang lain
<img align="center" src="https://github.com/FerdikaPradana/Tugas_Programing_Sinyal_2/blob/main/DFT%201D/A.png" width="600px" alt="lalit's Github Stats">

2) Sinyal kotak dengan f(t) = 1 untuk -A/2<t<A/2 dan 0 untuk t yang lain
<img align="center" src="https://github.com/FerdikaPradana/Tugas_Programing_Sinyal_2/blob/main/DFT%201D/setengah A.png" width="600px" alt="lalit's Github Stats">

3) Sinyal kotak dengan f(t) = 1 untuk -3A<t<3A dan 0 untuk t yang lain
<img align="center" src="https://github.com/FerdikaPradana/Tugas_Programing_Sinyal_2/blob/main/DFT%201D/tiga A.png" width="600px" alt="lalit's Github Stats">

## Transformasi Fourier Dua Dimensi
Kode python
```
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
```
Berikut adalah gambar pasangan sinyal kotak (gambar kiri) dan hasil transformasi fourier diskret-nya (gambar kanan): 
1) Sinyal kotak dengan f(t) = 1 untuk -A<t<A dan 0 untuk t yang lain dan g(t) = 1 untuk -A<t<A dan 0 untuk t yang lain 
   <img align="center" src="https://github.com/FerdikaPradana/Tugas_Programing_Sinyal_2/blob/main/DFT%202D/A%20(2).png" width="600px" alt="lalit's Github Stats">
2) Sinyal kotak dengan f(t) = 1 untuk -A/2<t<A/2 dan 0 untuk t yang lain dan g(t) = 1 untuk -A/2<t<A/2 dan 0 untuk t yang lain 
   <img align="center" src="https://github.com/FerdikaPradana/Tugas_Programing_Sinyal_2/blob/main/DFT%202D/aetengah%20A%20(2).png" width="600px" alt="lalit's Github Stats">
3) Sinyal kotak dengan f(t) = 1 untuk -3A<t<3A dan 0 untuk t yang lain dan g(t) = 1 untuk -3A<t<3A dan 0 untuk t yang lain 
   <img align="center" src="https://github.com/FerdikaPradana/Tugas_Programing_Sinyal_2/blob/main/DFT%202D/tiga%20A%20(2).png" width="600px" alt="lalit's Github Stats">

## MFCC

Kode Python
```
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
```
Berikut adalah pasangan gambar sinyal dan hasil MFCC-nya
1) Sinyal kotak dengan f(t) = 1 untuk -A<t<A dan 0 untuk t yang lain
 <img align="center" src="https://github.com/FerdikaPradana/Tugas_Programing_Sinyal_2/blob/main/MFCC%20A.png" width="600px" alt="lalit's Github Stats">
 
2) Sinyal kotak dengan f(t) = 1 untuk -A/2<t<A/2 dan 0 untuk t yang lain

<img align="center" src="https://github.com/FerdikaPradana/Tugas_Programing_Sinyal_2/blob/main/MFCC%20setengah%20A.png" width="600px" alt="lalit's Github Stats">  

3) Sinyal kotak dengan f(t) = 1 untuk -3A<t<3A dan 0 untuk t yang lain

<img align="center" src="https://github.com/FerdikaPradana/Tugas_Programing_Sinyal_2/blob/main/MFCC%20tiga%20A.png" width="600px" alt="lalit's Github Stats">  
