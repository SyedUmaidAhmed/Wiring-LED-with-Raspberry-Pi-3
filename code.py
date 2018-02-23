from gpiozero import LED
from time import sleep
red_light = LED(17)
red_light.blink()
