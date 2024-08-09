from flask import Flask, render_template, request
import param

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home/home.html')

@app.route('/specifiche')
def specifiche():
    return render_template('home/spec.html')


@app.route('/dieta/<dieta_name>', methods=['GET', 'POST'])
def dieta(dieta_name):
    dieta_name = dieta_name.upper()  # Converte il nome della dieta in maiuscolo

    # Limiti per gli ingredienti di ogni dieta
    diete = {
        'A': {'liquame_bovino': (5, 15), 'insilato_mais': (75, 90), 'siero_latte': (5, 10)},
        'B': {'letame_bovino': (5, 25), 'insilato_mais': (55, 75), 'scarti_patata': (10, 35)},
        'C': {'liquame_suino': (15, 25), 'insilato_mais': (30, 65), 'bucce_pomodoro': (10, 35)},
        'D': {'letame_bovino': (25, 50), 'insilato_sorgo': (5, 50), 'sansa_olive': (10, 35)},
        'E': {'letame_suino': (15, 60), 'insilato_triticale': (5, 50), 'scarti_frutta': (10, 35)}
    }

    input_values = {}
    if request.method == 'POST':
        # Ottieni le percentuali degli ingredienti dal form
        ingredienti = diete[dieta_name]
        percentuali = {}
        for ingrediente in ingredienti:
            percentuali[ingrediente] = float(request.form[ingrediente])  # Prendi i valori come percentuali
            input_values[ingrediente] = request.form[ingrediente]  # Salva il valore inserito dall'utente

        # Calcolo del metano totale necessario
        M_ch4_tot = param.E_el / (param.H * param.n)  # Quantità di metano totale necessario (Nm³)

        # Calcolo del biogas totale necessario per tutte le diete
        #----------------------
        #DIET A
        if dieta_name == 'A':
            C_CH4_LS = param.pot_ch4_animali['liquame_bovino']
            C_CH4_IT = param.pot_ch4_colture['insilato_mais']
            C_CH4_SF = param.pot_ch4_scarti['siero_latte']

            Pg_LS = param.pot_pg_animali['liquame_bovino']
            Pg_IT = param.pot_pg_colture['insilato_mais']
            Pg_SF = param.pot_pg_scarti['siero_latte']

            phi_LS = percentuali['liquame_bovino'] / 100
            phi_IT = percentuali['insilato_mais'] / 100
            phi_SF = percentuali['siero_latte'] / 100
            #diet A - check OK - ✅
        #----------------------
        #DIET B
        elif dieta_name == 'B':
            C_CH4_LS = param.pot_ch4_animali['letame_bovino']
            C_CH4_IT = param.pot_ch4_colture['insilato_mais']
            C_CH4_SF = param.pot_ch4_scarti['scarti_patata']

            Pg_LS = param.pot_pg_animali['letame_bovino']
            Pg_IT = param.pot_pg_colture['insilato_mais']
            Pg_SF = param.pot_pg_scarti['scarti_patata']

            phi_LS = percentuali['letame_bovino'] / 100
            phi_IT = percentuali['insilato_mais'] / 100
            phi_SF = percentuali['scarti_patata'] / 100
            #diet B - check OK - ✅
        #----------------------
        #DIET C
        elif dieta_name == 'C':
            C_CH4_LS = param.pot_ch4_animali['liquame_suino']
            C_CH4_IT = param.pot_ch4_colture['insilato_mais']
            C_CH4_SF = param.pot_ch4_scarti['bucce_pomodoro']

            Pg_LS = param.pot_pg_animali['liquame_suino']
            Pg_IT = param.pot_pg_colture['insilato_mais']
            Pg_SF = param.pot_pg_scarti['bucce_pomodoro']

            phi_LS = percentuali['liquame_suino'] / 100
            phi_IT = percentuali['insilato_mais'] / 100
            phi_SF = percentuali['bucce_pomodoro'] / 100
            #diet C - check OK - ✅
        #----------------------
        #DIET D
        elif dieta_name == 'D':
            C_CH4_LS = param.pot_ch4_animali['letame_bovino']
            C_CH4_IT = param.pot_ch4_colture['insilato_sorgo']
            C_CH4_SF = param.pot_ch4_scarti['sansa_olive']

            Pg_LS = param.pot_pg_animali['letame_bovino']
            Pg_IT = param.pot_pg_colture['insilato_sorgo']
            Pg_SF = param.pot_pg_scarti['sansa_olive']

            phi_LS = percentuali['letame_bovino'] / 100
            phi_IT = percentuali['insilato_mais'] / 100
            phi_SF = percentuali['sansa_olive'] / 100
            #diet D - check OK - ✅
        #----------------------
        #DIET E
        elif dieta_name == 'E':
            C_CH4_LS = param.pot_ch4_animali['letame_suino']
            C_CH4_IT = param.pot_ch4_colture['insilato_triticale']
            C_CH4_SF = param.pot_ch4_scarti['scarti_frutta']

            Pg_LS = param.pot_pg_animali['letame_suino']
            Pg_IT = param.pot_pg_colture['insilato_triticale']
            Pg_SF = param.pot_pg_scarti['scarti_frutta']

            phi_LS = percentuali['letame_suino'] / 100
            phi_IT = percentuali['insilato_triticale'] / 100
            phi_SF = percentuali['scarti_frutta'] / 100
            #diet E - check OK - ✅
        #----------------------
        # Calcolo della massa totale di biogas
        M_B_tot_numerator = M_ch4_tot
        M_B_tot_denominator = (phi_LS * Pg_LS * C_CH4_LS) + (phi_IT * Pg_IT * C_CH4_IT) + (phi_SF * Pg_SF * C_CH4_SF)
        M_B_tot = M_B_tot_numerator / M_B_tot_denominator

        # Massa di biogas prodotto
        M_B_IT = phi_IT * M_B_tot
        M_B_LS = phi_LS * M_B_tot

        # Numero di giorni all'anno in cui l'impianto funziona
        N = param.t / 24  # giorni/anno

        # Ottieni i parametri specifici della dieta dal file param.py
        diet_params = param.get_diet_params(dieta_name)

        # Superficie da destinare alla coltura energetica
        resa_IT = diet_params['resa_IT']
        S_IT = (M_B_IT * N) / resa_IT

        # Numero di capi necessari per la produzione di letame suino
        p_m = diet_params['p_m']
        rho = diet_params['rho']
        m_c = diet_params['m_c']
        A_capi = (M_B_LS * N) / (p_m * rho * m_c)


        # Debug dei valori intermedi
        debug_info = {
            'phi_LS': phi_LS,
            'phi_IT': phi_IT,
            'phi_SF': phi_SF,
            'Pg_LS': Pg_LS,
            'Pg_IT': Pg_IT,
            'Pg_SF': Pg_SF,
            'C_CH4_LS': C_CH4_LS,
            'C_CH4_IT': C_CH4_IT,
            'C_CH4_SF': C_CH4_SF,
            'M_B_tot_numerator': M_B_tot_numerator,
            'M_B_tot_denominator': M_B_tot_denominator,
            'M_B_tot_denominator_calculation': {
                'phi_LS * Pg_LS * C_CH4_LS': phi_LS * Pg_LS * C_CH4_LS,
                'phi_IT * Pg_IT * C_CH4_IT': phi_IT * Pg_IT * C_CH4_IT,
                'phi_SF * Pg_SF * C_CH4_SF': phi_SF * Pg_SF * C_CH4_SF,
            },
            'resa_IT': resa_IT,
            'p_m': p_m,
            'rho': rho,
            'm_c': m_c,
        }

        return render_template('diets/diet.html', dieta=f'Dieta {dieta_name}', ingredienti=ingredienti, percentuali=percentuali, E_el=param.E_el, M_ch4_tot=M_ch4_tot, M_B_tot=M_B_tot, M_B_IT=M_B_IT, M_B_LS=M_B_LS, S_IT=S_IT, A_capi=A_capi, input_values=input_values, debug_info=debug_info)

    return render_template('diets/diet.html', dieta=f'Dieta {dieta_name}', ingredienti=diete[dieta_name], input_values=input_values)

if __name__ == '__main__':
    app.run(debug=True)
