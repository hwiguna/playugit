"""
hello.py

    Writes "Hello!" in random colors at random locations on the display.
"""

import random
import utime
import st7789
import tft_config
import vga1_bold_16x32 as font

tft = tft_config.config(0)

def center(text):
    length = len(text)
    tft.text(
        font,
        text,
        tft.width() // 2 - length // 2 * font.WIDTH,
        tft.height() // 2 - font.HEIGHT,
        st7789.WHITE,
        st7789.RED)

def main():
    tft.init()
    tft.rotation(1)

    tft.fill(st7789.RED)
    center("Hello 01")

main()
