import time
from config.jitter_settings import JITTER_CONFIG
from config.jitter import jitter

class JitteredBackpressureUploader:
    def __init__(self, task_type="db_sync"):
        self.task_type = task_type

    def flush_buffer_to_destination(self, data_chunk):
        """
        Keshdagi ma'lumotlarni manzilga yuklash (upload) funksiyasi
        """
        # 2. Config'dan loyiha uchun belgilangan BASE_DELAY ni olamiz (Masalan: 10.0)
        base_delay = JITTER_CONFIG[self.task_type]["BASE_DELAY"]
        
        # 3. KELTIRILGAN SHU BASE_DELAY NI `quantity` SIFATIDA BERIB YUBORAMIZ:
        # Funksiya bizga 5.0 va 10.0 sekund oralig'ida float qiymat qaytaradi (Masalan: 7.34)
        calculated_delay = jitter(quantity=base_delay)
        
        print(f"[JBU] Backpressure ishga tushdi. Server yuklamasini kamaytirish uchun {calculated_delay:.2f}s kutilmoqda...")
        
        # 4. Tizimni dynamic hisoblangan vaqt davomida to'xtatib turamiz
        time.sleep(calculated_delay)
        
        # 5. Kutish tugagach, yuklash (upload) bajariladi
        self._execute_upload(data_chunk)

    def _execute_upload(self, data):
        # Haqiqiy yuklash kodi shu yerda bo'ladi
        print("[JBU] Ma'lumotlar muvaffaqiyatli yuklandi!")