import os
import cv2

path = "C:/Users/Lenovo Franco/Desktop/BYJUS/Proyecto 105/Imagenes"
imagenes = []
for i in os.listdir(path):
    name, extencion = os.path.splitext(i)
    if extencion in [".png", ".jpg", ".jpeg", ".gif"]:
        file_name = path + "/" + i
        print(file_name)
        imagenes.append(file_name)
count = len(imagenes)
frame = cv2.imread(imagenes[0])
height, width, layers = frame.shape
size = (width, height)
print(size)
out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)
for l in range(0, count-1):
    print(imagenes[l])
    frame = cv2.imread(imagenes[l])
    out.write(frame)
out.release()
print("Listo")