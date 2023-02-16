import board
import busio
import digitalio
import adafruit_rgb_display.st7735 as st7735
import subprocess

# Initialize SPI bus and control pins for the display
spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = digitalio.DigitalInOut(board.D27)
BUTTON_1 = digitalio.DigitalInOut(board.D21)
BUTTON_2 = digitalio.DigitalInOut(board.D20)
BUTTON_3 = digitalio.DigitalInOut(board.D16)

# Initialize display object
display = st7735.ST7735R(spi, cs=cs_pin, dc=dc_pin, rst=reset_pin, baudrate=16000000, width=128, height=128)
display.rotation = 270

# Button Configurations
BUTTON_1.switch_to_input(pull=digitalio.Pull.UP)
BUTTON_2.switch_to_input(pull=digitalio.Pull.UP)
BUTTON_3.switch_to_input(pull=digitalio.Pull.UP)

while True:
    # Wait for 5 seconds before updating the image again
    #time.sleep(5)
    if not BUTTON_1.value:
        # Stop the service
        subprocess.run(['sudo', 'systemctl', 'stop', 'display'])
    elif not BUTTON_2.value:
        # Restart the service
        subprocess.run(['sudo', 'systemctl', 'restart', 'display'])
    elif not BUTTON_3.value:
        # Reboot the device
        subprocess.run(['sudo', 'reboot'])
