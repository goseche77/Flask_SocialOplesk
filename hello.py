from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

# Tipos de Metodos 
# GET -> se utiliza para recuperar informacion del servidor
# POST -> Se utiliza para enviar datos al servidor para su procesamiento
# DELETE -> Se utiliza para eliminar 1 o mas recursos en el servidor o base de datos
# PUT -> Se utiliza para actualizar un recurso en el servidor 
# PATCH -> Se utiliza para actualizar parcialmente un recurso en el servidor

''' Librerias necesarias para contactar flask con nuestra base de datos'''
'''Flask-SQLAlchemy - es la expresion que facilita el uso de SQLAlchemy con Flask'''
'''psycopg2 - es el adaptador de PostgreSQL para python''' 

''''Los curl tiene una peticion y el link  ejemplo "curl -X GET http://localhost:5000/students "'''
''''Los curl tiene una peticion y el link  ejemplo "curl -X GET http://localhost:5000/create-students "'''

## Para instalar la base de datos se coloca de la siguiente manera --> pip install Flask-SQLAlchemy psycopg2 ##

app = Flask(__name__)

# Para correr la aplicacion es con 'flask --app hello run'

## Estructura de la base de daros: motorbasededatos://usuario:contraseña@host:localhost:5432/nombre_base_de_datos' ##

# Configuracion de la base de datos #

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:posgre@localhost:5432/estudiantes_grupo_8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

## Definicion del modelo de estudiante ## modelo (es una tabla de base de datos) ##

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    major = db.Column(db.String(50), nullable=False)

def to_dict(self):
    return {
        'id' : self.id,
        'name' : self.name,
        'age' : self.age,
        'major' : self.major
    }
## Crear las tablas ##
with app.app_context():
    db.create_all()
    
    ## Verificar la conexion a la base de datos ##
    # try:
    #     #Realizamos una consulta simple
    #     db.session.execute(text('SELECT 1'))
    #     print("Conexion a la base de datos exitosa")
    # except Exception as e:
    #     print(f'Error al conectar a las base de datos: {e}')
    

# @app.route('/')
# def hello_world():
#     return 'Hello, Wordl!!!!!!!!'

# @app.route('/kmg', methods=['GET', 'POST'])
# def Hello_KMG():
#     return '<h1> Hello, KMG </h1>'

# # Ruta para obtener estudiantes 
@app.route('/students', methods=['GET'])
def students_get():
    students = Student.query.all()
    return jsonify ([student.to_dict() for student in students])

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student_by_id(student_id):
    student = Student.query.get(student_id)
    if student:
        return jsonify(student.to_dict())
    return jsonify({'message': 'El estudiante no ha sido encontrado'})


## Ruta para crear un estudiante ##
@app.route('/create-student', methods=['POST'])
def create_student():
    data = request.json
    new_student = Student(name = data['name'], age = data['age'], major = data['major'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify(
        {   
            'message': 'Estudiante creado correctamente',
            'data': new_student.to_dict()      
        })

# #Ruta para borrar todos los estudiantes
# @app.route('/delete-students', methods=["DELETE"])
# def delete_all_students():
#     students.clear()
#     return jsonify({'message': 'Estudiantes borrados correctamente'})


