import requests
import json
import pandas as pd
import sys
import datetime
import json

fuentesLink = 'https://github.com/Sud-Austral/Fuego_LEAFLET/blob/main/SEMANARIO_INCENDIO/Consolidado/ConsolidadoPuntosFuego.xlsx?raw=true'
fuentePuntos = ['MODIS_24h', 'SUOMI_24h', 'J1_24h']

def regiones(region):
    
    data = pd.read_excel('Incendios_24h/data.xlsx', sheet_name='regiones')
    data = data[data['COD_REGION'] == region]
    
    indx = data.index[0]
    
    return data['REGION'][indx]

def provincias(prov):
    
    data = pd.read_excel('Incendios_24h/data.xlsx', sheet_name='provincias')
    data = data[data['COD_PROVIN'] == prov]
    
    indx = data.index[0]
    
    return data['PROVINCIA'][indx]

def descarga(fuente):
    print(fuente)
    print(fuentesLink)
    
    url = fuentesLink

    df = pd.read_excel(url)

    df['NOM_REGION'] = df['REGION'].apply(lambda x: regiones(x))
    df['NOM_PROVINCIA'] = df['PROVINCIA'].apply(lambda x: provincias(x))

    df = df[df['Fuente'] == fuente]

    dfLat2 = df

    # AQUÍ SE PODRÍA AGREGAR LA INFORMACIÓN CALLE, COMUNA, PROVINCIA, REGIÓN.
    # CALLE, COMUNA, PROVINCIA, REGIÓN (INCLUIR JSON)

    dfLat2.to_csv(f"Incendios_24h/Data/{fuente}/Puntos_Diarios_{fuente}.csv")
    dfLat2.to_csv(f"Incendios_24h/Data_Legacy/{fuente}/Puntos_Diarios_{fuente}_{datetime.datetime.now().strftime('%Y-%m-%d')}.csv")
    
    return dfLat2

def getJSON(fuente):
    df = descarga(fuente)
    features = []
    features2 = []
    for i, j in df.iterrows():
        f = {'type': 'Feature', \
            'geometry': {'type': 'Point', 'coordinates': [j["longitude"], j["latitude"]]}, \
            'properties': {'acq_date': j["acq_date"]}}
        features.append(f.copy())
        f = {'acq_date': j["acq_date"],"lat":j["latitude"],"lng":j["longitude"], "location": j["Locacion"], "region": j["NOM_REGION"], "provincia": j["NOM_PROVINCIA"], "comuna": j["Comuna"]}
        features2.append(f.copy())
    salida = {"type":"FeatureCollection","features":features}
    with open(f'Incendios_24h/Data/{fuente}/heatmap_{fuente}.json', 'w') as file:
        json.dump(salida, file, indent=4)
    with open(f'Incendios_24h/Data/{fuente}/data_{fuente}.json', 'w') as file:
        json.dump(features2, file, indent=4)
    return True

def proceso():
    for i in fuentePuntos:
        #descarga(i)

        getJSON(i)

if __name__ == '__main__':
    try:
        proceso()
    except:
        try:
            proceso()
        except:
            error = sys.exc_info()[1]
            print(error)