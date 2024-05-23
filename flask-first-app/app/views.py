from flask import Flask, redirect, url_for, render_template
from markupsafe import escape

app = Flask(__name__)
app.counter = 0


@app.route("/")
@app.route("/index")
def index():
    movies = ['Terminator', 'Breaking Bad', 'Avatar', 'Pitbull']
    return render_template("index.html", name ='Edek', movies = movies)

@app.route("/articles")
def articles():
    posts = [
        {
            'author': {'nickname': 'John'},
            'title': 'Beautiful day in Poznan!',
            'body': 'Very random text about Poznan!'
        },
        {
            'author': {'nickname': 'Susan'},
            'title': 'The Avengers movie was so cool!',
            'body': 'Long random text about the movie!'
        },
        {
            'author': {'nickname': 'Róża '},
            'title': 'Peppopodobna świnka, apokalipsa zombie i selfie z Chopinem',
            'body': 'Od niechcenia przeglądam Facebooka, bez celu i chyba z nudów, bo przecież tam naprawdę jest istne śmieciowisko! Zatrzymuje mnie kilkuzdaniowy post (kto jeszcze pisze posty na Facebooku? – ona, znajoma ze szkoły), czytam (kto jeszcze czyta posty na Facebooku? – ja, znudzona, prokrastynująca ja). Jest coś o nieprzygotowaniu na lekcję, zbliżającym się egzaminie, ale ona nie ma nut, nie wie, co grać, a co gorsza – nie wie, jak grać. Struny nie stroją, a może to jednak smyczek? Wyrywa więc z fortepianu klawisz A i pociąga nim po strunach. Zadziała? Akompaniatorka (niewzruszona brakiem jednego klawisza) cierpliwie czeka, profesor, już mniej cierpliwie, ale wciąż – czeka. Gotowa? Gramy? Koniec snu, koniec posta, a pod nim mnóstwo komentarzy.!'
        },
        {
            'author': {'nickname': 'Susan'},
            'title': 'Przewodnik po telewizyjnych miasteczkach lat 90!',
            'body': 'Zapomnij o przewodnikach po Paryżu czy Rzymie – oto ekskluzywny przewodnik po najbardziej malowniczych i zagadkowych serialowych miasteczkach z lat dziewięćdziesiątych! Od zasypanego śniegiem Cicely po mroczne zakątki Twin Peaks – odkryj, gdzie tajemnice i humor mieszają się z kawą tak czarną, jak bezgwiezdna noc.!'
        }
    ]

    return render_template("articles.html", title="Awesome Blog", posts=posts)
@app.route('/<name>')
def welcome(name):
    return f'Hello {escape(name)}'

@app.route('/hello/<name>')
def welcome_name(name):
    return f'Hello {escape(name)}'


@app.route('/counter')
def log_counter():
    app.counter += 1
    return f'Counter is  {escape(app.counter)}'


@app.route('/anonim')
def anonim():
    return redirect(url_for("welcome", name='Guest'))



if __name__ == '__main__':
    app.run(debug=True)