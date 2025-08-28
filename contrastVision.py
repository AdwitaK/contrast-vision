import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    b, g, r = cv2.split(frame)
    contrast = np.zeros_like(frame)
    
    # Change pixel colours
    contrast[(r >= 128) & (g < 128) & (b < 128)] = [50,48,255]  # Red
    contrast[(g >= 128) & (r < 128) & (b < 128)] = [21,238,116]  # Green
    contrast[(b >= 128) & (r < 128) & (g < 128)] = [255,30,0]  # Blue
    contrast[(r >= 128) & (g >= 128) & (b < 128)] = [0,231,255]  # Yellow
    contrast[(r >= 128) & (b >= 128) & (g < 128)] = [255, 0, 240]  # Magenta
    contrast[(g >= 128) & (b >= 128) & (r < 128)] = [234,238,77]  # Cyan
    contrast[(r < 128) & (g < 128) & (b < 128)] = [0, 0, 0]  # Black
    contrast[(r >= 128) & (g >= 128) & (b >= 128)] = [255, 255, 255]  # White
    
    #Output
    cv2.imshow("Contrasted video", contrast)
    
   # Press any key to exit
    if cv2.waitKey(1) > -1:
        break
    
cv2.destroyAllWindows()
