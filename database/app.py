from flask import Flask, request, jsonify
# import mysql.connector
from flask_mysqldb import MySQL
# from mysql.connector import Error

app = Flask(__name__)

# # Konfigurasi database
# db_config = {
#     'host': 'localhost:3306',
#     'database': 'cc_image',
#     'user': 'novin',
#     'password': 'novin'
# }

app.config['MYSQL_USER'] = 'novin'
app.config['MYSQL_PASSWORD'] = 'novin'
app.config['MYSQL_DB'] = 'cc_image'
app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

@app.route('/')
def endpoint():
    return "Hello world!"

# Endpoint untuk memasukkan data
@app.route('/insert', methods=['POST'])
def insert_data():
    try:
        # connection = mysql.connector.connect(**db_config)
        cursor = mysql.connection.cursor()
    # if connection.is_connected():
        # cursor = connection.cursor()

        # Ambil data dari form data
        id_ops = request.form.get('id_ops')
        name = request.form.get('name')
        file = request.form.get('name_file')
        pred = request.form.get('prediction')

        query = "INSERT INTO operation(id_ops, name, name_file, prediction ) VALUES (%s, %s, %s, %s)"
        values = (id_ops, name, file, pred)

        cursor.execute(query, values)
        mysql.connection.commit()
        response = jsonify('Data berhasil dimasukkan.')
        # response.status_code = 200
        return response
    except Exception as e:
        return jsonify(str(e)), 500
 

if __name__ == '__main__':
    app.run(debug=True)
