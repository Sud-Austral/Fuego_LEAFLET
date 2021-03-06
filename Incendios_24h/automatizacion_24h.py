import requests
import json
import pandas as pd
import sys
import datetime
import json

fuentes = [["https://github.com/Sud-Austral/Fuego_LEAFLET/blob/main/SEMANARIO_INCENDIO/Consolidado/ConsolidadoPuntosFuego.xlsx?raw=true",
            "MODIS_24h"],
            ["https://github.com/Sud-Austral/Fuego_LEAFLET/blob/main/SEMANARIO_INCENDIO/Consolidado/ConsolidadoPuntosFuego.xlsx?raw=true",
            "SUOMI_24h"],
            ["https://github.com/Sud-Austral/Fuego_LEAFLET/blob/main/SEMANARIO_INCENDIO/Consolidado/ConsolidadoPuntosFuego.xlsx?raw=true",
            "J1_24h"]]

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
    url = fuente[0]
    dataFuente = ''

    if(fuente[1] == 'MODIS_24h'):
        dataFuente = 'MODIS'

    if(fuente[1] == 'SUOMI_24h'):
        dataFuente = 'SUOMI'

    if(fuente[1] == 'J1_24h'):
        dataFuente = 'J1'

    print('FUENTE 24: ' + str(dataFuente))   
    
    today = str(datetime.datetime.today())[0:10]
    #yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")

    new_today = [today]#,yesterday]
    
    dfDatas = pd.read_excel(url)

    dfAux = dfDatas[dfDatas['Coordenadas'] != '-27.12613,-109.28293000000001']
    dfAux2 = dfAux[dfAux['Coordenadas'] != '-27.126920000000002,-109.27901000000001']

    ##df = dfAux2[dfAux2['acq_date'] == today]
    df = dfAux2[dfAux2['acq_date'].apply(lambda x: x in new_today)]
    print(df["acq_date"].head(5))
    print("a")
    df['NOM_REGION'] = df['REGION'].apply(lambda x: regiones(x))
    print("b")
    df['NOM_PROVINCIA'] = df['PROVINCIA'].apply(lambda x: provincias(x))
    print("c")
    df = df[df['Fuente'] == dataFuente]
    print("d")
    dfLat2 = df  #.reset_index()
    print("e")

    # AQU?? SE PODR??A AGREGAR LA INFORMACI??N CALLE, COMUNA, PROVINCIA, REGI??N.
    # CALLE, COMUNA, PROVINCIA, REGI??N (INCLUIR JSON)
    print("Puntos de Calor")
    print(len(dfLat2))
    dfLat2.to_csv(f"Incendios_24h/Data/{fuente[1]}/Puntos_Diarios_{fuente[1]}.csv")
    dfLat2.to_csv(f"Incendios_24h/Data_Legacy/{fuente[1]}/Puntos_Diarios_{fuente[1]}_{datetime.datetime.now().strftime('%Y-%m-%d')}.csv")
    

    
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
    with open(f'Incendios_24h/Data/{fuente[1]}/heatmap_{fuente[1]}.json', 'w') as file:
        json.dump(salida, file, indent=4)
    with open(f'Incendios_24h/Data/{fuente[1]}/data_{fuente[1]}.json', 'w') as file:
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