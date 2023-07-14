import time
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import board
import digitalio

keyboard = Keyboard(usb_hid.devices)

led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

led.value = False
time.sleep(5)

while True:
    led.value = True
    keyboard.press(Keycode.CAPS_LOCK)
    keyboard.release_all()
    led.value = False
    time.sleep(60)
