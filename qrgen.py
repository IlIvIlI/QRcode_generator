import pyqrcode 
from pyqrcode import QRCode

nopass = False

# String which represent the QR code
isWifiQR = input('Is it gonna be wifi QRcode (y/n)? ')
if isWifiQR == 'y'.lower(): 
	security = input('Enter security type (WPA/WPA2/WEP/nopass): ')
	if security == 'nopass':
		password = ''
		nopass = True
	SSID = input('Enter SSID: ')
	if not nopass:
		password = input('Enter the password: ')

	data = f'WIFI:T:{security};S:{SSID};P:{password};;' #WIFI:T:WPA;S:mynetwork;P:mypass;; order of parameters does not matter.\
														#source: https://github.com/zxing/zxing/wiki/Barcode-Contents#wi-fi-network-config-android-ios-11
else:	
	data = input('Enter the data to scan: ')
qrcode_size = int(input('Enter size of QRcode (1-10): '))
qrcode_name = input(f'\nWARNING! If you name file as existing one, it will rewrite that file with new data.\n\nEnter name of qrcode file (you may not fill this field. Default name will be applied): ')


if qrcode_size < 0:
	qrcode_size = 1
if qrcode_size > 10:
	qrcode_size = 10

file_type = input('Save file as (png/svg)? ')
qrcode = pyqrcode.create(data) # Generate QR code
if file_type == 'png':
	qrcode.png(f"{qrcode_name}.png", scale = qrcode_size) # "myqr.png"
	qrcode.show()
if file_type == 'svg':
	qrcode.svg(f"{qrcode_name}.svg", scale = qrcode_size)
else: #in case incorrect file type, .png will be set
	qrcode.png(f"{qrcode_name}.png", scale = qrcode_size) # "myqr.png"
	qrcode.show()
print('DONE!')	
