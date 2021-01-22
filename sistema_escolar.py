import sqlite3

DB_PATH = "base_de_datos.db"

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

#---------------------------------------------------------------------------------------------------------------------#
#MANAGERS DE LAS DIFERENTES TABLAS DE DATOS

class ManagerCurso:

    def __init__(self, database=None):
        if not database:
            database = ':memory:'
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()

    def Insert(self, obj):
        
        self.cursor.execute("INSERT INTO Cursos VALUES ('{}', '{}', '{}', '{}', '{}')".format(obj.ID, obj.curso, obj.dia, obj.hora_entrada, obj.hora_salida))
        self.conn.commit()

    def Get(self):
        
        self.cursor.execute("SELECT * FROM Cursos")
        items = self.cursor.fetchall()
        if not items:
            print("No hay datos agregados")
        for item in items:
            print(item)

    def Search(self):

        sea_curso = input("Nombre del curso a buscar: ")
        self.cursor.execute("SELECT * FROM Cursos WHERE curso= ?", (sea_curso,))
        print(self.cursor.fetchall())

    def Update(self):

        curso = input("Indique el nuevo nombre del curso: ")
        ID = input("Indique el ID del curso a modificar: ")
        self.cursor.execute("UPDATE Cursos SET curso = :curso WHERE curso_ID = :curso_ID", {"curso": curso, "curso_ID": ID})
        self.conn.commit()
        

    def Delete(self, ID):
        
        self.cursor.execute("DELETE FROM Cursos WHERE curso_ID = '{}'".format(ID))
        self.conn.commit()

class ManagerProfe:

    def __init__(self, database=None):
        if not database:
            database = ':memory:'
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()

    def Insert(self, obj):
        
        self.cursor.execute("INSERT INTO Profe VALUES ('{}', '{}', '{}', '{}')".format(obj.curso_ID, obj.profe_ID, obj.nombre, obj.apellido))
        self.conn.commit()

    def Get(self):
        
        self.cursor.execute("SELECT profe_ID, Nombre, Apellido FROM Profe")
        items = self.cursor.fetchall()
        if not items:
            print("No hay datos agregados")
        for item in items:
            print(item)

    def Get_Busquedas(self):

        list_curso = input("Indique el codigo del curso: ")
        self.cursor.execute("""SELECT curso, dia, hora_entrada, hora_salida, profe_ID, Nombre, Apellido FROM
                            Cursos C LEFT JOIN Profe P ON C.curso_ID = P.curso_ID WHERE C.curso_ID = ?""", (list_curso,))
        items = self.cursor.fetchall()
        if not items:
            print("No hay datos agregados")
        for item in items:
            print(item)

    def Search(self):

        sea_profe = input("Apellido del profesor a buscar: ")
        self.cursor.execute("SELECT * FROM Profe WHERE apellido= ?", (sea_profe,))
        print(self.cursor.fetchall())

    def Update(self):

        nombre = input("Indique el nombre del nuevo profesor: ")
        apellido = input("Indique el apellido del nuevo profesor : ")
        ID = input("Indique el ID del profesor a modificar: ")
        self.cursor.execute("UPDATE Profe SET nombre = :nombre, apellido = :apellido WHERE profe_ID = :profe_ID",
                            {"nombre": nombre, "apellido": apellido, "profe_ID": ID})
        self.conn.commit()
        

    def Delete(self, profe_ID):
        
        self.cursor.execute("DELETE FROM Profe WHERE profe_ID = '{}'".format(profe_ID))
        self.conn.commit()

class ManagerAlumni:

    def __init__(self, database=None):
        if not database:
            database = ':memory:'
        self.conn = sqlite3.connect(database)
        self.cursor = self.conn.cursor()

    def Insert(self, obj):
        
        self.cursor.execute("INSERT INTO Alumni VALUES ('{}', '{}', '{}', '{}')".format(obj.profe_ID, obj.alumni_ID, obj.nombre, obj.apellido))
        self.conn.commit()

    def Get(self):
        
        self.cursor.execute("SELECT alumni_ID, Nombre, Apellido FROM Alumni")
        items = self.cursor.fetchall()
        if not items:
            print("No hay datos agregados")
        for item in items:
            print(item)

    def Get_Busquedas_Alumnni(self):

        list_curso_alumni = input("Indique el codigo del profesor: ")
        self.cursor.execute("""SELECT Nombre, Apellido, alumni_ID, Nombre_Alumni, Apellido_Alumni FROM
                            Profe P LEFT JOIN Alumni A ON P.profe_ID = A.profe_ID WHERE P.profe_ID = ?""", (list_curso_alumni,))
        items = self.cursor.fetchall()
        if not items:
            print("No hay datos agregados")
        for item in items:
            print(item)

    def Search(self):

        sea_alumni = input("Apellido del alumni a buscar: ")
        self.cursor.execute("SELECT * FROM Alumni WHERE apellido= ?", (sea_alumni,))
        print(self.cursor.fetchall())

    def Update(self):

        nombre = input("Indique el nombre del nuevo alumno: ")
        apellido = input("Indique el apellido del nuevo alumno: ")
        ID = input("Indique el ID del alumno a modificar: ")
        self.cursor.execute("UPDATE Alumni SET nombre = :nombre, apellido = :apellido WHERE alumni_ID = :alumni_ID",
                            {"nombre": nombre, "apellido": apellido, "alumni_ID": ID})
        self.conn.commit()
        

    def Delete(self, alumni_ID):
        
        self.cursor.execute("DELETE FROM Alumni WHERE alumni_ID = '{}'".format(alumni_ID))
        self.conn.commit()


#-----------------------------------------------------------------------------------------------------------------#
#CLASES DE LAS TABLAS

class Cursos(object):
    objects = ManagerCurso(DB_PATH)

    def __init__(self, ID, curso, dia, hora_entrada, hora_salida):
        self.ID = ID
        self.curso = curso
        self.dia = dia
        self.hora_entrada = hora_entrada
        self.hora_salida = hora_salida

    def __repr__(self):
        return u"{} - {}".format(self.ID, self.curso)

class Profe(object):
    objects = ManagerProfe(DB_PATH)

    def __init__(self, curso_ID, profe_ID, nombre, apellido):
        self.curso_ID = curso_ID
        self.profe_ID = profe_ID
        self.nombre = nombre
        self.apellido = apellido

class Alumni(object):
    objects = ManagerAlumni(DB_PATH)

    def __init__(self, profe_ID, alumni_ID, nombre, apellido):
        self.profe_ID = profe_ID
        self.alumni_ID = alumni_ID
        self.nombre = nombre
        self.apellido = apellido

#------------------------------------------------------------------------------------------------#
#MANAGERS DE LOS MENUS

def menu():

    opcion = 0
    salir = "5"

    while opcion != salir:
        print("--------------------")
        print("Menu principal")
        print("--------------------")
        print("1.- Cursos")
        print("2.- Profesores")
        print("3.- Alumnos")
        print("4.- Busquedas generales")
        print("5.- Salir")
        print("--------------------")
        opcion = input("Indique la accion a efectuar: ")
        print("--------------------")

        if opcion == "1":
            menu_cursos()
        elif opcion == "2":
            menu_profe()
        elif opcion == "3":
            menu_alumnos()
        elif opcion == "4":
            menu_busquedas()
        elif opcion == "5":
            print("Muchas gracias")
            break

def menu_cursos():

    opcion = 0
    salir = "6"

    while opcion != salir:
        print("--------------------")
        print("Menu Cursos")
        print("--------------------")
        print("1.- Lista de cursos agregados")
        print("2.- Agregar nuevo curso")
        print("3.- Borrar un curso")
        print("4.- Buscar un curso")
        print("5.- Actualizar el nombre de un curso por ID: ")
        print("6.- Volver al menu principal")
        print("--------------------")
        opcion = input("Indique la accion a efectuar: ")
        print("--------------------")

        if opcion == "1":
            print("Id --- Nombre --- Dia --- Entrada --- Salida")
            print(Cursos.objects.Get())
        elif opcion == "2":
            curso_agre = Cursos(ID = input("ID del curso: "), curso = input("Nombre del curso a agregar: "), dia = input("Indique el dia de cursada: ", ),
                                hora_entrada = input("Indique la hora de inicio: "), hora_salida = input("Indique hora de salida: "))
            Cursos.objects.Insert(curso_agre)
        elif opcion == "3":
            Cursos.objects.Delete(int(input("Indique el ID del curso a borrar: ")))
        elif opcion == "4":
            Cursos.objects.Search()
        elif opcion == "5":
            Cursos.objects.Update()
        elif opcion == "6":
            menu()

def menu_profe():

    opcion = 0
    salir = "6"

    while opcion != salir:
        print("--------------------")
        print("Menu Profesores")
        print("--------------------")
        print("1.- Lista de profesores agregados")
        print("2.- Agregar nuevo profesor")
        print("3.- Borrar a un profesor")
        print("4.- Buscar a un profesor")
        print("5.- Actualizar el nombre de un profesor por ID: ")
        print("6.- Volver al menu principal")
        print("--------------------")
        opcion = input("Indique la accion a efectuar: ")
        print("--------------------")

        if opcion == "1":
            print("Id profesor - Nombre - Apellido")
            print(Profe.objects.Get())
        elif opcion == "2":
            profe_agre = Profe(curso_ID = input("ID del curso: "), profe_ID = input("ID del profesor: "), nombre = input("Nombre: "),
                               apellido = input("Apellido: "))
            Profe.objects.Insert(profe_agre)
        elif opcion == "3":
            Profe.objects.Delete(input("Indique el ID del profesor a borrar: "))
        elif opcion == "4":
            Profe.objects.Search()
        elif opcion == "5":
            Profe.objects.Update()
        elif opcion == "6":
            menu()


def menu_alumnos():

    opcion = 0
    salir = "6"

    while opcion != salir:
        print("--------------------")
        print("Menu Alumnos")
        print("--------------------")
        print("1.- Lista de alumnos agregados")
        print("2.- Agregar nuevo alumno")
        print("3.- Borrar a un alumno")
        print("4.- Buscar a un alumno")
        print("5.- Actualizar el nombre de un alumno por ID: ")
        print("6.- Volver al menu principal")
        print("--------------------")
        opcion = input("Indique la accion a efectuar: ")
        print("--------------------")

        if opcion == "1":
            print("ID Alumno - Nombre - Apellido")
            print(Alumni.objects.Get())
        elif opcion == "2":
            alumni_agre = Alumni(profe_ID = input("ID del profesor: "), alumni_ID = input("ID del alumno: "), nombre = input("Nombre: "),
                                 apellido = input("Apellido: "))
            Alumni.objects.Insert(alumni_agre)
        elif opcion == "3":
            Alumni.objects.Delete(input("Indique el ID del alumno a borrar: "))
        elif opcion == "4":
            Alumni.objects.Search()
        elif opcion == "5":
            Alumni.objects.Update()
        elif opcion == "6":
            menu()

def menu_busquedas():

    opcion = 0
    salir = "3"

    while opcion != salir:
        print("--------------------")
        print("Busquedas Generales")
        print("--------------------")
        print("1.- Ver lista de profesores asignados segun el ID del curso")
        print("2.- Ver lista de alumnos asignados segun el ID del profesor")
        print("3.- Volver al menu principal")
        print("--------------------")
        opcion = input("Indique la accion a efectuar: ")
        print("--------------------")

        if opcion == "1":
            Profe.objects.Get_Busquedas()
        elif opcion == "2":
            Alumni.objects.Get_Busquedas_Alumnni()
        elif opcion == "3":
            menu()

print("""Bienvenido al sistema de asignacion de cursos, profesores y alumnos del instituto.
Usar IDs correlativos para asignar cursos, profesores y alumnos y poder llevar un mejor control de las busquedas.
Ejemplo de uso de IDs:
Codigo de curso 1001
Codigo de profesor 1001-01
Codigo de alumno A1001-01""")


menu()
