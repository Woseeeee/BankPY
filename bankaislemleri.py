from config import KAYIT_KLASORU
import json
import os


def hesap_bilgisi(hesapno):

    dosya = f"{KAYIT_KLASORU}/{hesapno}.json"

    with open(dosya, "r", encoding="utf-8") as f:
        veri = json.load(f)

    return veri

def para_yatir(hesapno, miktar):

    dosya = f"{KAYIT_KLASORU}/{hesapno}.json"

    with open(dosya, "r", encoding="utf-8") as f:
        veri = json.load(f)

    veri["Para"] += miktar

    with open(dosya, "w", encoding="utf-8") as f:
        json.dump(veri, f, indent=2, ensure_ascii=False)

    return veri["Para"]

def para_cek(hesapno, miktar):

    dosya = f"{KAYIT_KLASORU}/{hesapno}.json"

    with open(dosya, "r", encoding="utf-8") as f:
        veri = json.load(f)

    if veri["Para"] < miktar:
        return False

    veri["Para"] -= miktar

    with open(dosya, "w", encoding="utf-8") as f:
        json.dump(veri, f, indent=2, ensure_ascii=False)

    return True

def para_gonder(gonderen_hesap, alici_hesap, miktar):

    gonderen_dosya = f"{KAYIT_KLASORU}/{gonderen_hesap}.json"
    alici_dosya = f"{KAYIT_KLASORU}/{alici_hesap}.json"

    if not os.path.exists(alici_dosya):
        return False

    with open(gonderen_dosya, "r", encoding="utf-8") as f:
        gonderen = json.load(f)

    if gonderen["Para"] < miktar:
        return False

    with open(alici_dosya, "r", encoding="utf-8") as f:
        alici = json.load(f)

    gonderen["Para"] -= miktar
    alici["Para"] += miktar

    with open(gonderen_dosya, "w", encoding="utf-8") as f:
        json.dump(gonderen, f, indent=2, ensure_ascii=False)

    with open(alici_dosya, "w", encoding="utf-8") as f:
        json.dump(alici, f, indent=2, ensure_ascii=False)

    return True