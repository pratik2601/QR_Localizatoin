import qrcode

img1=qrcode.make("10")
img1.save('QR_Tag1.png')
img2=qrcode.make("20")
img2.save('QR_Tag2.png')

img1=qrcode.make("30")
img1.save('QR_Tag3.png')
img2=qrcode.make("40")
img2.save('QR_Tag4.png')