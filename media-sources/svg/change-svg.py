import os
import xml.etree.ElementTree as ET

# PAYLOAD
directorio = "." 
ancho = 30  # Ancho en píxeles
alto = 30   # Alto en píxeles
color_relleno = "#00000000"  #relleno
color_stroke = "#FFF"  #lineas


def modificar_svg(archivo_svg, ancho, alto, color_relleno, color_stroke):
    # Cargar el archivo SVG
    tree = ET.parse(archivo_svg)
    root = tree.getroot()

    # Modificar ancho y alto del SVG
    root.set("width", f"{ancho}px")
    root.set("height", f"{alto}px")

    # Tipos de elementos gráficos que queremos modificar
    elementos_graficos = ["circle", "ellipse", "line", "polyline", "polygon", "path"]

    # Modificar color de relleno y color de trazo en cada tipo de elemento gráfico
    for elemento in elementos_graficos:
        for item in root.findall(f".//{{*}}{elemento}"):
            item.set("fill", color_relleno)
            item.set("stroke", color_stroke)

    # Guardar los cambios en el archivo SVG
    tree.write(archivo_svg)

def modificar_svgs_en_directorio(directorio, ancho, alto, color_relleno, color_stroke):
    # Obtener todos los archivos .svg en el directorio
    archivos_svg = [f for f in os.listdir(directorio) if f.endswith('.svg')]

    # Recorrer cada archivo y aplicar las modificaciones
    for archivo in archivos_svg:
        ruta_completa = os.path.join(directorio, archivo)
        modificar_svg(ruta_completa, ancho, alto, color_relleno, color_stroke)
        print(f"Modificado: {ruta_completa}")

modificar_svgs_en_directorio(directorio, ancho, alto, color_relleno, color_stroke)
