import requests
import json
import pandas as pd
import sys
import datetime

def proceso():
    url = "https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_South_America_7d.csv"
    df = pd.read_csv("https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_South_America_24h.csv")
    dfDate = df[df["acq_date"] == datetime.datetime.now().strftime("%Y-%m-%d")]
    if(len(dfDate) > 0):
        dfDate = df
    dfLat = dfDate[dfDate["latitude"] < -16.5]
    dfLat2 = dfLat[dfLat["longitude"] < -69.5]
    dfLat2.to_csv("Data/Puntos_Diarios.csv")
    return dfLat2

if __name__ == '__main__':
    try:
        proceso()
    except:
        try:
            proceso()
        except:
            error = sys.exc_info()[1]
            print(error)