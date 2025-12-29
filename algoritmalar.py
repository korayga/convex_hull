import math

class KonveksZarfCozucu:
    # konveks zarf algoritmalari burada

    @staticmethod
    def yonelim_hesapla(p, q, r):
        # uc noktanin yonelimini bulur
        # 0: dogrusal, 1: saat yonu, 2: saat yonu tersi
        
        deger = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        
        if abs(deger) < 1e-10:
            return 0
        return 1 if deger > 0 else 2

    @staticmethod
    def mesafe_hesapla(p1, p2):
        # iki nokta arasi mesafe
        return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

    @staticmethod
    def polar_aci_hesapla(p0, p1):
        # p0'a gore p1'in acisi
        return math.atan2(p1[1] - p0[1], p1[0] - p0[0])

    @staticmethod
    def kaba_kuvvet_konveks_zarf(noktalar):
        # kaba kuvvet yontemi O(N^3)
        n = len(noktalar)
        if n < 3:
            return noktalar

        zarf_kenarlari = []

        # her nokta ciftine bak
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                
                p, q = noktalar[i], noktalar[j]
                gecerli_kenar = True
                
                # diger noktalarin hepsi ayni tarafta
                for k in range(n):
                    if k == i or k == j:
                        continue
                    
                    r = noktalar[k]
                    # Eger nokta saga (saat yonu) dusuyorsa, bu kenari atla
                    # Sadece tek bir yondeki (saat yonu tersi) kenarlari kabul ediyoruz
                    if KonveksZarfCozucu.yonelim_hesapla(p, q, r) == 1:
                        gecerli_kenar = False
                        break
                
                if gecerli_kenar:
                    zarf_kenarlari.append((p, q))

        if not zarf_kenarlari:
            return []

        # benzersiz noktalari al
        zarf_noktalari = list({p for kenar in zarf_kenarlari for p in kenar})
        
        # saat yonu tersine sirala
        if len(zarf_noktalari) > 2:
            merkez_x = sum(p[0] for p in zarf_noktalari) / len(zarf_noktalari)
            merkez_y = sum(p[1] for p in zarf_noktalari) / len(zarf_noktalari)
            merkez = (merkez_x, merkez_y)
            
            # Bubble Sort ile Aciya Gore Siralama
            m = len(zarf_noktalari)
            for i in range(m):
                for j in range(0, m-i-1):
                    p1 = zarf_noktalari[j]
                    p2 = zarf_noktalari[j+1]
                    
                    aci1 = math.atan2(p1[1] - merkez[1], p1[0] - merkez[0])
                    aci2 = math.atan2(p2[1] - merkez[1], p2[0] - merkez[0])
                    
                    if aci1 > aci2:
                        zarf_noktalari[j], zarf_noktalari[j+1] = zarf_noktalari[j+1], zarf_noktalari[j]
            
        return zarf_noktalari

    @staticmethod
    def graham_tarama_konveks_zarf(noktalar):
        # graham scan algoritmasi O(N log N)
        n = len(noktalar)
        if n < 3:
            return noktalar

        # 1. baslangic noktasi (en alt sol)
        pivot = min(noktalar, key=lambda p: (p[1], p[0]))

        # 2. diger noktalari sirala (O(n log n) ile)
        diger_noktalar = [p for p in noktalar if p != pivot]
        
        # Python'un sorted() fonksiyonu ile O(n log n) siralama
        # 1. Kriter: Pivot noktasina gore aci (kucukten buyuge)
        # 2. Kriter: Aci esitse, pivota olan mesafe (kucukten buyuge)
        
        def siralama_anahtari(nokta):
            aci = KonveksZarfCozucu.polar_aci_hesapla(pivot, nokta)
            mesafe = KonveksZarfCozucu.mesafe_hesapla(pivot, nokta)
            return (aci, mesafe)
        
        sirali_noktalar = sorted(diger_noktalar, key=siralama_anahtari)

        # 3. stack islemleri
        yigin = [pivot, sirali_noktalar[0]]

        for i in range(1, len(sirali_noktalar)):
            simdiki_nokta = sirali_noktalar[i]
            
            # saga donus varsa cikar
            while len(yigin) > 1:
                yonelim = KonveksZarfCozucu.yonelim_hesapla(yigin[-2], yigin[-1], simdiki_nokta)
                if yonelim != 2: 
                    yigin.pop()
                else:
                    break
            
            yigin.append(simdiki_nokta)

        return yigin

