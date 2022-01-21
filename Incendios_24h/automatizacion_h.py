import requests
import json
import pandas as pd
import sys
import datetime
import json

fuentes = [["https://github.com/Sud-Austral/Fuego_LEAFLET/blob/main/SEMANARIO_INCENDIO/Consolidado/ConsolidadoPuntosFuego.xlsx?raw=true",
            "MODIS_diario"],
            ["https://github.com/Sud-Austral/Fuego_LEAFLET/blob/main/SEMANARIO_INCENDIO/Consolidado/ConsolidadoPuntosFuego.xlsx?raw=true",
            "SUOMI_diario"],
            ["https://github.com/Sud-Austral/Fuego_LEAFLET/blob/main/SEMANARIO_INCENDIO/Consolidado/ConsolidadoPuntosFuego.xlsx?raw=true",
            "J1_diario"]]


def proceso():
    for registro in fuentes:
        #descarga(i)
        print(registro)
        # getJSON(registro)
        # print(i[1])
        # print(i[0])
        # print(i)

if __name__ == '__main__':
    try:
        proceso()
    except:
        try:
            proceso()
        except:
            error = sys.exc_info()[1]
            print(error)