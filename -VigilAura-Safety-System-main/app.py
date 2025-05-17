from flask import Flask, jsonify, render_template, request
import json, smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load configuration from config.json
with open("config.json") as f:
    config = json.load(f)

SENDER_EMAIL = config["sender_email"]
APP_PASSWORD = config["app_password"]
RECEIVER_EMAILS = config["receiver_emails"]

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/sos")
def sos():
    subject = "🚨 SOS Alert from VigilAura"
    body = "Emergency! The user triggered SOS from VigilAura. Please check immediately."
    success = send_email(subject, body)
    return jsonify({"status": "🚨 SOS Sent to contacts!" if success else "❌ Failed to send SOS!"})

@app.route("/fake_call")
def fake_call():
    return jsonify({"status": "📞 Fake call initiated"})

@app.route("/share_location")
def share_location():
    lat = request.args.get("lat")
    lng = request.args.get("lng")

    if not lat or not lng:
        return jsonify({"status": "❌ Location not received"})

    location_link = f"https://maps.google.com/?q={lat},{lng}"
    subject = "📍 Location Shared from VigilAura"
    body = f"The user shared their location:\n\n{location_link}"
    send_email(subject, body)
    return jsonify({"status": "📍 Location shared with contacts"})

def send_email(subject, body):
    try:
        msg = MIMEMultipart()
        msg["From"] = SENDER_EMAIL
        msg["To"] = ", ".join(RECEIVER_EMAILS)
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAILS, msg.as_string())
        server.quit()
        print("✅ Email sent successfully.")
        return True
    except Exception as e:
        print(f"❌ Email failed: {e}")
        return False

if __name__ == "__main__":
    app.run(debug=True)
