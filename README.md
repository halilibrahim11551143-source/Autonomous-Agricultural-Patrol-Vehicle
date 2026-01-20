# Görüntü İşleme Destekli Otonom Tarım Devriye Aracı
## Autonomous Agricultural Patrol Vehicle with Deep Learning

[cite_start]Bu proje, Manisa Celal Bayar Üniversitesi bünyesinde "Lisans Bitirme Tasarımı" olarak geliştirilmiştir[cite: 48, 63]. [cite_start]Tarım arazilerinde otonom navigasyon yaparak bitki hastalıklarını gerçek zamanlı tespit eden ve noktasal (hedefli) ilaçlama gerçekleştiren entegre bir mekatronik sistemdir [cite: 126-127, 255].



### 🛠 Mühendislik Yaklaşımı ve Bileşenler
[cite_start]Sistem; algılama, karar verme ve eylem olmak üzere üç temel katmandan oluşmaktadır[cite: 128, 176]:

* [cite_start]**Yüksek Seviye Kontrol (Vision):** Raspberry Pi 5 üzerinde koşan YOLOv8n-cls modeli[cite: 303, 335].
* [cite_start]**Düşük Seviye Kontrol (Actuation):** Arduino Nano ile diferansiyel sürüş ve pompa yönetimi[cite: 303, 338, 399].
* [cite_start]**Donanım Kararı:** NVIDIA Jetson Nano yerine Raspberry Pi 5 seçilerek, sahada daha yüksek güç verimliliği ve fiyat/performans dengesi hedeflenmiştir [cite: 395-397].

### 📊 Performans Analizi (Sayısal Bulgular)
[cite_start]Elde edilen sonuçlar sistemin gerçek zamanlı tarımsal operasyonlara uygunluğunu kanıtlamaktadır[cite: 409, 446]:

| Parametre | Teknik Değer | Kaynak (Tez) |
| :--- | :--- | :--- |
| **Model Doğruluk Oranı (Top-1)** | [cite_start]%97.2 | [cite: 413, 418] |
| **Görüntü İşleme Hızı (Inference)** | [cite_start]30 ms / kare | [cite: 424, 448] |
| **Sistem Tepki Süresi** | [cite_start]45 ms | [cite: 450, 448] |
| **Eğitim Veri Seti** | [cite_start]16.011 Görüntü (10 Sınıf) | [cite: 373, 379] |
| **Otonom Hareket Hızı** | [cite_start]0.5 m/s | [cite: 451, 448] |

### 📂 Depo Hiyerarşisi
* [cite_start]**/Software/High_Level:** Ana otonom kontrol ve AI çıkarım kodları [cite: 514-515].
* **/Software/Embedded:** Eyleyici motor ve servo kontrol algoritmaları [cite: 585-588, 681].
* [cite_start]**/Software/Tools:** Veri ön işleme (`data_split.py`) ve sistem tanılama (`diagnostics.py`) araçları[cite: 848, 910].
* **/Hardware/CAD:** SolidWorks üzerinde tasarlanan parametrik şasi modelleri[cite: 315, 326].
* [cite_start]**/Documentation:** Akademik bitirme tezi tam metni (PDF) [cite: 47-51].

### 🔍 Neden Özgün?
[cite_start]Sistem, sadece bir yazılım projesi değil; mekanik tasarımı, devre mimarisi ve gömülü yazılımı ile bütünleşik bir mekatronik tasarımıdır[cite: 128, 250, 456]. [cite_start]Hatalı ilaçlama oranının %2.1'de tutulması, sürdürülebilir akıllı tarım uygulamalarına doğrudan katkı sağlamaktadır[cite: 448, 465].

---
**Geliştirici:** Halil İbrahim KURNAZ
