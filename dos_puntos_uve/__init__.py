from flask import Flask, render_template
app = Flask(__name__)

with app.app_context():
    from . import db
    db.init_app(app)

@app.route("/")
def hola():
    return 'Hello World'

@app.route("/chau")
def chau():
    return 'Chau'

@app.route("/generos")
def generos():
    consulta = """
        SELECT name FROM genres
        ORDER BY name;
    """
    con = db.get_db()
    res = con.execute(consulta)
    lista_generos = res.fetchall()
    pagina = render_template('generos.html',
                             generos=lista_generos)
    return pagina