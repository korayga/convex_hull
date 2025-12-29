# Algoritma Analizi ve Tasarımı Ödevi
## Kapalı Çevrim (Convex Hull) Uygulaması - Detaylı Kullanım Kılavuzu

---

## 📋 Proje Hakkında

Bu proje, hesaplamalı geometrinin temel problemlerinden biri olan **Kapalı Çevrim (Convex Hull)** probleminin çözümü için geliştirilmiş kapsamlı bir Python uygulamasıdır.

### 🎯 Projenin Amacı
- İki farklı algoritmanın (Kaba Kuvvet ve Graham Scan) teorik karmaşıklık analizlerini pratik sonuçlarla doğrulamak
- Algoritmaların çalışma mantığını görsel olarak sunmak
- Kullanıcı dostu bir arayüz ile etkileşimli deneyim sunmak
- Performans testleri ile algoritmaların gerçek dünya davranışlarını gözlemlemek

### 🔬 Convex Hull Problemi Nedir?
Düzlem üzerinde verilen N adet nokta için, tüm noktaları içine alan en küçük **dışbükey çokgen**i (convex polygon) bulmaktır. Bu çokgenin köşeleri verilen noktalardan seçilir.

---

## 🚀 Kurulum ve Çalıştırma

### Gereksinimler
- **Python 3.8 veya üzeri**
- **İşletim Sistemi:** Windows, macOS, Linux

### 1. Gerekli Kütüphanelerin Kurulumu

```bash
pip install matplotlib
```

### 2. GUI Uygulamasını Başlatma

```bash
python convex_hull_app.py
```

### 3. Performans Testlerini Çalıştırma

```bash
python performance_test.py
```

---

## 📊 Algoritma Detayları

### 1. Kaba Kuvvet (Brute Force) Algoritması

#### Çalışma Mantığı
```
1. Her nokta çiftini (P, Q) seç → O(N²)
2. Bu çift bir doğru parçası oluşturur
3. Diğer TÜM noktaların bu doğrunun aynı tarafında olup olmadığını kontrol et → O(N)
4. Eğer tüm noktalar aynı taraftaysa, (P, Q) Convex Hull'ın bir kenarıdır
5. Bulunan kenarları birleştir ve açısal olarak sırala (Bubble Sort)
```

#### Karmaşıklık Analizi
| Adım | İşlem | Karmaşıklık |
|------|-------|-------------|
| Dış Döngü (i) | Tüm noktalar | O(N) |
| Orta Döngü (j) | Diğer noktalar | O(N) |
| İç Döngü (k) | Doğrulama | O(N) |
| **TOPLAM** | **N × N × N** | **O(N³)** |

#### Avantajları
- ✅ Basit ve anlaşılır mantık
- ✅ Uygulaması kolay
- ✅ Küçük veri setlerinde (N < 100) hızlı sonuç

#### Dezavantajları
- ❌ Büyük veri setlerinde çok yavaş (N > 500 kullanışsız)
- ❌ Gereksiz tekrarlı kontroller
- ❌ Bellek verimsiz

---

### 2. Graham Scan Algoritması

#### Çalışma Mantığı
```
1. Başlangıç Noktası (Pivot) Seç → O(N)
   - En alt (Y en küçük) ve en sol (X en küçük) nokta
   
2. Noktaları Kutupsal Açılarına Göre Sırala
   - Pivot noktasına göre polar açı hesapla (math.atan2)
   - Eğitim amaçlı Bubble Sort kullanılmıştır → O(N²)
   
3. Stack (Yığın) ile Tarama → O(N)
   - Her nokta için:
     * Sağa dönüş varsa: Yığından çıkar
     * Sola dönüş varsa: Yığına ekle
```

#### Karmaşıklık Analizi
| Adım | İşlem | Karmaşıklık |
|------|-------|-------------|
| Pivot Bulma | Linear tarama | O(N) |
| Sıralama | Bubble Sort (Eğitim Amaçlı) | O(N²) |
| Yığın Tarama | Her nokta 1 kez | O(N) |
| **TOPLAM** | **Sıralama Baskın** | **O(N²)** |
*(Not: Standart Graham Scan O(N log N) karmaşıklığındadır, ancak bu projede algoritma mantığını göstermek için Bubble Sort kullanılmıştır.)*


#### Avantajları
- ✅ Kaba Kuvvet yöntemine göre çok daha hızlı
- ✅ Bellek verimli
- ✅ Büyük veri setlerinde ideal

#### Dezavantajları
- ❌ Uygulama biraz daha karmaşık
- ❌ Sıralama gerektirir

---

## 🛠️ Kullanılan Teknolojiler

| Teknoloji | Kullanım Amacı |
|-----------|---------------|
| **Python 3.x** | Ana programlama dili |
| **tkinter** | GUI oluşturma ve kullanıcı etkileşimi |
| **matplotlib** | Grafik çizimi, veri görselleştirme ve Tkinter entegrasyonu |
| **math** | Geometrik hesaplamalar (atan2, sqrt) |
| **random** | Test verisi üretimi |

## 📂 Proje Yapısı

```
algo/
├── algoritmalar.py       # Algoritma sınıfları ve fonksiyonları (Logic)
├── convex_hull_app.py    # Ana GUI uygulaması (Görselleştirme)
├── performance_test.py   # Performans karşılaştırma modülü (Analiz)
└── README.md             # Proje dokümantasyonu
```





