import random
import time
from datetime import datetime

class ShakeDetector:
    def __init__(self, sensitivity=3):
        """Simulates shake detection with configurable sensitivity
        Args:
            sensitivity (int): 1-5 where 1=most sensitive, 5=least sensitive
        """
        self.sensitivity = max(1, min(5, sensitivity))
        self.last_detection = None
        
    def detect_shake(self):
        """Simulates shake detection for prototype purposes"""
        time.sleep(0.3)  # Simulate sensor delay
        if random.random() < (0.25 * (6 - self.sensitivity)):
            self.last_detection = datetime.now()
            return True
        return False
    
    def get_last_shake_time(self):
        return self.last_detection
