import requests
import json
import pandas as pd
import sys
import datetime

fuentes = [["https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_South_America_7d.csv",
            "MODIS"],
            ["https://firms.modaps.eosdis.nasa.gov/data/active_fire/suomi-npp-viirs-c2/csv/SUOMI_VIIRS_C2_South_America_7d.csv",
            "SUOMI"],
            ["https://firms.modaps.eosdis.nasa.gov/data/active_fire/noaa-20-viirs-c2/csv/J1_VIIRS_C2_South_America_7d.csv",
            "J1"]]

def descarga(fuente):
    url = fuente[0]
    #url = "https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_South_America_7d.csv"
    df = pd.read_csv("https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_South_America_24h.csv")
    dfDate = df[df["acq_date"] == datetime.datetime.now().strftime("%Y-%m-%d")]
    if(len(dfDate) > 0):
        dfDate = df
    dfLat = dfDate[dfDate["latitude"] < -16.5]
    dfLat2 = dfLat[dfLat["longitude"] < -69.5]
    dfLat2.to_csv(f"Data/{fuente[0]}/Puntos_Diarios_{fuente[0]}.csv")
    print(url)
    return dfLat2

def proceso():
    for i in fuentes:
        descarga(i)

if __name__ == '__main__':
    try:
        proceso()
    except:
        try:
            proceso()
        except:
            error = sys.exc_info()[1]
            print(error)