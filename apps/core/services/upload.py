from apps.core.models.jbu_db import Data
import time
import logging
from config.jitter_settings import JITTER_CONFIG
from config.jitter import jitter

logger = logging.getLogger(__name__)

class DataService:
    @staticmethod
    def create_data(validated_data):
        return Data.objects.create(**validated_data)

class JitteredBackpressureService:
    @staticmethod
    def upload_data(task_type, data_chunk):
        task_config = JITTER_CONFIG.get(task_type)
        if not task_config:
            raise ValueError(f"'{task_type}' uchun konfiguratsiya topilmadi!")

        base_delay = task_config.get("BASE_DELAY", 5.0)
        calculated_delay = jitter(quantity=base_delay)
        
        logger.info(f"[JBU] {task_type} uchun {calculated_delay:.2f}s kechikish.")
        time.sleep(calculated_delay)
        
        # Bu yerda ma'lumotni yuklash mantiqi
        print(f"[JBU] Yuklandi: {data_chunk}")
        return True