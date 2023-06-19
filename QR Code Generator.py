import pyqrcode
#import pypng
import qrcode
from pyqrcode import QRCode


website = "www.eventbrite.com"

url = pyqrcode.create(website)

url.png('myqr.png', scale = 6)


print("Hello world")

img = qrcode.make(website)
img.save('QrCode1.png')

print(img.save)
