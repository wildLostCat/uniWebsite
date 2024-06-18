from flask import Flask, render_template


app = Flask(__name__)

headers = ('name', 'city', 'cost', 'link')

data = ((('gazi', 'gaziantep', '40k'), 'google.com'),
        (('mine', 'gaziant', '30k'), 'youtube.com'),
        (('lod', 'gazntep', '40k'), 'google.com'))


@app.route('/')
def table():
    return render_template('table.html', headers=headers, data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

