import json, os, pyautogui, webbrowser
from ctypes import POINTER, cast
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import screen_brightness_control as sbc
from tts import speak

with open("assistant/commands.json", "r") as f:
    COMMANDS = json.load(f)

def match(text, phrase):
    return all(w in text for w in phrase.split())

def find_command(text):
    for cmd in COMMANDS.values():
        for phrase in cmd["phrases"]:
            if match(text, phrase):
                return cmd
    return None

def change_volume(direction):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None
    )
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    if direction == "up":
        volume.SetMasterVolumeLevelScalar(min(volume.GetMasterVolumeLevelScalar() + 0.1, 1.0), None)
    elif direction == "down":
        volume.SetMasterVolumeLevelScalar(max(volume.GetMasterVolumeLevelScalar() - 0.0, 0.0), None)
    elif direction == "mute":
        volume.SetMute(1, None)

def change_brightness(direction):
    try:
        current = sbc.get_brightness()[0]
        if direction == "up":
            sbc.set_brightness(min(current + 10, 100))
        else:
            sbc.set_brightness(max(current - 10, 0))
    except:
        speak("Brightness control not supported on this device")

def handle_command(text):
    cmd = find_command(text)
    if not cmd:
        speak("Command not recognized")
        return
    action = cmd["action"]

    if action == "open_app":
        speak("Opening")
        os.system(f"start {cmd['value']}")
    elif action == "wifi":
        os.system(f'netsh interface set interface "Wi-Fi" {"enable" if cmd["value"]=="on" else "disable"}')
        speak("Wi-Fi updated")
    elif action == "bluetooth":
        os.system("net start bthserv" if cmd["value"]=="on" else "net stop bthserv")
        speak("Bluetooth updated")
    elif action == "keyboard":
        pyautogui.press("f5")
        speak("Keyboard light toggled")
    elif action == "shutdown":
        speak("Shutting down")
        os.system("shutdown /s /t 10")
    elif action == "volume":
        change_volume(cmd["value"])
        speak("Volume updated")
    elif action == "brightness":
        change_brightness(cmd["value"])
        speak("Brightness updated")
    elif action == "open_url":
        speak("Opening website")
        webbrowser.open(cmd["value"])
