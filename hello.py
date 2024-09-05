from flask import Flask, jsonify, request

# Tipos de Metodos 
# GET -> se utiliza para recuperar informacion del servidor
# POST -> Se utiliza para enviar datos al servidor para su procesamiento
# DELETE -> Se utiliza para eliminar 1 o mas recursos en el servidor o base de datos
# PUT -> Se utiliza para actualizar un recurso en el servidor 
# PATCH -> Se utiliza para actualizar parcialmente un recurso en el servidor

''' Librerias necesarias para contactar flask con nuestra base de datos'''
'''Flask-SQLAlchemy - es la expresion que facilita el uso de SQLAlchemy con Flask'''
'''psycopg2 - es el adaptador de PostgreSQL para python''' 

app = Flask(__name__)

# Para correr la aplicacion es con 'flask --app hello run'

students = [
    {
        'name' : 'Gustavo',
        'age' : 38,
        'major' : 'computer science'
    },
    
    {
        'name' : 'Hiram',
        'age' : 22,
        'major' : 'computer science'
    },
    
    {
        'name' : 'Keishmer',
        'age' : 30,
        'major' : 'computer science'
    }
    
    
]

@app.route('/')
def hello_world():
    return 'Hello, Wordl!!!!!!!!'

@app.route('/kmg', methods=['GET', 'POST'])
def Hello_KMG():
    return '<h1> Hello, KMG </h1>'

# Ruta para obtener estudiantes 
@app.route('/students', methods=['GET'])
def students_get():
    return jsonify (students)

@app.route('/create-student', methods=['POST'])
def create_student():
    data = request.json
    students.append(data)
    return jsonify ({'message': 'Estudiante creado correctamente', 'data' : data})

#Ruta para borrar todos los estudiantes
@app.route('/delete-students', methods=["DELETE"])
def delete_all_students():
    students.clear()
    return jsonify({'message': 'Estudiantes borrados correctamente'})


