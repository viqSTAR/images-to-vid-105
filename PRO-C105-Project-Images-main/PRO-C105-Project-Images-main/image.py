import cv2
import os

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter('output.avi', fourcc, 30.0, (1920, 1080))

path = 'Images/'
images = [img for img in os.listdir(path) if img.endswith('.jpg')]

for image_name in images:
    image = cv2.imread(os.path.join(path, image_name))
    out.write(image)

out.release()