from utils import temizle
from auth import kayitol, girisyap

def selectmenu():
    while True:
        temizle()
        print ("KTA Bank Syste")
        print("1 - Hesap olustur")
        print("2 - Hesap gir")
        print("3 - cikis")

        secim = input()


        if secim in ["1","2","3"]:
            if secim == "1":
                kayitol()
            elif secim == "2":
                girisyap()
            elif secim == "3":
                temizle()
                print("Cikmak istediginize emin misiniz e/h")
                csecim = input()
                if csecim == "e" or csecim == "E":
                    temizle()
                    print("Kapaniyor iyi gunler dileriz.")
                    exit()
                elif csecim == "h" or csecim == "H":
                    return selectmenu()
        else:
            temizle()
            print("Hatali secim lutfen tekrar deneyin devam etmek icin Enter basin.")
            input()
            return selectmenu()
