from PIL import Image, ImageDraw, ImageFont
import math
import textwrap
import os

ralsei_sprites = ["angry", "classic", "happy", "light_blush", "light_classic", "light_happy", "lookdown",
                  "lookdown_blush", "sad", "sad_blush", "sad_fangs", "ser", "stare"]


def ralsay_adv(text, sprite):
    text, sprite = text.lower(), sprite.lower()
    if sprite not in ralsei_sprites:
        print("Invalid sprite!")
    elif len(text) > 72:
        print("Text too long!")
    else:
        img_text = '\n'.join(textwrap.wrap(text, 26))

        im = Image.open(f"ralsei_faces/{sprite}.png")
        fnt = ImageFont.truetype("DTM-Mono.otf", 24)
        d = ImageDraw.Draw(im)
        d.multiline_text((160, 40), img_text, font=fnt, fill="#ffffff")
        im.save(f"result.png")
        return "Success!"


ralsay_adv("Hello, world!", "happy")
