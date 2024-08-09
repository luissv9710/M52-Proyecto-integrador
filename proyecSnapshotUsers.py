import mysql.connector
import pandas as pd
from mysql.connector import Error

def connect_to_mysql(host, user, password, database):
    try:
        connection = mysql.connector.connect(
            host='195.179.238.58',
            user='u927419088_admin',
            password='#Admin12345#',
            database='u927419088_testing_sql'
        )

        if connection.is_connected():
            print("Conexión exitosa a la base de datos")
            return connection

    except Error as e:
        print(f"Error al conectar a MySQL: {e}")
        return None

def fetch_data_to_dataframe(connection, query):
    try:
        # Ejecutar la consulta y obtener los datos en un DataFrame
        df = pd.read_sql(query, connection)
        return df
    except Error as e:
        print(f"Error al realizar la consulta: {e}")
        return None

def export_dataframe_to_excel(df, file_name):
    try:
        # Exportar el DataFrame a un archivo Excel
        df.to_excel(file_name, index=False)
        print(f"Datos exportados exitosamente a {file_name}")
    except Exception as e:
        print(f"Error al exportar a Excel: {e}")

def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print("Conexión a MySQL cerrada.")


# Ejemplo de uso:
host = '195.179.238.58',
user = 'u927419088_admin',
password = '#Admin12345#',
database = 'u927419088_testing_sql'

# Conectar a la base de datos
connection = connect_to_mysql(host, user, password, database)

if connection:
    # Definir la consulta SQL
    query = "SELECT * FROM datos_usuario"

    # Obtener los datos en un DataFrame
    df = fetch_data_to_dataframe(connection, query)

    if df is not None:
        # Exportar el DataFrame a un archivo Excel
        export_dataframe_to_excel(df, "datos_usuario.xlsx")
        csv_filename = "datos_usuario.csv"
        df.to_csv(csv_filename, index=False)

    # Cerrar la conexión a la base de datos
    close_connection(connection)

