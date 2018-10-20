import netCDF4 as netCDF4
import numpy as np
import datetime
import matplotlib.pyplot as plt


def getLatitudeAsIndex(lat):
    latitudeInit = -45.625
    latitudeAsIndex = 0
    while latitudeInit <= -0.125:
        if lat == latitudeInit:
            return latitudeAsIndex
        else:
            latitudeAsIndex += 1
            latitudeInit = latitudeInit + 0.25


def getLongitudeAsIndex(lon):
    longitudeInit = -83.625
    longitudeAsIndex = 0
    while longitudeInit <= 179.875:
        if lon == longitudeInit:
            return longitudeAsIndex
        else:
            longitudeAsIndex += 1
            longitudeInit = longitudeInit + 0.25


def getPrecipitation(lat, lon, date):
    path = ("./3B42_Daily." + date + ".7.nc4.nc4")
    dataset = netCDF4.Dataset(path)
    return (dataset.variables['precipitation'][getLongitudeAsIndex(lon)][getLatitudeAsIndex(lat)])


# 2017-07-30 to 2018-07-30
def parseDates(y, m, d):
    date = datetime.date(y, m, d)
    for i in range(366):
        date += datetime.timedelta(days=1)
        print(date.strftime("%Y%m%d"))


def formatDate(y, m, d):
    y = str(y)
    if (m < 10):
        m = "0" + str(m)
    else:
        m = str(m)
    if (d < 10):
        d = "0" + str(d)
    else:
        d = str(d)
    return(y+m+d)


def preciptFilter(x):
    return x > 1

# print(formatDate(2017, 7, 30))


array = list()
array.append(getPrecipitation(-1.375, -48.625, "20170730"))
array.append(getPrecipitation(-1.375, -48.625, "20170731"))
array.append(getPrecipitation(-1.375, -48.625, "20170801"))
array.append(getPrecipitation(-1.375, -48.625, "20170802"))
array.append(getPrecipitation(-1.375, -48.625, "20170803"))
array.append(getPrecipitation(-1.375, -48.625, "20170804"))
array.append(getPrecipitation(-1.375, -48.625, "20170805"))
array.append(getPrecipitation(-1.375, -48.625, "20170806"))

# drenagem
# rochoso < 20
# argila 20-30
# argila arenosa 30-70
# areia fina 70-140
# cascalhos > 140

# escoamento = (precipitacao - 0.2 * drenagem)²/(precipitacao - 0.2*drenagem + drenagem)
# se precipitacao > 0.2 * drenagem


def calcRunoffCurve(preciptation, soilRunoff):
    flowIntensity = 0
    initialLoss = 0.2 * soilRunoff
    if preciptation <= (initialLoss):
        return flowIntensity
    else:
        flowIntensity = (preciptation - (initialLoss)) / \
            ((preciptation-(initialLoss))+soilRunoff)


print(np.mean(array))
print(np.median(array))


# usar numero de habitante para fazer calculo de gasto com correçao
# receber input de capacidade de escoamento do solo para ver quantas vezes chove mais que a capacidade
# receber area da cidade para calcular o preço da obra
# calcular o preço da obra
# calcular retorno por investimento com preço da obra e calculo de gasto com correçao


res = list(filter(lambda x: x > 1, array))
print(res)


# plot graphics
# plt.plot(array)
# plt.ylabel('precipt')
# plt.xlabel('day')
# plt.show()


# x = map(preciptFilter, array)
# print(x)
# # print (dataset.file_format)
# # print (dataset.dimensions.keys())
# # print (dataset.variables.keys())
# k = 0
# count = 0
# for k in range(100):
#     a = (dataset.variables['precipitation'][k][:])
#     rounded = numpy.round(a, 2)
#     count += 1
#     print("linha", count, "valor", rounded)

# print (count)
#
# a = (dataset.variables['precipitation'][73][:])


# # k = dataset.dimensions.keys()
# # print(k)
# # f = open('test_logs.txt', 'a+')
# # f.write(str(k))
