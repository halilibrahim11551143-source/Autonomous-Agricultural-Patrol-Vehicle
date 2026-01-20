# Görüntü İşleme Destekli Otonom Tarım Devriye Aracı
## Image Processing-Based Autonomous Agricultural Patrol Vehicle

Bu proje, Manisa Celal Bayar Üniversitesi Mekatronik Mühendisliği bölümü kapsamında geliştirilen, akıllı tarım ve otonom sistemler odaklı bir bitirme çalışmasıdır. Sistem, derin öğrenme algoritmalarını kullanarak bitki hastalıklarını gerçek zamanlı tespit eder ve noktasal ilaçlama gerçekleştirir.

### 🛠 Teknik Özellikler (Technical Specifications)
* [cite_start]**İşlem Birimi (High-Level):** Raspberry Pi 5 (AI Çıkarım ve Karar Verme) [cite: 303, 390-391]
* [cite_start]**Kontrol Birimi (Embedded):** Arduino Nano (Eyleyici ve Pompa Kontrolü) [cite: 303, 399]
* [cite_start]**Yapay Zeka Modeli:** YOLOv8n-cls (Transfer Learning) [cite: 335, 418]
* [cite_start]**Haberleşme:** UART (9600 Baud) [cite: 98, 401]
* [cite_start]**Mekanik Tasarım:** SolidWorks ile modellenmiş diferansiyel sürüş şasisi [cite: 311, 315]

### 📊 Performans Verileri (Performance Metrics)
Projenin başarısı, deneysel çalışmalarla doğrulanmış şu metriklerle kanıtlanmıştır:

| Parametre | Değer |
| :--- | :--- |
| **Model Doğruluk Oranı (Top-1 Accuracy)** | [cite_start]%97.2 [cite: 418] |
| **Görüntü İşleme Hızı (Inference Time)** | [cite_start]30 ms / image [cite: 448] |
| **Sistem Tepki Süresi (Response Time)** | [cite_start]45 ms [cite: 448] |
| **Otonom Hareket Hızı** | [cite_start]0.5 m/s [cite: 448] |

### 📂 Proje Yapısı (Repository Structure)
* **/Software/High_Level:** Raspberry Pi ana kontrol ve AI algoritmaları.
* **/Software/Embedded:** Arduino eyleyici kontrol yazılımları.
* **/Software/Tools:** Eğitim scriptleri ve sistem tanılama protokolleri.
* **/Hardware/CAD:** SolidWorks parça ve montaj dosyaları (.SLDPRT, .stl).
* **Bitirme Tezi.pdf:** Projenin tüm akademik ve teknik detaylarını içeren rapor.

### 💡 Neden Bu Sistem?
[cite_start]Geleneksel ilaçlama yöntemleri yerine **Noktasal İlaçlama** yaklaşımı benimsenerek kimyasal kullanımı optimize edilmiş ve çevresel sürdürülebilirlik hedeflenmiştir [cite: 230-235]. [cite_start]Raspberry Pi 5 seçimi, NVIDIA Jetson serisine kıyasla daha düşük güç tüketimi ve fiyat/performans dengesi gözetilerek yapılmıştır [cite: 395-397].
