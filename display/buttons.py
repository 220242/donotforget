import board
import busio
import digitalio
import adafruit_rgb_display.st7735 as st7735
import subprocess
import time

# Initialize SPI bus and control pins for the display
spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = digitalio.DigitalInOut(board.D27)
#BUTTON_1 = digitalio.DigitalInOut(board.D21)
BUTTON_2 = digitalio.DigitalInOut(board.D20)
BUTTON_3 = digitalio.DigitalInOut(board.D16)
BUTTON_UP = digitalio.DigitalInOut(board.D6)
BUTTON_DOWN = digitalio.DigitalInOut(board.D19)
BUTTON_LEFT = digitalio.DigitalInOut(board.D5)
BUTTON_RIGHT = digitalio.DigitalInOut(board.D26)
BUTTON_PRESS = digitalio.DigitalInOut(board.D13)

# Initialize display object
display = st7735.ST7735R(spi, cs=cs_pin, dc=dc_pin, rst=reset_pin, baudrate=16000000, width=128, height=128)
display.rotation = 270

# Button Configurations
#BUTTON_1.switch_to_input(pull=digitalio.Pull.UP)
BUTTON_2.switch_to_input(pull=digitalio.Pull.UP)
BUTTON_3.switch_to_input(pull=digitalio.Pull.UP)
BUTTON_UP.switch_to_input(pull=digitalio.Pull.UP)
BUTTON_DOWN.switch_to_input(pull=digitalio.Pull.UP)
BUTTON_LEFT.switch_to_input(pull=digitalio.Pull.UP)
BUTTON_RIGHT.switch_to_input(pull=digitalio.Pull.UP)
BUTTON_PRESS.switch_to_input(pull=digitalio.Pull.UP)

while True:
    if not BUTTON_2.value:
        subprocess.run(['sudo', 'systemctl', 'restart' , 'display'])
        time.sleep(1)
    elif not BUTTON_3.value:
        subprocess.run(['sudo', 'systemctl', 'stop' , 'display'])
        time.sleep(1)
    elif not BUTTON_UP.value:
        print("up")
        time.sleep(1)
    elif not BUTTON_DOWN.value:
        print("DOWN")
        time.sleep(1)
    elif not BUTTON_LEFT.value:
        subprocess.run(['sudo', 'ifconfig', 'wlan0', 'up'])
        time.sleep(1)
    elif not BUTTON_RIGHT.value:
        subprocess.run(['sudo', 'ifconfig', 'wlan0', 'down'])
        time.sleep(1)
    elif not BUTTON_PRESS.value:
        print("PRESS")
        time.sleep(1)
    time.sleep(0.01)
