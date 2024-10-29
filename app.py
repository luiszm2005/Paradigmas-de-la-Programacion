from flask import Flask, render_template, request, redirect, url_for
import os
import database as db

template_dir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(template_dir, 'src', 'templates')

app = Flask(__name__, template_folder=template_dir)

# Rutas de aplicación
@app.route('/')
def home():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM alumnos")
    myresult = cursor.fetchall()
    
    # Convertir datos en diccionario
    insertObjet = []
    columNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObjet.append(dict(zip(columNames, record)))
    cursor.close()

    return render_template('index.html', data=insertObjet)

# Ruta para guardar alumnos en la base de datos
@app.route('/alumno', methods=['POST'])
def addAlumno():
    # Obtener datos del formulario
    nombre = request.form['nombre']
    edad = request.form['edad']
    direccion = request.form['direccion']
    
    if nombre and edad and direccion:
        # Guardar datos en la base de datos
        cursor = db.database.cursor()
        sql = "INSERT INTO alumnos (nombre, edad, direccion) VALUES (%s, %s, %s)"
        data = (nombre, edad, direccion)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

# Ruta para eliminar alumnos
@app.route('/delete/<int:id>')
def delete(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM alumnos WHERE alumno_ID = %s"
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('home'))

# Ruta para editar alumnos
@app.route('/edit/<int:id>', methods=['POST'])
def edit(id):
    nombre = request.form['nombre']
    edad = request.form['edad']
    direccion = request.form['direccion']
    
    if nombre and edad and direccion:
        # Actualizar datos en la base de datos
        cursor = db.database.cursor()
        sql = "UPDATE alumnos SET nombre=%s, edad=%s, direccion=%s WHERE alumno_ID=%s"
        data = (nombre, edad, direccion, id)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
    