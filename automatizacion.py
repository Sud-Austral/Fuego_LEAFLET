import requests
import json
import pandas as pd
import sys

#BENCINA EN LÍNEA:

def proceso():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/bencina-en-linea/v1/combustibles/vehicular/estaciones.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("combustibles_vehicular_estaciones.xlsx", index = False)

def proceso2():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/bencina-en-linea/v1/combustibles/vehicular/estaciones/diesel.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("combustibles_vehicular_estaciones_diesel.xlsx", index = False)

def proceso3():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/bencina-en-linea/v1/combustibles/vehicular/estaciones/gasolina93.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("combustibles_vehicular_estaciones_gasolina93.xlsx", index = False)

def proceso4():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/bencina-en-linea/v1/combustibles/vehicular/estaciones/gasolina95.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("combustibles_vehicular_estaciones_gasolina95.xlsx", index = False)

def proceso5():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/bencina-en-linea/v1/combustibles/vehicular/estaciones/gasolina97.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("combustibles_vehicular_estaciones_gasolina97.xlsx", index = False)

def proceso6():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/bencina-en-linea/v1/combustibles/vehicular/estaciones/glp.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("combustibles_vehicular_estaciones_glp.xlsx", index = False)

def proceso7():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/bencina-en-linea/v1/combustibles/vehicular/estaciones/gnc.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("combustibles_vehicular_estaciones_gnc.xlsx", index = False)

def proceso8():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/bencina-en-linea/v1/emisiones.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("combustibles_vehicular_estaciones_gnc.xlsx", index = False)

#CAPACIDAD INSTALADA:

def proceso9():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/capacidad-instalada/v1/convencional.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("capacidad-instalada_v1_convencional.xlsx", index = False)

def proceso10():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/capacidad-instalada/v1/enoperacion.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("capacidad-instalada_v1_enoperacion.xlsx", index = False)

def proceso11():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/capacidad-instalada/v1/enpruebas.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("capacidad-instalada_v1_enpruebas.xlsx", index = False)

def proceso12():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/capacidad-instalada/v1/ernc.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("capacidad-instalada_v1_ernc.xlsx", index = False)

def proceso13():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/capacidad-instalada/v1/sistemas.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("capacidad-instalada_v1_sistemas.xlsx", index = False)

#INDICADORES DIARIOS:

def proceso14():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/indicadores-diarios/v1/brent.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("indicadores-diarios_v1_brent.xlsx", index = False)

def proceso15():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/indicadores-diarios/v1/dolar.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("indicadores-diarios_v1_dolar.xlsx", index = False)

def proceso16():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/indicadores-diarios/v1/euro.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("indicadores-diarios_v1_euro.xlsx", index = False)

def proceso17():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/indicadores-diarios/v1/henryhub.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("indicadores-diarios_v1_henryhub.xlsx", index = False)

def proceso18():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/indicadores-diarios/v1/uf.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("indicadores-diarios_v1_uf.xlsx", index = False)

def proceso19():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/indicadores-diarios/v1/utm.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("indicadores-diarios_v1_utm.xlsx", index = False)

def proceso20():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/indicadores-diarios/v1/wti.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("indicadores-diarios_v1_wti.xlsx", index = False)

#COSTOS MARGINALES:

def proceso21():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/costos-marginales/v1/diarios/atacama.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("costos-marginales_v1_diarios_atacama.xlsx", index = False)

def proceso22():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/costos-marginales/v1/diarios/cardones.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("costos-marginales_v1_diarios_cardones.xlsx", index = False)

def proceso23():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/costos-marginales/v1/diarios/charrua.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("costos-marginales_v1_diarios_charrua.xlsx", index = False)

def proceso24():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/costos-marginales/v1/diarios/crucero.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("costos-marginales_v1_diarios_crucero.xlsx", index = False)

def proceso25():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/costos-marginales/v1/diarios/pandeazucar.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("costos-marginales_v1_diarios_pandeazucar.xlsx", index = False)

def proceso26():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/costos-marginales/v1/diarios/puertomontt.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("costos-marginales_v1_diarios_puertomontt.xlsx", index = False)

def proceso27():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/costos-marginales/v1/diarios/quillota.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("costos-marginales_v1_diarios_quillota.xlsx", index = False)

def proceso28():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/costos-marginales/v1/diarios/tarapaca.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("costos-marginales_v1_diarios_tarapaca.xlsx", index = False)

def proceso29():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/costos-marginales/v1/horarios/atacama.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("costos-marginales_v1_horarios_atacama.xlsx", index = False)

def proceso30():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/costos-marginales/v1/horarios/cardones.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("costos-marginales/v1/horarios/cardones.xlsx", index = False)

def proceso31():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/costos-marginales/v1/horarios/charrua.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("costos-marginales_v1_horarios_charrua.xlsx", index = False)

def proceso32():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/costos-marginales/v1/horarios/crucero.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("costos-marginales_v1_horarios_crucero.xlsx", index = False)

def proceso33():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/costos-marginales/v1/horarios/pandeazucar.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("costos-marginales_v1_horarios_pandeazucar.xlsx", index = False)

def proceso34():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/costos-marginales/v1/horarios/puertomontt.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("costos-marginales_v1_horarios_puertomontt.xlsx", index = False)

def proceso35():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/costos-marginales/v1/horarios/quillota.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("costos-marginales_v1_horarios_quillota.xlsx", index = False)

def proceso36():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/costos-marginales/v1/horarios/tarapaca.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("costos-marginales_v1_horarios_tarapaca.xlsx", index = False)

#GENERACIÓN BRUTA:

def proceso37():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/generacion-bruta/v1/horaria/convencional.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("generacion-bruta_v1_horaria_convencional.xlsx", index = False)

def proceso38():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/generacion-bruta/v1/horaria/ernc.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("generacion-bruta_v1_horaria_ernc.xlsx", index = False)

def proceso39():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/generacion-bruta/v1/mensual/convencional.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("generacion-bruta_v1_mensual_convencional.xlsx", index = False)

def proceso40():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/generacion-bruta/v1/mensual/ernc.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("generacion-bruta_v1_mensual_ernc.xlsx", index = False)

def proceso41():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/generacion-bruta/v1/mensual/sic/tecnologia.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("generacion-bruta_v1_mensual_sic_tecnologia.xlsx", index = False)

def proceso42():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/generacion-bruta/v1/mensual/sing/tecnologia.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("generacion-bruta_v1_mensual_sing_tecnologia.xlsx", index = False)

def proceso43():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/generacion-bruta/v1/mensual/sistema.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("generacion-bruta_v1_mensual_sistema.xlsx", index = False)

def proceso44():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/generacion-bruta/v1/mensual/total.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("generacion-bruta_v1_mensual_total.xlsx", index = False)

#Importación y exportación:

def proceso45():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/importacion-y-exportacion/v1/anios.ajson/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame({"anios": result["result"][0]})
    df.to_excel("importacion-y-exportacion_v1_anios.xlsx", index = False)

def proceso46():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/importacion-y-exportacion/v1/exportacion.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.ajson(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("importacion-y-exportacion_v1_exportacion.xlsx", index = False)

def proceso47():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/importacion-y-exportacion/v1/exportacion/resumen.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("importacion-y-exportacion_v1_exportacion_resumen.xlsx", index = False)

def proceso48():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/importacion-y-exportacion/v1/importacion.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("importacion-y-exportacion_v1_importacion.xlsx", index = False)

def proceso49():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/importacion-y-exportacion/v1/importacion/resumen.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("importacion-y-exportacion_v1_importacion_resumen.xlsx", index = False)

def proceso50():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/importacion-y-exportacion/v1/ultimo-mes-disponible.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("importacion-y-exportacion_v1_ultimo-mes-disponible.xlsx", index = False)

#CALEFACCIÓN EN LINEA:

def proceso51():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/calefaccion-en-linea/v1/kerosene.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("calefaccion-en-linea_v1_kerosene.xlsx", index = False)

def proceso52():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/calefaccion-en-linea/v1/lena.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("calefaccion-en-linea_v1_lena.xlsx", index = False)

#SAIDI:


#def proceso53():
#    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
#    url = 'https://api.desarrolladores.energiaabierta.cl/saidi/v1/mensual/{codigoComuna}.json/'
#    get_url = f"{url}?auth_key={api_auth}&limit=5000"

#    response = requests.get(get_url)
#    result = response.json(strict=False)
#    df = pd.DataFrame(result["data"])
#    df.columns = result["headers"]
#    df.to_excel("saidi/v1/mensual/{codigoComuna}.xlsx", index = False)

#PEQUEÑOS MEDIOS DE GENERACIÓN DISTRIBUIDA:
 
def proceso54():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/pequenos-medios-de-generacion-distribuida/v1/netbilling.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("pequenos-medios-de-generacion-distribuida_v1_netbilling.xlsx", index = False)

def proceso55():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/pequenos-medios-de-generacion-distribuida/v1/pmgd/comunas.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("pequenos-medios-de-generacion-distribuida_v1_pmgd_comunas.xlsx", index = False)

def proceso56():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/pequenos-medios-de-generacion-distribuida/v1/regiones.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("pequenos-medios-de-generacion-distribuida_v1_regiones.xlsx", index = False)

#FACTORES DE EMISIÓN:

def proceso57():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/factores-de-emision/v1/anual.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("factores-de-emision_v1_anual.xlsx", index = False)

def proceso58():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/factores-de-emision/v1/mensual.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("factores-de-emision_v1_mensual.xlsx", index = False)

#BALANCE DE ENERGÍA:

def proceso59():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/balance-de-energia/v1/balance-nacional.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("balance-de-energia_v1_balance-nacional.xlsx", index = False)

def proceso60():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/balance-de-energia/v1/balance-nacional/anios.ajson/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("balance-de-energia_v1_balance-nacional_anios.xlsx", index = False)

def proceso61():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/balance-de-energia/v1/balance-nacional/consumo-final.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("balance-de-energia_v1_balance-nacional_consumo-final.xlsx", index = False)

#ENERGÍA EMBALSADA:

def proceso62():
    api_auth = "1594882b82550b038f365b0c6a7976682bdd0192"
    url = 'https://api.desarrolladores.energiaabierta.cl/energia-embalsada/v1/embalses.json/'
    get_url = f"{url}?auth_key={api_auth}&limit=5000"

    response = requests.get(get_url)
    result = response.json(strict=False)
    df = pd.DataFrame(result["data"])
    df.columns = result["headers"]
    df.to_excel("energia-embalsada_v1_embalses.xlsx", index = False)






if __name__ == '__main__':
    try:
        proceso()
    except:
        try:
            proceso()
        except:
            error = sys.exc_info()[1]
            print(error)
        
    try:
        proceso2()
    except:
        try:
            proceso2()
        except:
            error = sys.exc_info()[1]
            print(error)

    try:
        proceso3()
    except:
        try:
            proceso3()
        except:
            error = sys.exc_info()[1]
            print(error)

    try:
        proceso4()
    except:
        try:
            proceso4()
        except:
            error = sys.exc_info()[1]
            print(error)
    try:
        proceso5()
    except:
        try:
            proceso5()
        except:
            error = sys.exc_info()[1]
            print(error)
    
    try:
        proceso6()
    except:
        try:
            proceso6()
        except:
            error = sys.exc_info()[1]
            print(error)
            
    try:
        proceso7()
    except:
        try:
            proceso7()
        except:
            error = sys.exc_info()[1]
            print(error)
    
    try:
        proceso8()
    except:
        try:
            proceso8()
        except:
            error = sys.exc_info()[1]
            print(error)
    
    try:
        proceso9()
    except:
        try:
            proceso9()
        except:
            error = sys.exc_info()[1]
            print(error)

    try:
        proceso10()
    except:
        try:
            proceso10()
        except:
            error = sys.exc_info()[1]
            print(error)

    try:
        proceso11()
    except:
        try:
            proceso11()
        except:
            error = sys.exc_info()[1]
            print(error)
    
    try:
        proceso12()
    except:
        try:
            proceso12()
        except:
            error = sys.exc_info()[1]
            print(error)
    
    try:
        proceso13()
    except:
        try:
            proceso13()
        except:
            error = sys.exc_info()[1]
            print(error)

    try:
        proceso14()
    except:
        try:
            proceso14()
        except:
            error = sys.exc_info()[1]
            print(error)

    try:
        proceso15()
    except:
        try:
            proceso15()
        except:
            error = sys.exc_info()[1]
            print(error) 
    
    try:
        proceso16()
    except:
        try:
            proceso16()
        except:
            error = sys.exc_info()[1]
            print(error)

    try:
        proceso17()
    except:
        try:
            proceso17()
        except:
            error = sys.exc_info()[1]
            print(error)

    try:
        proceso18()
    except:
        try:
            proceso18()
        except:
            error = sys.exc_info()[1]
            print(error)

    try:
        proceso19()
    except:
        try:
            proceso19()
        except:
            error = sys.exc_info()[1]
            print(error)
    
    try:
        proceso20()
    except:
        try:
            proceso20()
        except:
            error = sys.exc_info()[1]
            print(error)

    try:
        proceso21()
    except:
        try:
            proceso21()
        except:
            error = sys.exc_info()[1]
            print(error)

    try:
        proceso22()
    except:
        try:
            proceso22()
        except:
            error = sys.exc_info()[1]
            print(error)

    try:
        proceso23()
    except:
        try:
            proceso23()
        except:
            error = sys.exc_info()[1]
            print(error)

    try:
        proceso24()
    except:
        try:
            proceso24()
        except:
            error = sys.exc_info()[1]
            print(error)

    try:
        proceso25()
    except:
        try:
            proceso25()
        except:
            error = sys.exc_info()[1]
            print(error)

    try:
        proceso26()
    except:
        try:
            proceso26()
        except:
            error = sys.exc_info()[1]
            print(error)

    try:
        proceso27()
    except:
        try:
            proceso27()
        except:
            error = sys.exc_info()[1]
            print(error)

    try:
        proceso28()
    except:
        try:
            proceso28()
        except:
            error = sys.exc_info()[1]
            print(error)

    try:
        proceso29()
    except:
        try:
            proceso29
        except:
            error = sys.exc_info()[1]
            print(error)

    try:
        proceso30()
    except:
        try:
            proceso30()
        except:
            error = sys.exc_info()[1]
            print(error)

    try:
        proceso31()
    except:
        try:
            proceso31()
        except:
            error = sys.exc_info()[1]
            print(error)

    try:
        proceso32()
    except:
        try:
            proceso32()
        except:
            error = sys.exc_info()[1]
            print(error)

    try:
        proceso33()
    except:
        try:
            proceso33()
        except:
            error = sys.exc_info()[1]
            print(error)

    try:
        proceso34()
    except:
        try:
            proceso34()
        except:
            error = sys.exc_info()[1]
            print(error)

    try:
        proceso35()
    except:
        try:
            proceso35()
        except:
            error = sys.exc_info()[1]
            print(error)

    try:
        proceso36()
    except:
        try:
            proceso36()
        except:
            error = sys.exc_info()[1]
            print(error)

    try:
        proceso37()
    except:
        try:
            proceso37()
        except:
            error = sys.exc_info()[1]
            print(error)

    try:
        proceso38()
    except:
        try:
            proceso38()
        except:
            error = sys.exc_info()[1]
            print(error)
    
    try:
        proceso39()
    except:
        try:
            proceso39()
        except:
            error = sys.exc_info()[1]
            print(error)
    
    try:
        proceso40()
    except:
        try:
            proceso40
        except:
            error = sys.exc_info()[1]
            print(error)
    
    try:
        proceso41()
    except:
        try:
            proceso41()
        except:
            error = sys.exc_info()[1]
            print(error)
    
    try:
        proceso42()
    except:
        try:
            proceso42()
        except:
            error = sys.exc_info()[1]
            print(error)
    
    try:
        proceso43()
    except:
        try:
            proceso43()
        except:
            error = sys.exc_info()[1]
            print(error)
    
    try:
        proceso44()
    except:
        try:
            proceso44
        except:
            error = sys.exc_info()[1]
            print(error)
    
    try:
        proceso45()
    except:
        try:
            proceso45()
        except:
            error = sys.exc_info()[1]
            print(error)
    
    try:
        proceso46()
    except:
        try:
            proceso46()
        except:
            error = sys.exc_info()[1]
            print(error)
    
    try:
        proceso47()
    except:
        try:
            proceso47()
        except:
            error = sys.exc_info()[1]
            print(error)
    
    try:
        proceso48()
    except:
        try:
            proceso48()
        except:
            error = sys.exc_info()[1]
            print(error)
    
    try:
        proceso49()
    except:
        try:
            proceso49()
        except:
            error = sys.exc_info()[1]
            print(error)
    
    try:
        proceso50()
    except:
        try:
            proceso50()
        except:
            error = sys.exc_info()[1]
            print(error)
    
    try:
        proceso51()
    except:
        try:
            proceso51()
        except:
            error = sys.exc_info()[1]
            print(error)
    
    try:
        proceso52()
    except:
        try:
            proceso52
        except:
            error = sys.exc_info()[1]
            print(error)
    
    #try:
    #    proceso53()
    #except:
    #    try:
    #        proceso53()
    #    except:
    #        error = sys.exc_info()[1]
    #        print(error)
    
    try:
        proceso54()
    except:
        try:
            proceso54()
        except:
            error = sys.exc_info()[1]
            print(error)
    
    try:
        proceso55()
    except:
        try:
            proceso55()
        except:
            error = sys.exc_info()[1]
            print(error)
    
    try:
        proceso56()
    except:
        try:
            proceso56()
        except:
            error = sys.exc_info()[1]
            print(error)
    
    try:
        proceso57()
    except:
        try:
            proceso57()
        except:
            error = sys.exc_info()[1]
            print(error)
    
    try:
        proceso58()
    except:
        try:
            proceso58()
        except:
            error = sys.exc_info()[1]
            print(error)
    
    try:
        proceso59()
    except:
        try:
            proceso59()
        except:
            error = sys.exc_info()[1]
            print(error)
    
    try:
        proceso60()
    except:
        try:
            proceso60()
        except:
            error = sys.exc_info()[1]
            print(error)
    
    try:
        proceso61()
    except:
        try:
            proceso61()
        except:
            error = sys.exc_info()[1]
            print(error)
    
    try:
        proceso62()
    except:
        try:
            proceso62()
        except:
            error = sys.exc_info()[1]
            print(error)
    
