import qrcode

data = 'Salve familia'

img = qrcode.make(data)

img.save('C:/Users/matap/Desktop/Treinos Python/QR Code/Imgs/myqrcode.png')