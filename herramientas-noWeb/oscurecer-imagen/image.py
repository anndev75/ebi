from PIL import Image, ImageEnhance
#Payload
ruta_de_la_imagen = "fondo.jpg"
nivel_opacidad = 0.5 

imagen = Image.open(ruta_de_la_imagen)
enhancer = ImageEnhance.Brightness(imagen)
imagen_oscurecida = enhancer.enhance(nivel_opacidad)
imagen_oscurecida.save("oscurecida_"+ruta_de_la_imagen)
