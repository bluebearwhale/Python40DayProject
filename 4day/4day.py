import qrcode

qr_data='www.naver.com'
#qr코드 생성
qr_img=qrcode.make(qr_data)
save_path='4day\\'+qr_data+'.png'
qr_img.save(save_path)

