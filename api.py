from flask import Flask, render_template, request
import requests
app = Flask(__name__)


@app.route('/temperature', methods=['POST'])
def temperature():
    zipcode = request.form['zip']
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',us&appid=69b69eaa7e159d854dc861079adea11a')
    json_object = r.json()
    temp_k = float(json_object['main']['temp'])
    return render_template('temperature.html', temp = temp_k)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)