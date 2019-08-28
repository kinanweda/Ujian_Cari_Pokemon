from flask import Flask, render_template, jsonify, request, redirect
import requests

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/pokemon',methods = ['POST'])
def pokemon():
    request.method == 'POST'
    body = request.form
    pokemon = body['poke'].lower()
    url = 'https://pokeapi.co/api/v2/pokemon/{}'.format(pokemon)
    
    insert = requests.get(url)

    if insert.status_code == 200:
        json = insert.json()
        return render_template('hasil.html', insert1='{}'.format(json['name']),insert2='{}'.format(json['id']), insert3='{}'.format(json['sprites']['front_default']), insert4='{}'.format(json['height']),insert5='{}'.format(json['weight']))
    elif str(insert) == """<Response [404]>""":
        return render_template('error.html')
    
    return render_template('hasil.html')

if (__name__) == '__main__':
    app.run(
        debug=True,
        host='localhost',
        port=5000
        )