from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home/home.html')

@app.route('/dieta/<dieta_name>')
def dieta(dieta_name):
    dieta_name = dieta_name.upper()  # Converte il nome della dieta in maiuscolo
    return render_template('diets/diet.html', dieta=f'Dieta {dieta_name}')

if __name__ == '__main__':
    app.run(debug=True)
