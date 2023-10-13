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