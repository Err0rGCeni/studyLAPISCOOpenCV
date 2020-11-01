#"python.linting.pylintArgs": ["--extension-pkg-whitelist=cv2"]
import cv2 #OpenCV
import numpy as np #Arrays
import matplotlib.pyplot as plt #Plots
img = cv2.imread('/home/gceni/virtualenvs/gcPDI/imgPDI/female01.tiff')
print(type(img))
cv2.imshow('Image', img)
cv2.waitKey(0)
#Melhor usar ESC para evitar bug
cv2.destroyAllWindows()
cv2.threshold()