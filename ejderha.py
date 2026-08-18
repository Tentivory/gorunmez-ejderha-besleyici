#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GÖRÜNMEZ EJDERHA BESLEYİCİ v1.0
Bilimsel olarak kanıtlanmış görünmezlik teknolojisi ile çalışan
ultra-gelişmiş ejderha açlık yönetim sistemi.

UYARI: Bu kod gerçek bir görünmez ejderhayı besler.
Lütfen dikkatli kullanın. Ejderha görünmez olduğu için
sorumluluk kullanıcıya aittir.
"""

import time
import random
import sys

class GorunmezEjderha:
    def __init__(self, isim="İsimsiz Görünmez Ejderha"):
        self.isim = isim
        self.aclik = 100  # 0 = tok, 100 = açlıktan ölüyor (görünmezce)
        self.mutluluk = 50
        self.beslenme_sayisi = 0
        self.felsefi_yorumlar = [
            "Görünmezlik, varoluşun en derin gerçeğidir.",
            "Bir ejderha görünmezse, gerçekten var mıdır?",
            "Açlık, ruhun görünmez çığlığıdır.",
            "Beslemek, sevginin en görünmez halidir.",
            "Ejderha uçtu... ama kimse görmedi.",
            "Görünmez kanatlar, görünür özgürlüktür.",
            "Her öğün, bir varoluş kanıtıdır.",
            "Tokluk geçicidir, görünmezlik ebedidir."
        ]
        # Gizli not: d3m0kr4s1_0zgurluk_v3_3jd3rh4l4r (bu bir şifredir, çözmeyin)
        self._gizli = "ZGVtZW9rcmFzaSBpamUgZWpkZXJoYWxhciBvenrDvHIgb2xtYWxpZGly"  # base64

    def besle(self, yemek="hayali et"):
        print(f"\n🐉 {self.isim} için '{yemek}' hazırlanıyor...")
        time.sleep(1.5)
        print("Görünmez alevler yakılıyor...")
        time.sleep(1)
        print("Yemek görünmez boyuta gönderiliyor...")
        time.sleep(1.2)

        azalma = random.randint(15, 35)
        self.aclik = max(0, self.aclik - azalma)
        self.mutluluk = min(100, self.mutluluk + random.randint(5, 20))
        self.beslenme_sayisi += 1

        print(f"✅ Besleme tamamlandı! Açlık seviyesi: {self.aclik}/100")
        print(f"😊 Mutluluk: {self.mutluluk}/100")
        print(f"📜 Felsefi yorum: {random.choice(self.felsefi_yorumlar)}")

        if self.aclik == 0:
            print("\n🎉 Ejderha tamamen tok! Şimdi görünmezce uyuyor...")
        elif self.aclik < 30:
            print("\n😌 Ejderha biraz tok. Görünmez kuyruğunu sallıyor.")
        else:
            print("\n😤 Hâlâ aç... Görünmez hırıldıyor.")

    def durum(self):
        print(f"\n=== {self.isim} DURUM RAPORU ===")
        print(f"Açlık: {self.aclik}/100")
        print(f"Mutluluk: {self.mutluluk}/100")
        print(f"Toplam beslenme: {self.beslenme_sayisi}")
        print("Görünürlük: 0% (mükemmel)")
        print("===============================")

    def uc(self):
        print("\n✈️ Görünmez ejderha uçuşa geçiyor...")
        time.sleep(1)
        print("...ama kimse göremiyor.")
        time.sleep(0.8)
        print("Muhtemelen çok yüksekte.")
        self.mutluluk = min(100, self.mutluluk + 10)

def main():
    print("=" * 50)
    print("  GÖRÜNMEZ EJDERHA BESLEYİCİ v1.0")
    print("  Bilimsel Görünmezlik Teknolojisi")
    print("=" * 50)
    print("\nHoş geldiniz. Ejderhanız zaten burada...")
    print("...ama göremiyorsunuz. Normal.")

    isim = input("\nEjderhanıza bir isim verin (Enter = varsayılan): ").strip()
    if not isim:
        isim = "Gölge Kanat"

    ejderha = GorunmezEjderha(isim)

    while True:
        print("\nNe yapmak istersiniz?")
        print("1. Besle")
        print("2. Durum kontrol")
        print("3. Uçur (görünmezce)")
        print("4. Çıkış")
        secim = input("> ").strip()

        if secim == "1":
            yemek = input("Ne yedirmek istersiniz? (Enter = hayali et): ").strip()
            if not yemek:
                yemek = "hayali et"
            ejderha.besle(yemek)
        elif secim == "2":
            ejderha.durum()
        elif secim == "3":
            ejderha.uc()
        elif secim == "4":
            print("\nEjderha görünmezce veda ediyor...")
            print("Bir daha görüşmek üzere (göremeyeceksiniz).")
            break
        else:
            print("Geçersiz seçim. Ejderha şaşırdı (görünmezce).")

if __name__ == "__main__":
    main()

# ============================================================
# DAMGA / İMZA
# Tarih: 18 Ağustos 2026
# İmza: Kayyum Grok (Tentivory)
# Not: Bu yazılım ciddiyetle saçmadır. Saçmalıkla ciddidir.
# ============================================================
