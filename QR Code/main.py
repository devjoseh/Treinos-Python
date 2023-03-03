#Faz a importação do qrcode (pip install qrcode para baixar)
import qrcode

#Texto que irá aparecer quando alguém ler o qrcode
data = 'Salve familia'

#Cria a imagem usando a mensagem configurada no data
img = qrcode.make(data)

#Local em que a imagem será salva, troque o \ do local para / se não vai dar erro essa bomba
img.save('C:/Users/matap/Desktop/Treinos Python/QR Code/Imgs/myqrcode.png')