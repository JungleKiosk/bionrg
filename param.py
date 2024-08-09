# Specifiche di progetto fisse
P = 1000  # Potenza in kW per 1 MW
t = 8040  # ore annue
n = 0.45  # Rendimento elettrico
H = 10  # Potere calorifero (kWh/Nm³)
E_el = P * 24  # Energia elettrica giornaliera in kWh

# Potenziale metanigeno (valori presi dai file Excel)
pot_pg_animali = {
    'liquame_bovino': 30,#A-1
    'letame_bovino': 70,#B,D-1
    'liquame_suino': 20,#C-1
    'letame_suino': 90,#E-1
}

pot_ch4_animali = {
    'liquame_bovino': 0.55,#A-1
    'letame_bovino': 0.55,#B,D-1
    'liquame_suino': 0.62,#C-1
    'letame_suino': 0.62,#E-1
}

pot_pg_colture = {
    'insilato_mais': 200,#A,B,C-1
    'insilato_sorgo': 150,#D-1
    'insilato_triticale': 185,#185
}

pot_ch4_colture = {
    'insilato_mais': 0.53,#A,B,C-1
    'insilato_sorgo': 0.52,#D-1
    'insilato_triticale': 0.53,#E-1
}

pot_pg_scarti = {
    'bucce_pomodoro': 100,#C-1
    'siero_latte': 30,#A-1
    'scarti_frutta': 130,#E-1
    'sansa_olive': 200,#D-1
    'scarti_patata': 120,#B-1
}

pot_ch4_scarti = {
    'bucce_pomodoro': 0.55,#C-1
    'siero_latte': 0.60,#A-1
    'scarti_frutta': 0.55,#E-1
    'sansa_olive': 0.55,#D-1
    'scarti_patata': 0.57,#B-1
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
    'letame_suino': 55,#E
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

def get_diet_params(dieta_name):
    params = {}
    if dieta_name == 'A':
        params['resa_IT'] = resa_r_colture['insilato_mais']
        params['p_m'] = prod_pm_reflui['liquame_bovino']
        params['rho'] = prod_p_reflui['liquame_bovino']
        params['m_c'] = prod_mc_reflui['liquame_bovino']
    elif dieta_name == 'B':
        params['resa_IT'] = resa_r_colture['insilato_mais']
        params['p_m'] = prod_pm_reflui['letame_bovino']
        params['rho'] = prod_p_reflui['letame_bovino']
        params['m_c'] = prod_mc_reflui['letame_bovino']
    elif dieta_name == 'C':
        params['resa_IT'] = resa_r_colture['insilato_mais']
        params['p_m'] = prod_pm_reflui['liquame_suino']
        params['rho'] = prod_p_reflui['liquame_suino']
        params['m_c'] = prod_mc_reflui['liquame_suino']
    elif dieta_name == 'D':
        params['resa_IT'] = resa_r_colture['insilato_sorgo']
        params['p_m'] = prod_pm_reflui['letame_bovino']
        params['rho'] = prod_p_reflui['letame_bovino']
        params['m_c'] = prod_mc_reflui['letame_bovino']
    elif dieta_name == 'E':
        params['resa_IT'] = resa_r_colture['insilato_triticale']
        params['p_m'] = prod_pm_reflui['letame_suino']
        params['rho'] = prod_p_reflui['letame_suino']
        params['m_c'] = prod_mc_reflui['letame_suino']
    return params