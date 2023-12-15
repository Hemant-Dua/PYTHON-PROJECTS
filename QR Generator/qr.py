import qrcode

data = input("Type the Message : ")
img = qrcode.make(data)
img.save('QR Generator//MyQRCode.png')