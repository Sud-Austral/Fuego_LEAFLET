import requests
import json
import pandas as pd
import sys
import datetime
import json
import pandas as pd
from geopy.geocoders import Nominatim

fuentes = [["https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_South_America_7d.csv",
            "MODIS"],
            ["https://firms.modaps.eosdis.nasa.gov/data/active_fire/suomi-npp-viirs-c2/csv/SUOMI_VIIRS_C2_South_America_7d.csv",
            "SUOMI"],
            ["https://firms.modaps.eosdis.nasa.gov/data/active_fire/noaa-20-viirs-c2/csv/J1_VIIRS_C2_South_America_7d.csv",
            "J1"]]

def setComuna(x):
    if(x["city"] != ""):
        return x["city"]
    elif(x["town"] != ""):
        return x["town"]
    elif(x["village"] != ""):
        return x["village"]
    else:
        return x["suburb"]

def getComunas(df):
    geolocator = Nominatim(user_agent="geoapiExercises")
    print(len(df))
    df['Coordenadas'] = df[['latitude', 'longitude']].apply(lambda x: f'{x.latitude},{x.longitude}', axis=1)
    #coordenadas = df[['latitude', 'longitude']].apply(lambda x: f'{x.latitude},{x.longitude}', axis=1)
    #df.assign(Coordenadas = coordenadas)
    print(2)
    df["Locacion"] = df["Coordenadas"].apply(lambda x: geolocator.reverse(x))
    referencia = ['road', 'city', 'county', 'state', 'country', 'country_code',
       'industrial', 'town', 'isolated_dwelling', 'hamlet', 'postcode',
       'building', 'neighbourhood', 'region', 'suburb', 'amenity',
       'man_made', 'village', 'office', 'historic', 'aeroway', 'tourism',
       'state_district', 'highway']
    print(3)
    for i in referencia:
        def AgregarColumn(x):
            try:
                return x.raw["address"][i]
            except:
                return ""
        df[i] = df["Locacion"].apply(lambda x: AgregarColumn(x))
    print(4)
    dfChile = df[df["country"] == "Chile"]
    print(5)
    dfChile = dfChile.reset_index()
    print(6)
    dfChile["Comuna"] = dfChile[["city","town","village","suburb"]].apply(setComuna, axis=1)
    ref = pd.read_excel(r"LocalizaGoogle.xlsx")
    print(7)
    ref = ref[['REGION', 'PROVINCIA', 'COMUNA','Comuna', 'ComunaUpper', 'raw']]
    dfFinal = dfChile.merge(ref, left_on='Comuna', right_on='Comuna',how="left")
    print(8)
    return dfFinal

def descarga(fuente):
    url = fuente[0]
    print(url)   
    #url = "https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_South_America_7d.csv"
    #df = pd.read_csv("https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_South_America_24h.csv")
    df = pd.read_csv(url) #.iloc[:200,:]
    #dfDate = df[df["acq_date"] == datetime.datetime.now().strftime("%Y-%m-%d")]
    #if(len(dfDate) > 0):
    dfDate = df
    dfLat = dfDate[dfDate["latitude"] < -16.5]
    #dfLat2 = dfLat[dfLat["longitude"] < -69.5]
    dfLat2 = dfLat[dfLat["longitude"] < -65.5]
    dfLat2 = dfLat2.reset_index()
    print("Tama??o descarga")
    print(fuente[1])
    print(len(dfLat2))
    try:
        dfLat2 = getComunas(dfLat2)
        dfLat2.to_csv(f"Data/{fuente[1]}/Puntos_Diarios_{fuente[1]}.csv",encoding='utf-8-sig')
        dfLat2.to_csv(f"Data_Legacy/{fuente[1]}/Puntos_Diarios_{fuente[1]}_{datetime.datetime.now().strftime('%Y-%m-%d')}.csv",encoding='utf-8-sig')    
    except:
        error = sys.exc_info()[1]
        print(error)
        print("Error en getComunas")
    
    # AQU?? SE PODR??A AGREGAR LA INFORMACI??N CALLE, COMUNA, PROVINCIA, REGI??N.
    # CALLE, COMUNA, PROVINCIA, REGI??N (INCLUIR JSON)

    
    
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
        f = {'acq_date': j["acq_date"],"lat":j["latitude"],"lng":j["longitude"]}
        features2.append(f.copy())
    salida = {"type":"FeatureCollection","features":features}
    with open(f'Data/{fuente[1]}/heatmap_{fuente[1]}.json', 'w') as file:
        json.dump(salida, file, indent=4)
    with open(f'Data/{fuente[1]}/data_{fuente[1]}.json', 'w') as file:
        json.dump(features2, file, indent=4)
    print(f"Se descargo la fuente {fuente}")
    return True

def getJSON2(df,fuente):
    features = []
    features2 = []
    for i, j in df.iterrows():
        f = {'type': 'Feature', \
            'geometry': {'type': 'Point', 'coordinates': [j["longitude"], j["latitude"]]}, \
            'properties': {'acq_date': j["acq_date"]}}
        features.append(f.copy())
        f = {'acq_date': j["acq_date"],"lat":j["latitude"],"lng":j["longitude"]}
        features2.append(f.copy())
    salida = {"type":"FeatureCollection","features":features}
    with open(f'Data/{fuente}/heatmap_{fuente}.json', 'w') as file:
        json.dump(salida, file, indent=4)
    with open(f'Data/{fuente}/data_{fuente}.json', 'w') as file:
        json.dump(features2, file, indent=4)
    print(f"Se descargo la fuente {fuente}")
    return True

def proceso():
    for i in fuentes:
        #descarga(i)
        getJSON(i)
    #'Data/J1/Puntos_Diarios_J1.csv'
    salida = []
    for ruta in ["MODIS","SUOMI","J1"]:
    #for ruta in ["MODIS"]:
        file = f'Data/{ruta}/Puntos_Diarios_{ruta}.csv'
        dfaux = pd.read_csv(file)
        dfaux["Fuente"] =  ruta
        dfaux.to_excel()
        salida.append(dfaux)
    pd.concat(salida).to_excel("Data/Consolidado/ConsolidadoPuntosCalor.xlsx", index=False)
    return

def saveConsolidado():
    diaActual = datetime.datetime.now().strftime("%Y-%m-%d")
    consolidado = pd.read_excel("Consolidado/ConsolidadoPuntosFuego.xlsx")
    consolidado = consolidado[consolidado["acq_date"].apply(lambda x: x != diaActual)]
    print("Tama??o Consolidado")
    print(len(consolidado))
    salida2 = []
    print(2)
    for i in fuentes:
        dfaux = pd.read_csv(i[0])
        dfaux["Fuente"] = i[1]
        getJSON2(dfaux,i[1])
        salida2.append(dfaux)

    consolidadoUpdate = pd.concat(salida2)
    #consolidadoUpdate = consolidadoUpdate[consolidadoUpdate["acq_date"].apply(lambda x: x not in consolidado["acq_date"].unique())]
    
    consolidadoUpdate = consolidadoUpdate[consolidadoUpdate["acq_date"].apply(lambda x: x == diaActual)]
    #consolidadoUpdate = consolidadoUpdate.reset_index()
    dfDate = consolidadoUpdate
    dfLat = dfDate[dfDate["latitude"] < -16.5]
    dfLat2 = dfLat[dfLat["longitude"] < -65.5]
    dfLat2 = dfLat2.reset_index()
    try:
        dfLat2 = getComunas(dfLat2)
    except:
        error = sys.exc_info()[1]
        print(error)
        print("Error en getComunas")
    dfFinal = pd.concat([consolidado,dfLat2])
    #dfFinal = dfFinal.reset_index()
    #dfFinal2 = dfFinal.drop(columns=["level_0","index","Unnamed: 0"])
    dfFinal.to_excel("Consolidado/ConsolidadoPuntosFuego.xlsx", index=False)
    print("ya deberia estar")
    #print(dfFinal)
    return 

if __name__ == '__main__':
    print(1)
    print("Se inicia")
    try:
        saveConsolidado()
        #proceso()
        print("Hola todo bien")
    except:
        error = sys.exc_info()[1]
        print(error)
        #try:
            #proceso()
        #    print("Hola todo bien")
        #except:
        #    error = sys.exc_info()[1]
        #    print(error)
    
    #geolocator = Nominatim(user_agent="geoapiExercises")
    #for i in fuentes:
    #    df = pd.read_csv(i[0])
    #    dfDate = df
    #    dfLat = dfDate[dfDate["latitude"] < -16.5]
    #    dfLat2 = dfLat[dfLat["longitude"] < -69.5]
    #    dfLat2 = dfLat2.reset_index()
    #    dfLat2 = getComunas(dfLat2)
        #dfLat2['Coordenadas'] = dfLat2[['latitude', 'longitude']].apply(lambda x: f'{x.latitude},{x.longitude}', axis=1)
        #dfLat2["Locacion"] = dfLat2["Coordenadas"].apply(lambda x: geolocator.reverse(x))
        #referencia = ['road', 'city', 'county', 'state', 'country', 'country_code',
        #    'industrial', 'town', 'isolated_dwelling', 'hamlet', 'postcode',
        #    'building', 'neighbourhood', 'region', 'suburb', 'amenity',
        #    'man_made', 'village', 'office', 'historic', 'aeroway', 'tourism',
        #    'state_district', 'highway']
        #for i in referencia:
        #    def AgregarColumn(x):
        #        try:
        #            return x.raw["address"][i]
        #        except:
        #            return ""
        #    df[i] = df["Locacion"].apply(lambda x: AgregarColumn(x))
        #dfChile = df[df["country"] == "Chile"]
        #dfChile = dfChile.reset_index()
        #dfChile["Comuna"] = dfChile[["city","town","village","suburb"]].apply(setComuna, axis=1)
        #ref = pd.read_excel(r"LocalizaGoogle.xlsx")
        #ref = ref[['REGION', 'PROVINCIA', 'COMUNA','Comuna', 'ComunaUpper', 'raw']]
        #dfFinal = dfChile.merge(ref, left_on='Comuna', right_on='Comuna',how="left")
        #print(dfLat2)
    