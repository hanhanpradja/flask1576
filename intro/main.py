from flask import Flask
import random

app = Flask(__name__)

fakta = ['Kecanduan Shopping online dalam membuat uang habus',
         'Kecanduan game online dapat membuat waktu habis',
         'Kecanduan sosmed membuat hidupmu percuma']


@app.route('/')
def home():
    return '<h1>INI HALAMAN UTAMA</h1><a href="/random_facts">Klik untuk melihat fakta</a><br><a href="/hantu">Cerita hantu</a>'

@app.route("/random_facts")
def random_facts():
    return f"<p>Hello, World!</p><br><p>{random.choice(fakta)}</p><a href='/'>Back to Home</a>"


cerita_hantu = """




"""
@app.route('/hantu')
def hantu():
    return f"<p>{cerita_hantu}</p><a href='/'>Back to home</a>"

app.run(debug=True)