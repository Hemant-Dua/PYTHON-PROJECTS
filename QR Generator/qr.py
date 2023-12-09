# Importing library
import qrcode

# Data to be encoded
data = input("Type the Message : ")
 
# Encoding data using make() function
img = qrcode.make(data)
 
# Saving as an image file
img.save('QR Generator//MyQRCode.png')