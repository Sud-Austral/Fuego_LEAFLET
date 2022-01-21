import requests
import json
import pandas as pd
import sys
import datetime
import json

fuentes = [["https://github.com/Sud-Austral/Fuego_LEAFLET/blob/main/SEMANARIO_INCENDIO/Consolidado/ConsoliddddadoPuntosFuego.xlsx",
            "MODIS_diario"],
            ["https://github.com/Sud-Austral/Fuego_LEAFLET/blob/main/SEMANARIO_INCENDIO/Consolidado/ConsolidqwwadoPuntosFuego.xlsx",
            "SUOMI_diario"],
            ["https://github.com/Sud-Austral/Fuego_LEAFLET/blob/main/SEMANARIO_INCENDIO/Consolidado/ConsolidqwqadoPuntosFuego.xlsx",
            "J1_diario"]]

def proceso():
    for i in fuentes:
        #descarga(i)
        print(i)
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