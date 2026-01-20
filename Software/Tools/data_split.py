
import os
import shutil
import random

def veri_setini_hazirla():
    kaynak_klasor = 'Ham_Veriler' # Ham görüntülerin olduğu ana dizin
    hedef_klasor = 'VeriSeti'      # YOLOv8 formatına uygun çıktı dizini
    
    siniflar = os.listdir(kaynak_klasor)
    egitim_orani = 0.70
    val_orani = 0.20   

    for sinif in siniflar:
        sinif_yolu = os.path.join(kaynak_klasor, sinif)
        if not os.path.isdir(sinif_yolu):
            continue
            
        resimler = os.listdir(sinif_yolu)
        random.shuffle(resimler)
        
        toplam_resim = len(resimler)
        egitim_bitis = int(toplam_resim * egitim_orani)
        val_bitis = int(toplam_resim * (egitim_orani + val_orani))

        klasor_yapisi = {
            'train': resimler[:egitim_bitis],
            'val': resimler[egitim_bitis:val_bitis],
            'test': resimler[val_bitis:]
        }

        for kume_adi, kume_resimleri in klasor_yapisi.items():
            hedef_yol = os.path.join(hedef_klasor, kume_adi, sinif)
            os.makedirs(hedef_yol, exist_ok=True)
            for resim in kume_resimleri:
                shutil.copy(os.path.join(sinif_yolu, resim), os.path.join(hedef_yol, resim))
        
        print(f"Sınıf İşlendi: {sinif} | Toplam: {toplam_resim} adet")

if __name__ == '__main__':
    veri_setini_hazirla()
