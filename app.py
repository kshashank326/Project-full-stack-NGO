from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_USER'] = 'sql6501874'
app.config['MYSQL_PASSWORD'] = 'HlI4TISMfE'
app.config['MYSQL_HOST'] = 'http://sql6.freemysqlhosting.net/'
app.config['MYSQL_DB'] = 'sql6501874'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute(''' CREATE TABLE EXAMPLE (id integer, name varchar(20))''')
    return 'Done!'

if __name__ == "__main__":
    app.run(debug=True)