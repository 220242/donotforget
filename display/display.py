#Waveshare 1.44inch LCD HAT 128x128
import time
import os
import board
import busio
import digitalio
from PIL import Image, ImageDraw, ImageFont
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

# Set font and font size
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")
font_size = 6

# Set background color to black
background_color = (0, 0, 0)

# Set text color to white
text_color = (255, 255, 255)

while True:
    # Create blank image for drawing
    image = Image.new("RGB", (display.width, display.height))
    draw = ImageDraw.Draw(image)

    # Get the hostname, wifi network name, IP address, and system uptime
    hostname = os.popen("hostname -s").read().strip()
    wifi_network = os.popen("iwgetid -r wlan0").read().strip()
    ip_address = os.popen("hostname -I").read().strip()
    uptime = os.popen("uptime -p").read().strip()
    bitrate = subprocess.run(["iwconfig wlan0 | awk -F= '/Bit Rate/ {print $2}' | awk -F/ '{print $1}'"], shell=True, capture_output=True, text=True)
    bitrateoutput = bitrate.stdout.strip() + "/s"
    quality = subprocess.run(["iwconfig wlan0 | awk -F= '/Signal level/ {print $2}' | awk '{print $1}'"], shell=True, capture_output=True, text=True)
    signal = subprocess.run(["iwconfig wlan0 | awk '/Signal level/ {gsub(\"level=\",\"\",$4); print $4}'"], shell=True, capture_output=True, text=True)
    qualityoutput = "LQ:" + quality.stdout.strip() + " SL:" + signal.stdout.strip() + "dBm"
    frequency = subprocess.run(["iwconfig wlan0 | awk '/Frequency/ {print $2}' | cut -d: -f2"], shell=True, capture_output=True, text=True)
    frequencyoutput = frequency.stdout.strip() + "GHz"

    # Calculate center positions for each line of text
    text_width, text_height = font.getsize(hostname)
    x = (display.width - text_width) / 2
    y = (display.height - (text_height * 4 + font_size * 3)) / 9

    # Draw text on image
    draw.rectangle((0, 0, display.width, display.height), fill=background_color)
    draw.text((5, 0), hostname, font=font, fill=text_color)
    draw.text((5, 10), wifi_network, font=font, fill=text_color)
    draw.text((80, 10), frequencyoutput, font=font, fill=text_color)
    draw.text((5, 20), ip_address, font=font, fill=text_color)
    draw.text((15, 30), qualityoutput, font=font, fill=text_color)
    draw.text((5, 115), uptime, font=font, fill=text_color)
    draw.text((80, 0), bitrateoutput, font=font, fill=text_color)

    # Display the image on the screen
    display.image(image)

    # Wait for 5 seconds before updating the image again
    time.sleep(1)
    
