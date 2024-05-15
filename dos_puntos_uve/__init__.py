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

@app.route("/peliculas")
def peliculas():
    consulta = """
        SELECT title FROM film
        ORDER BY title;
    """
    con = db.get_db()
    res = con.execute(consulta)
    lista_peliculas = res.fetchall()
    pagina = render_template('film.html',
                             peliculas=lista_peliculas)
    return pagina

