from flask import Flask,render_template, request
from config import *

con_bd = EstablecerConexion()
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method =='POST':
        #porceso
        return "oks"
    else:
        return render_template('login.html')
    return render_template('login.html')


def crearTablaPersonas():
    cursor = con_bd.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios(
            id serial NOT NULL,
            email character varying(50),
            password character varying(102),
            nombres character varying(60),
            CONSTRAINT pk_id_personas PRIMARY KEY (id)
        );
    """)
    con_bd.commit()




if __name__ == '__main__':
    crearTablaPersonas()
    app.run(debug=True, port=5555)