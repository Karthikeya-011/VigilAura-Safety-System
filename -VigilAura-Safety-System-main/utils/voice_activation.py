# utils/voice_activation.py

import speech_recognition as sr

def listen_for_keyword(safe_word="help"):
    """Listens for the safe word using the microphone."""
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🔊 Say something...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=4)
            text = recognizer.recognize_google(audio).lower()
            print(f"🗣️ You said: {text}")
            return safe_word.lower() in text
        except sr.WaitTimeoutError:
            print("⏱️ No speech detected (timeout)")
        except sr.UnknownValueError:
            print("❓ Could not understand audio")
        except sr.RequestError as e:
            print(f"🌐 API Error: {e}")
        except Exception as e:
            print(f"🎤 Error during voice recognition: {e}")

    return False
