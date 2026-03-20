from bankaislemleri import hesap_bilgisi, para_yatir, para_cek, para_gonder
from utils import temizle


def islemlermenusu(hesapno):
    while True:
        temizle()
        print("KTA Bank System")
        print("1 - Para yatir")
        print("2 - Para cek")
        print("3 - Para gonder")
        print("4 - Hesap bilgileri")
        print("5 - Cikis")

        secimi = input("Secim: ")

        if secimi == "1":
            miktar = int(input("Yatirilacak miktar: "))
            para_yatir(hesapno, miktar)
            input("Devam etmek icin Enter...")

        elif secimi == "2":
            miktar = int(input("Cekilecek miktar: "))
            para_cek(hesapno, miktar)
            input("Devam etmek icin Enter...")

        elif secimi == "3":
            alici = input("Alici hesap no: ")
            miktar = int(input("Gonderilecek miktar: "))
            para_gonder(hesapno, alici, miktar)
            input("Devam etmek icin Enter...")

        elif secimi == "4":
            veri = hesap_bilgisi(hesapno)
            print(veri)
            input("Devam etmek icin Enter...")

        elif secimi == "5":
            temizle()
            print("Cikmak istediginize emin misiniz e/h")
            isecim = input()

            if isecim.lower() == "e":
                temizle()
                print("Kapaniyor iyi gunler dileriz.")
                exit()

        else:
            print("Hatali secim")
            input("Enter...")