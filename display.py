#Waveshare 1.44inch LCD HAT 128x128
import time
import os
import board
import busio
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_rgb_display.st7735 as st7735

# Initialize SPI bus and control pins for the display
spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = digitalio.DigitalInOut(board.D27)

# Initialize display object
display = st7735.ST7735R(spi, cs=cs_pin, dc=dc_pin, rst=reset_pin, baudrate=16000000, width=128, height=128)
display.rotation = 270

# Set font and font size
font = ImageFont.load_default()
font_size = 8

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

    # Calculate center positions for each line of text
    text_width, text_height = font.getsize(hostname)
    x = (display.width - text_width) / 2
    y = (display.height - (text_height * 4 + font_size * 3)) / 9

    # Draw text on image
    draw.rectangle((0, 0, display.width, display.height), fill=background_color)
    draw.text((x, y), hostname, font=font, fill=text_color)
    draw.text((x, y + text_height + font_size), wifi_network, font=font, fill=text_color)
    draw.text((x, y + 2 * (text_height + font_size)), ip_address, font=font, fill=text_color)
    draw.text((x, y + 3 * (text_height + font_size)), uptime, font=font, fill=text_color)

    # Display the image on the screen
    display.image(image)

    # Wait for 5 seconds before updating the image again
    time.sleep(5)
