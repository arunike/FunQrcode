import os
from amzqr import amzqr

version, level, qr_name = amzqr.run(

    words = 'https://arunike.github.io/', ## Link must be in https/http format
    version = 20, ## Size length of QR code, range from 1 to 40
    level = 'H', ## Error correction level, range L, M, Q, H
    picture = 'coding.gif', ## Picture to be embedded in QR code
    colorized = True, ## Colorized QR code
    contrast = 1.0, ## Contrast of QR code
    brightness = 1.0, ## Brightness of QR code
    save_name = "qrcode.gif", ## Name of QR code
    save_dir = os.getcwd() ## Directory to save QR code
)