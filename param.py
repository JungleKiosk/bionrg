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
    'bucce_pomodoro': 0.55,
    'siero_latte': 0.60,
    'scarti_frutta': 0.55,
    'sansa_olive': 0.55,
    'scarti_patata': 0.57,
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
