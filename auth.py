import os
import random
import json
from utils import temizle
import time
from islemlermenu import islemlermenusu
from config import KAYIT_KLASORU


class Kullanici:
    def __init__(self, isim, sifre, para=0):
        self.isim = isim
        self.sifre = sifre
        self.para = para
        self.hesapno = ''.join(str(random.randint(0,9)) for _ in range(16))

    def bilgi(self):
        return print(f"isim: {self.isim}\n"
                     f"sifre: {self.sifre}\n"
                     f"hesapno: {self.hesapno}\n"
                     f"Para: {self.para}")


def kayitol():
    temizle()
    isim = input("Isim giriniz: ")
    sifre = input("Sifre giriniz: ")

    k1 = Kullanici(isim, sifre)

    kayit = {
        "isim": isim,
        "sifre": sifre,
        "Hesapno": k1.hesapno,
        "Para": k1.para
    }

    dosya_adi = f"{KAYIT_KLASORU}/{k1.hesapno}.json"

    with open(dosya_adi, 'w', encoding='utf-8') as f:
        json.dump(kayit, f, indent=2, ensure_ascii=False)

    temizle()
    print("Basariyla kayit oldunuz.")
    time.sleep(2)

    islemlermenusu(k1.hesapno)


def girisyap():
    temizle()
    isim = input("Isim: ")
    sifre = input("Sifre: ")

    for dosya in os.listdir(KAYIT_KLASORU):

        if dosya.endswith(".json"):
            yol = os.path.join(KAYIT_KLASORU, dosya)

            with open(yol, "r", encoding="utf-8") as f:
                veri = json.load(f)

                if veri["isim"] == isim and veri["sifre"] == sifre:
                    islemlermenusu(veri["Hesapno"])
                    return

    print("Isim veya sifre hatali")
    time.sleep(2)