"""
PYTHON UNIVERSE 🚀
A single-file mega Python program
Author: You 😎
"""

import os
import sys
import time
import random
import math
import socket
import platform
from datetime import datetime

# ---------- UTILS ----------
def slow(text, speed=0.02):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(speed)
    print()

def line():
    print("-" * 60)

# ---------- LOGIN SYSTEM ----------
USERS = {"admin": "1234"}

def login():
    slow("🔐 Welcome to PYTHON UNIVERSE")
    for _ in range(3):
        u = input("Username: ")
        p = input("Password: ")
        if USERS.get(u) == p:
            slow(f"✅ Access granted, {u}!")
            return True
        else:
            slow("❌ Wrong credentials")
    return False

# ---------- INTERNET CHECK ----------
def internet():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=2)
        print("🌐 Internet: CONNECTED")
    except:
        print("🌐 Internet: DISCONNECTED")

# ---------- SYSTEM INFO ----------
def system_info():
    line()
    print("🖥 System Information")
    print("OS:", platform.system())
    print("Version:", platform.version())
    print("Processor:", platform.processor())
    print("Python:", platform.python_version())
    print("Time:", datetime.now())
    line()

# ---------- NOTES APP ----------
def notes():
    with open("notes.txt", "a+") as f:
        note = input("📝 Write note: ")
        f.write(note + "\n")
    print("✅ Saved to notes.txt")

# ---------- PASSWORD GENERATOR ----------
def password():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%"
    length = int(input("Password length: "))
    pwd = "".join(random.choice(chars) for _ in range(length))
    print("🔑 Password:", pwd)

# ---------- CALCULATOR ----------
def calculator():
    expr = input("Enter math expression (e.g. 5*sin(30)): ")
    try:
        result = eval(expr, {"__builtins__": None}, math.__dict__)
        print("Result:", result)
    except:
        print("❌ Invalid expression")

# ---------- FILE EXPLORER ----------
def files():
    path = input("Enter path (or .): ")
    try:
        for f in os.listdir(path):
            print("📁", f)
    except:
        print("❌ Invalid path")

# ---------- AI CHAT (RULE BASED) ----------
def ai_chat():
    slow("🤖 AI is online. Type 'exit' to leave.")
    while True:
        msg = input("You: ").lower()
        if msg == "exit":
            break
        elif "hello" in msg:
            print("AI: Hello human 👋")
        elif "time" in msg:
            print("AI:", datetime.now())
        elif "python" in msg:
            print("AI: Python is powerful, just like you 😎")
        else:
            print("AI: Interesting... tell me more.")

# ---------- COMMAND CENTER ----------
def command_center():
    commands = {
        "help": "Show commands",
        "sys": "System info",
        "net": "Internet status",
        "note": "Write note",
        "calc": "Calculator",
        "pwd": "Password generator",
        "files": "File explorer",
        "ai": "Chat with AI",
        "exit": "Exit Universe"
    }

    while True:
        cmd = input("🧠 PYTHON-OS > ").lower()

        if cmd == "help":
            for k, v in commands.items():
                print(f"{k} → {v}")

        elif cmd == "sys":
            system_info()

        elif cmd == "net":
            internet()

        elif cmd == "note":
            notes()

        elif cmd == "calc":
            calculator()

        elif cmd == "pwd":
            password()

        elif cmd == "files":
            files()

        elif cmd == "ai":
            ai_chat()

        elif cmd == "exit":
            slow("👋 Shutting down PYTHON UNIVERSE...")
            break

        else:
            print("❓ Unknown command. Type 'help'")

# ---------- MAIN ----------
if __name__ == "__main__":
    if login():
        command_center()
    else:
        slow("🚫 Too many attempts. System locked.")
