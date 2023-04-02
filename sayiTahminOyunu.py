import random
rastgeleSayi = random.randint(1,10)
hak = 0
puan= 0
print("Sayı tahmin etme oyununa hoşgeldiniz ")
while hak<5:
    girilenSayi = int(input("lütfen 1 ile 10 arasında (ikiside dahil) bir sayı giriniz "))
    if hak == 5:
        print(" yanlış ,hakkınız kalmadı. puanınız :" +str(puan-5))
        break
    if girilenSayi == rastgeleSayi:
        puan=puan+25
        print("doğru, kalan hak " + str(4-hak) + " puanınız " +str(puan))
        break
    else:
        puan=puan-5
        if girilenSayi < rastgeleSayi:
            print("Yukarı ")
        else:
            print("Aşağı ")
            
    
    hak=hak+1
    
    