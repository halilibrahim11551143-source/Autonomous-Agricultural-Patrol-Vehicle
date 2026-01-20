# YOLOv8n-cls Model Eğitim Scripti
# Veri Seti: 10 Sınıf, 16.011 Görüntü

from ultralytics import YOLO

def egitimi_baslat():
    # Nano model seçimi (Gömülü sistemler için optimize)
    model = YOLO('yolov8n-cls.pt') 

    # Eğitim parametreleri [cite: 668-670]
    model.train(
        data='Dataset_Path/',
        epochs=50,
        imgsz=224,
        batch=16,
        project='Tarm_Devriye_Sonuclari',
        name='Domates_Hastalik_Modeli'
    )

if __name__ == "__main__":
    egitimi_baslat()
