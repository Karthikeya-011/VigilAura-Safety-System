import smtplib
import json
from datetime import datetime
from utils.location import get_location

class AlertSystem:
    def __init__(self, config_file='config.json'):
        """Initialize alert system with configuration"""
        self.config = self._load_config(config_file)
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        
    def _load_config(self, config_file):
        """Load configuration from JSON file"""
        try:
            with open(config_file) as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {
                "email": {
                    "sender": "your_email@gmail.com",
                    "password": "your_app_password", 
                    "recipients": ["emergency@example.com"]
                }
            }
    
    def send_alert(self, message):
        """Send emergency alert with location"""
        location = get_location()
        email_text = f"""\
Subject: 🚨 VigilAura Alert: {message}

Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Location: {location.get('lat')}, {location.get('lng')}
Map: https://www.google.com/maps?q={location.get('lat')},{location.get('lng')}
"""
        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(
                    self.config["email"]["sender"],
                    self.config["email"]["password"]
                )
                for recipient in self.config["email"]["recipients"]:
                    server.sendmail(
                        self.config["email"]["sender"],
                        recipient,
                        email_text
                    )
            return True
        except Exception as e:
            print(f"Alert failed: {str(e)}")
            return False
