from PIL import Image
img = Image.open("fondo-pantalla.jpg")

img.rotate(90).save('rotated90.png')