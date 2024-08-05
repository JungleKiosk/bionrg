from flask import Flask, render_template, request
import pandas as pd
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Ottieni i dati dal form
        capacity = int(request.form['capacity'])
        livestock = int(request.form['livestock'])
        area = float(request.form['area'])
        crop_type = float(request.form['crop_type'])
        c_ch4 = float(request.form['c_ch4'])
        mcg = float(request.form['mcg'])
        
        # Calcoli con pandas e numpy
        P = 1000  # Potenza in kW per 1 MW
        E_el = P * 24  # Energia elettrica giornaliera in kWh

        # Esempio di calcoli aggiuntivi (sostituisci con i tuoi calcoli specifici)
        rendimento = np.random.rand()  # Questo è solo un esempio
        dati = {
            'capacity': capacity,
            'livestock': livestock,
            'area': area,
            'crop_type': crop_type,
            'c_ch4': c_ch4,
            'mcg': mcg,
            'E_el': E_el,
            'rendimento': rendimento
        }
        df = pd.DataFrame([dati])

        # Passa i risultati al template
        return render_template('result.html', tables=[df.to_html(classes='data', header="true")], E_el=E_el)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)