from flask import Flask, render_template


app = Flask(__name__)

headers = ('name', 'city', 'cost')
data = (('gazi', 'gaziantep', '40k'),
        ('mine', 'gaziant', '30k'),
        ('lod', 'gazntep', '40k'))

@app.route('/')
def table():
    return render_template('table.html', headers=headers, data=data)