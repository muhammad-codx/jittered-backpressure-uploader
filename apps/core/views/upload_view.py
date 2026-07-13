import time
from config.jitter_settings import JITTER_CONFIG
from config.jitter import jitter

class JitteredUploaderService:
    
    @staticmethod
    def process_upload(task_type: str, payload: dict) -> float:

        base_delay = JITTER_CONFIG.get(task_type, {}).get("BASE_DELAY", 10.0)
        

        calculated_delay = jitter(quantity=base_delay)

        time.sleep(calculated_delay)
        

        
        return calculated_delay