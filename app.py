from flask import  Flask, render_template, request, redirect, url_for,session

app= Flask(__name__)
app.config['SECRET_KEY'] = 'nelro'

@app.route("/")
def index():
    return render_template("index.html")

#-------------------------------------------------------------------------------------
# Lista para almacenar los registros
registros_ins = []

# Inscripción en curso
@app.route('/inscripcion', methods=['GET', 'POST'])
def inscripcion():
    if request.method == 'POST':
        # Recibir los datos del formulario
        nombre = request.form['nombre']
        apellidos = request.form['apellidos']
        curso = request.form['curso']

         # Agregar los datos a la lista de registros
        registros_ins.append({'nombre': nombre, 'apellidos': apellidos, 'curso': curso})
       # Redirigir a la página de confirmación
        #return redirect(url_for('rec_dat_inscripcion'))
    
    return render_template('inscripcion.html')

#recivir los datos enviados de inscrpcion a recivir datos en otra pagina
@app.route('/rec_dat_inscripcion')
def rec_dat_inscripcion():
    # Pasar los registros a la página de confirmación
    return render_template('rec_dat_inscripcion.html', registros_ins=registros_ins)

#-----------------------------------------------------------------------------------
#crear una lsista para recivir datos
lista_registros_usuarios=[]
# Registro de usuario
@app.route('/registro_usuario', methods=['GET', 'POST'])
def registro_usuario():

    if request.method == 'POST':
        #recivimos datos del fromulario reg. usuario
        nombre =  request.form['nombre']
        apellidos =  request.form['apellidos']
        email =  request.form['email']
        contraseña =  request.form['contraseña']
        # Agregar los datos a la lista de registros
        lista_registros_usuarios.append({'nombre': nombre, 'apellidos': apellidos, 'email': email,'contraseña':contraseña})

    return render_template('registro_usuario.html')

#para pdoer  ver los datos enviados a la lista

@app.route('/rec_dat_regUsuario')
def rec_dat_regUsuario():
    # Pasar los registros a la página de confirmación
    return render_template('rec_dat_regUsuario.html', lista_registros_usuarios=lista_registros_usuarios)

#-----------------------------------------------------------------------------

#generar una lista para poder alamcenar
lis_regProductos=[]
# Registro de productos
@app.route('/registro_productos',methods=['GET', 'POST'])
def registro_productos():
    
    if request.method == 'POST':
        # Recibir los datos del formulario
        producto = request.form['producto']
        categoria = request.form['categoria']
        existencia = request.form['existencia']
        precio = request.form['precio']
        

        # Agregar los datos a la lista de registros
        lis_regProductos.append({'producto': producto,'categoria':categoria,'existencia':existencia,'precio':precio})

    return render_template('registro_productos.html')

#para pdoer  ver los datos enviados a la lista registros de productos
@app.route('/rec_dat_regProductos')
def rec_dat_regProductos():
    # Pasar los registros a la página de confirmación
    return render_template('rec_dat_regProductos.html',lis_regProductos=lis_regProductos)

#----------------------------------------------------------------------------------------------
#generar una lista para poder alamcenar
lis_regLibros=[]
# Registro de libros
@app.route('/registro_libros', methods=['GET', 'POST'])
def registro_libros():
    #verificar si se mandaron datos
    if request.method == 'POST':
        # Recibiendo los datos del formulario
        titulo = request.form['titulo']
        autor = request.form['autor']
        resumen = request.form['resumen']
        medio = request.form['medio']
        
        # Agregar los datos a la lista de registros
        lis_regLibros.append({'titulo':titulo,'autor':autor,'resumen':resumen,  'medio':medio})

    return render_template('registro_libros.html')

#recivir datos del formulario enviado a la pagina  de registro de libros
@app.route('/rec_dat_regLibros')
def rec_dat_regLibros():
    # Pasar los registros a la página de confirmación
    return render_template('rec_dat_regLibros.html',lis_regLibros=lis_regLibros)


if  __name__ == '__main__':
    app.run(debug=True)

