import requests
import json
import pandas as pd
import sys
import datetime
import json

fuentes = ['J1_fuente', 'SUOMI_fuente', 'MODIS_fuente']

def regiones(region):
    
    data = pd.read_excel('Incendios_24h/data.xlsx', sheet_name='regiones')

    try:
        data = data[data['COD_REGION'] == region]
        indx = data.index[0]
        
        resultado = data['REGION'][indx]

    except: 
        resultado = ' '

    return resultado

def provincias(prov):
    
    data = pd.read_excel('Incendios_24h/data.xlsx', sheet_name='provincias')

    try:
        data = data[data['COD_PROVIN'] == prov]
        indx = data.index[0]

        resultado = data['PROVINCIA'][indx]

    except:
        resultado = ' '
    
    return resultado

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
    print("Comenzamos")
    dfDatas = pd.read_excel('https://github.com/Sud-Austral/Fuego_LEAFLET/blob/main/SEMANARIO_INCENDIO/Consolidado/ConsolidadoPuntosFuego.xlsx?raw=true')
    print(1)
    dfAux = dfDatas[dfDatas['Coordenadas'] != '-27.12613,-109.28293000000001']
    print(2)
    dfAux2 = dfAux[dfAux['Coordenadas'] != '-27.126920000000002,-109.27901000000001']
    print(3)
    dfData = dfAux2[dfAux2['Fuente'] == dataFuente]
    print(4)
    dfData['NOM_REGION'] = dfData['REGION'].apply(lambda x: regiones(x))
    print(5)
    dfData['NOM_PROVINCIA'] = dfData['PROVINCIA'].apply(lambda x: provincias(x))
    print(6)
    # dfData.fillna(' ')

    dfLat2 = dfData
    print(7)
    # AQUÍ SE PODRÍA AGREGAR LA INFORMACIÓN CALLE, COMUNA, PROVINCIA, REGIÓN.
    # CALLE, COMUNA, PROVINCIA, REGIÓN (INCLUIR JSON)
    print(dfLat2)
    dfLat2.to_csv(f"Incendios_24h/Data/{fuente}/Puntos_Diarios_{fuente}.csv")
    dfLat2.to_csv(f"Incendios_24h/Data_Legacy/{fuente}/Puntos_Diarios_{fuente}_{datetime.datetime.now().strftime('%Y-%m-%d')}.csv")
    print(8)

    
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
        print('1')
        print(i)
        #descarga(i)
        getJSON(i)

if __name__ == '__main__':

    proceso()

