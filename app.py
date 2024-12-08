from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.method == 'POST':
        city1 = request.form.get('city1')
        city2 = request.form.get('city2')
        if city1 and city2:
            message = f'{city1} и {city2}'
        else:
            message = 'Пожалуйста, заполните оба поля'

    return render_template('index.html', message=message)



if __name__ == '__main__':
    app.run(debug=True)
