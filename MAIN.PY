# 1
from datetime import datetime


class Hisob:
    def __init__(self, balans):
        self.balans = balans

    def foiz_hisoblash(self):
        raise NotImplementedError


    def pul_chiqarish(self, summa):
        raise NotImplementedError



class OmonatHisobi(Hisob):
    MINIMAL_QOLDIQ = 100_000

    def foiz_hisoblash(self):
        return self.balans * 0.05

    def pul_chiqarish(self, summa):
        if self.balans - summa < self.MINIMAL_QOLDIQ:
            print("❌ Pul chiqarib bo‘lmaydi! Minimal qoldiq talabi buzilmoqda.")
        else:
            self.balans -= summa
            print(f"✔ Pul chiqarildi. Yangi balans: {self.balans}")



class KreditHisobi(Hisob):
    FOIZ = 0.03  # 3% kredit foizi

    def foiz_hisoblash(self):
        return self.balans * self.FOIZ

    def pul_chiqarish(self, summa):
        jami = summa + (summa * self.FOIZ)
        self.balans += jami  # kredit qarzi oshadi
        print(f"✔ Kredit olindi. Qarzingiz: {self.balans} (foiz bilan)")



class InvestitsiyaHisobi(Hisob):
    def foiz_hisoblash(self):
        return self.balans * 0.12

    def pul_chiqarish(self, summa):
        bugun = datetime.today().weekday()

        if bugun >= 5:  # 5=shanba, 6=yakshanba
            print("❌ Bugun ish kuni emas! Pul chiqara olmaysiz.")
            return

        if summa > self.balans:
            print("❌ Balans yetarli emas.")
        else:
            self.balans -= summa
            print(f"✔ Pul chiqarildi. Yangi balans: {self.balans}")



print("--- Omonat Hisobi ---")
o = OmonatHisobi(200_000)
o.pul_chiqarish(50_000)
print("Foiz:", o.foiz_hisoblash())

print("\n--- Kredit Hisobi ---")
k = KreditHisobi(0)
k.pul_chiqarish(1_000_000)
print("Foiz:", k.foiz_hisoblash())

print("\n--- Investitsiya Hisobi ---")
i = InvestitsiyaHisobi(500_000)
i.pul_chiqarish(100_000)
print("Foiz:", i.foiz_hisoblash())


# 2
class Transport:
    def __init__(self, tezlik, yonish):
        self.tezlik = tezlik
        self.yonish = yonish

    def tezlik_oshirish(self, qiymat):
        self.tezlik += qiymat
        return self.tezlik

    def yoqilgi_sarfi(self, masofa):
        """Har bir transport uchun umumiy formula"""
        return masofa * self.yonish

    def safar_masofa(self, masofa):
        """Masofa berilganda yoqilgi va vaqt hisoblanadi"""
        vaqt = masofa / self.tezlik
        yoqilgi = self.yoqilgi_sarfi(masofa)
        return {
            "masofa": masofa,
            "vaqt_soat": vaqt,
            "yoqilgi_sarfi_litr": yoqilgi
        }


    def yuk_kotarish(self, yuk):
        return 0



class Avtobus(Transport):
    def yoqilgi_sarfi(self, masofa):
        return masofa * (self.yonish + 0.05)



class SportAvto(Transport):
    def yoqilgi_sarfi(self, masofa):
        return masofa * (self.yonish + 0.1)


class YukMashina(Transport):
    def yoqilgi_sarfi(self, masofa):
        return masofa * (self.yonish + 0.2)

    def yuk_kotarish(self, yuk):
        print(f"Yuk mashinasiga {yuk} kg yuk yuklandi.")
        return yuk



a = Avtobus(tezlik=60, yonish=0.15)
s = SportAvto(tezlik=120, yonish=0.12)
y = YukMashina(tezlik=70, yonish=0.2)

print("=== Avtobus safar ===")
print(a.safar_masofa(150))

print("\n=== SportAvto safar ===")
print(s.safar_masofa(150))

print("\n=== YukMashina safar ===")
print(y.safar_masofa(150))

print("\n=== YukMashina yuk ko‘tarish ===")
print(y.yuk_kotarish(5000))

print("\n=== Avtobus yuk ko‘tarishga urinish ===")
print(a.yuk_kotarish(1000))
