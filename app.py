from flask import Flask, render_template, request

app = Flask(__name__)

# Specifiche di progetto fisse
P = 1000  # Potenza in kW per 1 MW
t = 8040  # ore annue
n = 0.45  # Rendimento elettrico
H = 10  # Potere calorifero (kWh/Nm³)
E_el = P * 24  # Energia elettrica giornaliera in kWh

# Potenziale metanigeno (valori presi dai file Excel)
pot_pg_animali = {
    'liquame_bovino': 30,
    'letame_bovino': 70,
    'liquame_suino': 20,
    'letame_suino': 90,
}

pot_ch4_animali = {
    'liquame_bovino': 0.55,
    'letame_bovino': 0.55,
    'liquame_suino': 0.62,
    'letame_suino': 0.62,
}

pot_pg_colture = {
    'insilato_mais': 200,
    'insilato_sorgo': 150,
    'insilato_triticale': 185,
}

pot_ch4_colture = {
    'insilato_mais': 0.53,
    'insilato_sorgo': 0.52,
    'insilato_triticale': 0.53,
}

pot_pg_scarti = {
    'bucce_pomodoro': 100,
    'siero_latte': 30,
    'scarti_frutta': 130,
    'sansa_olive': 200,
    'scarti_patata': 120,
}

pot_ch4_scarti = {
    'bucce_pomodoro': 55,
    'siero_latte': 60,
    'scarti_frutta': 55,
    'sansa_olive': 55,
    'scarti_patata': 57,
}

# Resa colturale (valori presi dai file Excel)
resa_r_colture = {
    'insilato_mais': 40,
    'insilato_sorgo': 20,
    'insilato_triticale': 35,
}

resa_p_colture = {
    'insilato_mais': 0.63,
    'insilato_sorgo': 0.63,
    'insilato_triticale': 0.63,
}

# Produzione reflui (valori presi dai file Excel)
prod_pm_reflui = {
    'liquame_bovino': 21,
    'letame_bovino': 33,
    'liquame_suino': 28,
    'letame_suino': 55,
}

prod_mc_reflui = {
    'liquame_bovino': 0.48,
    'letame_bovino': 0.48,
    'liquame_suino': 0.10,
    'letame_suino': 0.10,
}

prod_p_reflui = {
    'liquame_bovino': 1.00,
    'letame_bovino': 0.35,
    'liquame_suino': 1.00,
    'letame_suino': 0.35,
}


@app.route('/')
def home():
    return render_template('home/home.html')

@app.route('/dieta/<dieta_name>', methods=['GET', 'POST'])
def dieta(dieta_name):
    dieta_name = dieta_name.upper()  # Converte il nome della dieta in maiuscolo

    # Limiti per gli ingredienti di ogni dieta
    diete = {
        'A': {'liquame_bovino': (5, 15), 'insilato_mais': (75, 90), 'siero_latte': (5, 10)},
        'B': {'letame_bovino': (5, 25), 'insilato_mais': (55, 75), 'scarti_patata': (10, 35)},
        'C': {'liquame_suino': (15, 25), 'insilato_mais': (30, 65), 'bucce_pomodoro': (10, 35)},
        'D': {'letame_bovino': (25, 50), 'insilato_mais': (5, 50), 'sanse_olive': (10, 35)},
        'E': {'liquame_suino': (10, 60), 'insilato_triticale': (5, 50), 'scarti_frutta': (10, 35)}
    }

    if request.method == 'POST':
        # Ottieni le percentuali degli ingredienti dal form
        ingredienti = diete[dieta_name]
        percentuali = {}
        for ingrediente in ingredienti:
            percentuali[ingrediente] = float(request.form[ingrediente])

        # Calcolo del metano totale necessario
        M_ch4_tot = E_el / (H * n)  # Quantità di metano totale necessario (Nm³)

        if dieta_name == 'E':
            # Calcolo del biogas totale necessario per dieta E
            C_CH4_LS = pot_ch4_animali['liquame_suino']
            C_CH4_IT = pot_ch4_colture['insilato_triticale']
            C_CH4_SF = pot_ch4_scarti['scarti_frutta']

            phi_LS = percentuali['liquame_suino'] / 100
            phi_IT = percentuali['insilato_triticale'] / 100
            phi_SF = percentuali['scarti_frutta'] / 100

            M_B_tot = M_ch4_tot / (phi_LS * pot_pg_animali['liquame_suino'] * C_CH4_LS +
                                   phi_IT * pot_pg_colture['insilato_triticale'] * C_CH4_IT +
                                   phi_SF * pot_pg_scarti['scarti_frutta'] * C_CH4_SF)

            # Massa di biogas prodotto
            M_B_IT = phi_IT * M_B_tot
            M_B_LS = phi_LS * M_B_tot

            # Numero di giorni all'anno in cui l'impianto funziona
            N = t / 24  # giorni/anno

            # Superficie da destinare alla coltura energetica
            resa_IT = resa_r_colture['insilato_triticale']
            S_IT = (M_B_IT * N) / resa_IT

            # Numero di capi necessari per la produzione di letame suino
            p_m = prod_pm_reflui['liquame_suino']
            rho = 0.35  # Densità (ton/m³)
            m_c = 0.1  # Quantità di refluo per capo (ton/capo)
            A_capi = (M_B_LS * N) / (p_m * rho * m_c)

            return render_template('diets/diet.html', dieta=f'Dieta {dieta_name}', ingredienti=ingredienti, percentuali=percentuali, E_el=E_el, M_ch4_tot=M_ch4_tot, M_B_tot=M_B_tot, M_B_IT=M_B_IT, M_B_LS=M_B_LS, S_IT=S_IT, A_capi=A_capi)

    return render_template('diets/diet.html', dieta=f'Dieta {dieta_name}', ingredienti=diete[dieta_name])

if __name__ == '__main__':
    app.run(debug=True)
