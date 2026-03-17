import tkinter as tk
from tkinter import scrolledtext
import threading
import speech_recognition as sr
import pyttsx3

# ---------------- GUI ----------------
root = tk.Tk()
root.title("HARI – Voice Assistant")
root.geometry("600x450")
root.configure(bg="#121212")

title = tk.Label(root, text="🤖 HARI – Voice Assistant",
                 font=("Arial", 16, "bold"),
                 bg="#121212", fg="white")
title.pack(pady=10)

output = scrolledtext.ScrolledText(
    root, font=("Consolas", 12),
    bg="#1e1e1e", fg="white"
)
output.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# ---------------- TTS (MAIN THREAD) ----------------
engine = pyttsx3.init()

def speak(text):
    output.insert(tk.END, f"HARI: {text}\n")
    output.see(tk.END)
    engine.say(text)
    engine.runAndWait()

# ---------------- VOICE ----------------
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as src:
        r.adjust_for_ambient_noise(src)
        audio = r.listen(src)
    try:
        return r.recognize_google(audio)
    except:
        return "I could not hear you"

# ---------------- WORKER ----------------
def run():
    speak("Listening...")
    text = listen()
    output.insert(tk.END, f"You: {text}\n")
    speak("You said " + text)

def start():
    threading.Thread(target=run, daemon=True).start()

btn = tk.Button(
    root, text="🎤 Speak",
    font=("Arial", 16),
    bg="#4CAF50", fg="white",
    command=start
)
btn.pack(pady=10)

speak("Hello! I am HARI.")
root.mainloop()
