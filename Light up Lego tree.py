"""
    neopixel_random.py

    Repeatedly displays random colours onto the LED strip.
    This example requires a strip of 8 Neopixels (WS2812) connected to pin0.

  Credit this code is a modified version of the original from here:
  https://microbit-micropython.readthedocs.io/en/latest/neopixel.html

"""
from microbit import *
import neopixel
from random import randint

# Setup the Neopixel strip on pin0 with a length of 8 pixels
np = neopixel.NeoPixel(pin0, 1)

while True:
    #Iterate over each LED in the strip
    if button_a.was_pressed():
        for pixel_id in range(0, len(np)):
            red = randint(0, 255)
            green = randint(0, 255)
            blue = randint(0, 255)
    
            # Assign the current LED a random red, green and blue value between 0 and 60
            np[pixel_id] = (red, green, blue)
    
            # Display the current pixel data on the Neopixel strip
            np.show()
            sleep(1000)
    
    if button_b.was_pressed():
        for pixel_id in range(0, len(np)):
            red = 0
            green = 0
            blue = 0
                        # Assign the current LED a random red, green and blue value between 0 and 60
            np[pixel_id] = (red, green, blue)
    
            # Display the current pixel data on the Neopixel strip
            np.show()

            # Display the current pixel data on the Neopixel stri
            sleep(1000)
