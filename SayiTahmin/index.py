import time
import random

sayi = random.randint(1,100)
tahmin_hakki = 5

while True:
    tahmin = int(input('Tahmininizi Giriniz : '))

    if sayi == tahmin:
        print('Tebrikler Sayıyı Doğru Bildiniz!')
    elif sayi == tahmin and tahmin_hakki == 5:
        print('Tebrikler Tekte Bildiniz!')
    elif sayi < tahmin:
        print('Sorgulanıyor!!!')
        time.sleep(2)
        tahmin_hakki -= 1
        print('Yanlış Tahmin !!! ', tahmin_hakki)
    elif sayi > tahmin:
        print('Sorgulanıyor!!!')
        time.sleep(2)
        tahmin_hakki -= 1
        print('Yanlış Tahmin !!! ', tahmin_hakki)
    if tahmin_hakki == 0:
        print('Daha fazla hak satın almak ister misiniz? E')
        hakAl = str(input())
        if hakAl == 'E':
            print('Başarıyla Hak Aldınız!')
            tahmin_hakki += 5
        else:
            print('')
    else:
        print(tahmin_hakki)