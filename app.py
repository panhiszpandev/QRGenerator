import random
import segno

def generateHash():
    value = random.getrandbits(64)
    return hash(value)

def generateUrl(baseUrl, hashedValue):
    enchancedUrl = baseUrl + str(hashedValue)
    return enchancedUrl

def generateQRCode(url, hashedValue):
    qrcode = segno.make_qr(url)
    qrcode.save(str(hashedValue)+".png", scale=5, kind='png')


baseUrl = 'http://192.168.1.141:8001/storage/'
i = 0
while i < 24:
    hashedValue = generateHash()
    url = generateUrl(baseUrl, hashedValue)
    generateQRCode(url, hashedValue)
    i = i + 1

# http://192.168.1.141:8001/storage/9387604709039283592
