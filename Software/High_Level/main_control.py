import cv2
from ultralytics import YOLO
import serial
import time

# 1. SERİ HABERLEŞME KURULUMU
try:
    arduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    time.sleep(2)
    print("Arduino Bağlantısı Başarılı.")
except:
    arduino = None
    print("UYARI: Arduino Bulunamadı!")

# 2. YAPAY ZEKA MODELİNİN YÜKLENMESİ
model = YOLO('best.pt')

# 3. KAMERA BAŞLATMA
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

GUVEN_LIMITI = 0.60

while True:
    success, img = cap.read()
    if not success:
        break

    # 5. MODEL ÇIKARIMI (INFERENCE)
    results = model(img, stream=True, verbose=False)

    for r in results:
        probs = r.probs
        if probs is not None:
            top1_index = probs.top1
            conf = probs.top1conf.item()
            class_name = r.names[top1_index]
            label = f"{class_name} ({conf*100:.1f}%)"

            if conf > GUVEN_LIMITI:
                if "healthy" in class_name.lower():
                    color = (0, 255, 0)
                    if arduino:
                        arduino.write(b'I')
                else:
                    color = (0, 0, 255)
                    if arduino:
                        arduino.write(b'H')

                cv2.putText(img, label, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    cv2.imshow('Otonom Tarim Robotu Kamera', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
