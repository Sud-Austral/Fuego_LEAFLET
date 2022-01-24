import requests
import json
import pandas as pd
import sys
import datetime
import json

fuentes = ['MODIS_fuente', 'SUOMI_fuente', 'J1_fuente']

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
    print('FUENTEEE: ' + fuente)
    dataFuente = ''

    if(fuente == 'MODIS_fuente'):
        dataFuente = 'MODIS'

    if(fuente == 'SUOMI_fuente'):
        dataFuente = 'SUOMI'

    if(fuente == 'J1_fuente'):
        dataFuente = 'J1'

    print('FUENTE: ' + str(dataFuente))   
    

    dfData = pd.read_excel('https://github.com/Sud-Austral/Fuego_LEAFLET/blob/main/SEMANARIO_INCENDIO/Consolidado/ConsolidadoPuntosFuego.xlsx?raw=true')
    dfData = dfData[dfData['Fuente'] == dataFuente]

    dfData['NOM_REGION'] = dfData['REGION'].apply(lambda x: regiones(x))
    dfData['NOM_PROVINCIA'] = dfData['PROVINCIA'].apply(lambda x: provincias(x))

    dfLat2 = dfData

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
    for i in fuentes:
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