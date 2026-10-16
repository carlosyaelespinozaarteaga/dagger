import sqlite3
import os

# 1. CREAR LA BASE DE DATOS
def crear_bd():
    os.makedirs("database", exist_ok=True)

    conexion = sqlite3.connect("database/alumnos.db")
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS empleados (
            curp TEXT PRIMARY KEY,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            calle TEXT,
            colonia TEXT,
            telefono TEXT
        )
    """)

    conexion.commit()
    conexion.close()

    print("Base de datos creada correctamente")


# 2. DAR DE ALTA A LOS EMPLEADOS
def alta_empleado():
    conexion = sqlite3.connect("database/alumnos.db")
    cursor = conexion.cursor()

    print("\n=== REGISTRO DE EMPLEADO ===")

    curp = input("CURP: ").strip()
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()
    calle = input("Calle: ").strip()
    colonia = input("Colonia: ").strip()
    telefono = input("Telefono: ").strip()

    if not curp or not nombre or not apellido:
        print("Error: CURP, nombre y apellido son obligatorios.")
        conexion.close()
        return

    try:
        cursor.execute("""
            INSERT INTO empleados
            (curp, nombre, apellido, calle, colonia, telefono)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (curp, nombre, apellido, calle, colonia, telefono))

        conexion.commit()
        print("Empleado registrado correctamente")

    except sqlite3.IntegrityError:
        print("Error: esa CURP ya esta registrada.")

    except sqlite3.Error as error:
        print("Error al registrar:", error)

    finally:
        conexion.close()


# 3. PROGRAMA PRINCIPAL
if __name__ == "__main__":
    crear_bd()
    alta_empleado()