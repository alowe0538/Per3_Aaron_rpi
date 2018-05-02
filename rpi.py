from gpiozero import LED
from time import sleep

def blink(time):
    """Turn on the LED light for a user-specified amount of time."""
    sunshine.on()
    sleep(time)
    sunshine.off()

sunshine = LED(17)

while True:
    blink(1)
    sleep(1.5)
