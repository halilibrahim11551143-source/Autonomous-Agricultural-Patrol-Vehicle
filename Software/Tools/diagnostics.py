import cv2
import serial
import os
from ultralytics import YOLO
import time

def hata_ayiklama_modulu():
    print("--- OTONOM ROBOT HATA AYIKLAMA VE TESHIS PROTOKOLU ---\n") [cite: 917]
    
    # 1. Dosya Sistemi Kontrolü [cite: 913-914]
    if os.path.exists('best.pt'):
        print("[OK] Model dosyası (best.pt) diskte mevcut.") [cite: 925]
    else:
        print("[HATA] KRITIK: 'best.pt' dosyası bulunamadı!") [cite: 927]

    # 2. Kamera Donanım Kontrolü [cite: 914]
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        ret, frame = cap.read()
        if ret:
            print("[OK] Kamera sensörü aktif ve veri akışı var.") [cite: 937]
        cap.release()
    else:
        print("[HATA] Kamera aygıtı başlatılamadı.") [cite: 945]

    # 3. Yapay Zeka Model Yükleme Testi [cite: 914]
    try:
        model = YOLO('best.pt')
        print("[OK] YOLOv8 modeli RAM belleğe hatasız yüklendi.") [cite: 954]
    except Exception as e:
        print(f"[HATA] Model yükleme hatası: {e}") [cite: 957]

    # 4. Arduino Seri Port Bağlantısı [cite: 914]
    try:
        ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1) [cite: 958]
        time.sleep(1)
        ser.close()
        print("[OK] Arduino seri port bağlantısı sağlandı.") [cite: 960]
    except:
        print("[UYARI] Arduino bağlantısı başarısız.") [cite: 962]

if __name__ == '__main__':
    hata_ayiklama_modulu()
