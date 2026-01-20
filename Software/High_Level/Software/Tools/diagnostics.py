# Otonom Tarım Robotu - Sistem Tanılama ve Hata Ayıklama Protokolü
# Hazırlayan: Halil İbrahim KURNAZ

import cv2
import os
from ultralytics import YOLO

def sistem_tanilama():
    print("--- SISTEM TESHIS PROTOKOLU BASLATILDI ---\n")
    
    # 1. Model Kontrolü
    if os.path.exists('best.pt'):
        print("[OK] AI Model ağırlık dosyası bulundu.")
    else:
        print("[HATA] 'best.pt' dosyası eksik!")

    # 2. Kamera Kontrolü
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        ret, frame = cap.read()
        if ret:
            print("[OK] Kamera sensörü veri akışı sağlıyor.")
        cap.release()
    else:
        print("[HATA] Kamera aygıtı başlatılamadı.")

    # 3. AI Yükleme Kontrolü
    try:
        model = YOLO('best.pt')
        print("[OK] YOLOv8 modeli RAM belleğe başarıyla yüklendi.")
    except Exception as e:
        print(f"[HATA] Model yükleme hatası: {e}")

if __name__ == "__main__":
    sistem_tanilama()
