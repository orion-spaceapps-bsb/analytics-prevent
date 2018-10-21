from netCDF4 import Dataset
import numpy as np
import datetime
import matplotlib.pyplot as plt
import math
import matplotlib.mlab as mlab
from flask import jsonify
from flask import Flask
import codecs
import json
import pandas as pd

# usar numero de habitante para fazer calculo de gasto com correçao
# receber input de capacidade de escoamento do solo para ver quantas vezes chove mais que a capacidade
# receber area da cidade para calcular o preço da obra
# calcular o preço da obra
# calcular retorno por investimento com preço da obra e calculo de gasto com correçao
app = Flask(__name__)


def getLatitudeAsIndex(lat):
    latitudeInit = -49.875
    latitudeAsIndex = 0
    while latitudeInit <= 49.875:
        if lat == latitudeInit:
            return latitudeAsIndex
        else:
            latitudeAsIndex += 1
            latitudeInit = latitudeInit + 0.25


def getLongitudeAsIndex(lon):
    longitudeInit = -179.875
    longitudeAsIndex = 0
    while longitudeInit <= 179.875:
        if lon == longitudeInit:
            return longitudeAsIndex
        else:
            longitudeAsIndex += 1
            longitudeInit = longitudeInit + 0.25


def getPrecipitation(lat, lon, date):
    # LATITUDE EH A COLUNA LONGITUDE EH A LINHA
    path = ("./data/3B42_Daily.%s.7.nc4" % (date))
    latitudeIndex = getLatitudeAsIndex(lat)
    longitudeIndex = getLongitudeAsIndex(lon)
    result = Dataset(path)
    a = (result.variables['precipitation'][longitudeIndex][latitudeIndex])
    return a


def parseDates(y, m, d):
    date = datetime.date(y, m, d)
    dates = list()
    for i in range(265):
        date += datetime.timedelta(days=1)
        dates.append(date.strftime("%Y%m%d"))
    return dates


def calcFloodIntensity(preciptation, soilRunoff):
    floodIntensity = 0
    initialLoss = 0.2 * soilRunoff
    if preciptation <= (initialLoss):
        return floodIntensity
    else:
        floodIntensity = (preciptation - (initialLoss)) / \
            ((preciptation-(initialLoss))+soilRunoff)
        return floodIntensity


def calcRunoffCurveNumber(soilRunoff):
    return 25400/(soilRunoff - 254)


def calcDemographicDensity(area, population):
    return area/population


def calcCostByPopulation(population):
    return 200*population


# dates = list()
# dates = (parseDates(2017, 11, 7))

# i = 0
# result = list()
# for i in range(len(dates)):
#     # passa latitude e depois longitude
#     date = (dates[i])
#     response = getPrecipitation(44.125, -89.875, str(date))
#     result.append(response)

# # print(len(result))
# # print(result)

# fullFloodIntensity = list()
# for i in range(len(result)):
#     fullFloodIntensity.append(calcFloodIntensity(result[i], 30))

# print(fullFloodIntensity)

# plot graphics

# a(np.median(result))
# plt.plot(fullFloodIntensity)
# plt.ylabel('flood intensity')
# plt.xlabel('day')
# plt.show()

# mu = np.mean(result)
# variance = 1
# sigma = math.sqrt(variance)
# x = np.linspace(mu - 3*sigma, mu + 3*sigma, 100)
# plt.plot(x, mlab.normpdf(x, mu, sigma))
# plt.show()


@app.route('/')
def entry_point():
    return 'Hello World!'


@app.route('/projects')
def getSugestion():
    dates = list()
    dates = (parseDates(2017, 11, 7))

    i = 0
    result = list()
    for i in range(len(dates)):
        # passa latitude e depois longitude
        date = (dates[i])
        response = getPrecipitation(44.125, -89.875, str(date))
        result.append(response)

    # print(len(result))
    print(result)

    fullFloodIntensity = list()
    for i in range(len(result)):
        fullFloodIntensity.append(calcFloodIntensity(result[i], 30))

    return pd.Series(result).to_json(orient='values')


if __name__ == '__main__':
    app.run(debug=True)
