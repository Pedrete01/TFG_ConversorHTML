import sys
import webbrowser

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                              ELEMENTOS
#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def boton():
    boton = """<button class="button">Boton</button>"""
    return boton

def formulario():
    form = """ <li>
    <label for="form">Texto:</label>
    <input type="text" id="form" name="texto">
    </li>"""
    return form

def menu():
    menu = """<header>
		<div class="menu_bar">
			<a href="#" class="bt-menu"><span class="icon-list2"></span>Menú</a>
		</div>

		<nav>
			<ul>
				<li><a href="#"><span class="icon-house"></span>Inicio</a></li>
				<li><a href="#"><span class="icon-suitcase"></span>Trabajos</a></li>
				<li class="submenu">
					<a href="#"><span class="icon-rocket"></span>Proyectos<span class="caret icon-arrow-down6"></span></a>
					<ul class="children">
						<li><a href="#">SubElemento #1 <span class="icon-dot"></span></a></li>
						<li><a href="#">SubElemento #2 <span class="icon-dot"></span></a></li>
						<li><a href="#">SubElemento #3 <span class="icon-dot"></span></a></li>
					</ul>
				</li>
				<li><a href="#"><span class="icon-earth"></span>Servicios</a></li>
				<li><a href="#"><span class="icon-mail"></span>Contacto</a></li>
			</ul>
		</nav>
	</header>"""
    return menu

def etiqueta():
    etiqueta = "<label>Etiqueta</label>"
    return etiqueta

def radioButton():
    radio = """<div>
      <input type="radio" id="radio" name="redioButton" value="ejemplo">
      <label for="radio">Radio Button de ejemplo</label>
    </div>"""
    return radio

def checkbutton():
    check = """<div><input type="checkbox" id="checkbutton" name="checkbutton" value="checkbutton ejemplo">
    <label for="checkbutton"> CheckButton de ejemplo</label></div>"""
    return check

def paginacion():
    paginacion = """<section class="paginacion">
			<ul>
				<li><a href="pagina1.html" class="active">1</a></li>
				<li><a href="pagina2.html">2</a></li>
				<li><a href="pagina3.html">3</a></li>
				<li><a href="pagina4.html">4</a></li>
				<li><a href="pagina5.html">5</a></li>
			</ul>
		</section>"""
    return paginacion

def desplegable():
    desplegable = """<select name="desplegable" class="desp">
        <option value="1" checked>Ejemplo 1</option>
        <option value="2">Ejemplo 2</option>
        <option value="3">Ejemplo 3</option>
        <option value="4">Ejemplo 4</option>
        <option value="5">Ejemplo 5</option>
        <option value="6">Ejemplo 6</option>
        <option value="7">Ejemplo 7</option>
        <option value="8">Ejemplo 8</option>
      </select>"""
    return desplegable

def icono():
    icono = """<i class="fa-solid fa-house"></i>"""
    return icono

def lista():
    lista = """<ol>
  <li>Elemento 1</li>
  <li>Elemento 2</li>
  <li>Elemento 3</li>
</ol>"""
    return lista

def imagen():
    imagen = """<img src="./Imagenes/imagen.webp" class="imagen">"""
    return imagen

def texto():
    texto = """<p class="texto">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor 
    incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation 
    ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit 
    in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat 
    non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>"""
    return texto

def video():
    video = "<img src=\"./Imagenes/imagen.webp\">"
    return video

def footer():
    footer = "<footer>Footer de la página</footer>"
    return footer

def logo():
    logo = "<img src=\"./Imagenes/imagen.webp\">"
    return logo

def url():
    url = """<a href="index.html">Website</a>"""
    return url

def error():
	print('error')

elementosDisponibles = {
	0: boton,
    1: formulario,
    2: menu,
    3: etiqueta,
    4: radioButton,
    5: checkbutton,
    6: paginacion,
    7: desplegable,
    8: icono,
    9: lista,
    10: imagen,
    11: texto,
    12: video,
    13: footer,
    14: logo,
    15: url
}

#////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

url = sys.argv[1]

try:
    archivo_labels = open(url, 'rt')
    archivo_HTML = open('web.html', 'w')
    archivo_TXT = open('web.txt', 'w')
    codigo = """<!DOCTYPE html>
        <html lang="es">
        <head>
        <meta charset="utf-8">
        <title>HTML PAGE</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="style.css">
        </head>
        """

        # Leer líneas del fichero de labels y guardar los elementos en un array

    elementos = []
    while(True):
        linea = archivo_labels.readline()
        array = linea.split(" ")
        if len(array) > 1:
            array[0] = int(array[0])
            array[1] = float(array[1])
            array[2] = float(array[2])
            array[3] = float(array[3])
            array[4] = array[4].replace('\n','')
            array[4] = float(array[4])
                
            elementos.append(array)
            
        if not linea:
            break
    # Formmato de los elementos:

    # array[0] = Elemento
    # array[1] = centro eje X
    # array[2] = centro eje Y
    # array[3] = horizontal
    # array[4] = vertical
        

    # Ordenar elementos en el eje Y
    from operator import itemgetter

    elementos = sorted(elementos, key=itemgetter(2))

    # Ordenar elementos en el eje X

    filas = 0
    primera = True
    elementosOrdenados = []
    aux = []
    filaNueva = False

    for e in elementos:
        arriba = e[2] - (e[4]/2)
        abajo = e[2] + (e[4]/2)
        izq = e[1] - (e[3]/2)
        der = e[1] + (e[3]/2)
        media = e[2]
        mediaH = e[1]

        if(primera == True):
            elementosOrdenados.append(e)
            primera = False
        elif(media >= (aux[2] - (aux[4]/2))):
            if(media <= (aux[2] + (aux[4]/2))):
                if(len(elementosOrdenados[filas]) == 0):
                    elementosOrdenados.append(e)
                    filaNueva = True
                else:
                    eFinal = e
                    if(filaNueva == True):
                        for o in reversed(elementosOrdenados[filas]):
                            eFinal = [o, eFinal]
                    else:
                        eFinal = [elementosOrdenados[filas], eFinal]
                    filaNueva = False 
                    elementosOrdenados[filas] = eFinal
            else:
                filas = filas + 1
                elementosOrdenados.append(e)
        else:
            filas = filas + 1
            elementosOrdenados.append(e)
        aux = e

    # Leer e imprimir elementos

    for e in elementosOrdenados:
        codigo = codigo + """<div class="contenedor">"""

        if(len(e) > 1):
            isInt = False
            elemento = e[0]
            ele = ""
            try:
                isInt = int(elemento) == elemento
                ele = elemento
                if isInt == True and ele != None:
                    codigoResult = elementosDisponibles.get(ele, error)()
                    codigo = codigo + codigoResult
            except:
                try:
                    # Ordenar en eje X los elementos de una fila
                    e = sorted(e, key=itemgetter(1))
                except:
                    e = e

                for a in e:
                    try:
                        a = sorted(a, key=itemgetter(1))
                    except:
                        a = a
                    ele = a[0]

                    try:
                        isInt = int(ele) == ele
                        if isInt == True and ele != None:
                            codigoResult = elementosDisponibles.get(ele, error)()
                            codigo = codigo + codigoResult
                    except:
                        for b in a:
                            ele = b[0]

                            try:
                                isInt = int(ele) == ele
                                if isInt == True and ele != None:
                                    codigoResult = elementosDisponibles.get(ele, error)()
                                    codigo = codigo + codigoResult
                            except:
                                for c in b:
                                    ele = c[0]

                                    try:
                                        isInt = int(ele) == ele
                                        if isInt == True and ele != None:
                                            codigoResult = elementosDisponibles.get(ele, error)()
                                            codigo = codigo + codigoResult
                                    except:
                                        ele = ele[0]

                                        try:
                                            isInt = int(ele) == ele
                                            if isInt == True and ele != None:
                                                codigoResult = elementosDisponibles.get(ele, error)()
                                                codigo = codigo + codigoResult
                                        except:
                                            print(ele)
                                            print("Fallo")

        codigo = codigo + """</div>"""
        
    codigo = codigo + """</body>
        </html>
        """
    archivo_HTML.write(codigo)
    archivo_HTML.close()
    archivo_TXT.write(codigo)
    archivo_TXT.close()
    archivo_labels.close()

    # webbrowser.open_new_tab('web.html')
except:
    print("Error - Ha ocurrido un error")
