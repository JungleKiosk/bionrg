from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home/home.html')

@app.route('/dieta/<dieta_name>', methods=['GET', 'POST'])
def dieta(dieta_name):
    dieta_name = dieta_name.upper()

    diete = {
        'A': {'liquame': (5, 15), 'insilato': (75, 90), 'siero': (5, 10)},
        'B': {'letame': (5, 25), 'insilato': (55, 75), 'scarti': (10, 35)},
        'C': {'liquame': (15, 25), 'insilato': (30, 65), 'bucce': (10, 35)},
        'D': {'letame': (25, 50), 'insilato': (5, 50), 'sanse': (10, 35)},
        'E': {'liquame': (10, 60), 'insilato': (5, 50), 'scarti': (10, 35)}
    }

    if request.method == 'POST':
        ingredienti = diete[dieta_name]
        percentuali = {}
        for ingrediente in ingredienti:
            percentuali[ingrediente] = float(request.form[ingrediente])
        
        return render_template('diets/diet.html', dieta=f'Dieta {dieta_name}', ingredienti=ingredienti, percentuali=percentuali)

    return render_template('diets/diet.html', dieta=f'Dieta {dieta_name}', ingredienti=diete[dieta_name])

if __name__ == '__main__':
    app.run(debug=True)
