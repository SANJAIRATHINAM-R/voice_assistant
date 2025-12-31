import pystray
from PIL import Image

def start_tray():
    icon = Image.new("RGB", (64,64), color="black")
    pystray.Icon("Assistant", icon).run_detached()
