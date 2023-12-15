import cv2
from pyzbar import pyzbar


capture = cv2.VideoCapture(0)

while capture.isOpened():
    ret, frame = capture.read()
    if not ret:
        
        break
    barcodes = pyzbar.decode(frame)
    
    for barcode in barcodes:
        barcode_value = barcode.data.decode('utf-8')
        
    cv2.imshow('Lector de codigo de barras', frame)
    
    if barcodes:
        print(f'Código de barras: {barcode_value}')
        break
    
    elif cv2.waitKey(1)== ord('q'):
        break
    
capture.release()
cv2.destroyAllWindows()

