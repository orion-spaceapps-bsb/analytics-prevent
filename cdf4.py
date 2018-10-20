import netCDF4 as netCDF4
import numpy
import datetime


def getLatitudeAsIndex(lat):
    latitudeInit = -49.875
    latitudeAsIndex = 0
    while latitudeInit <= -0.125:
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
    path = ("./3B42_Daily.20171231.7.nc4.nc4")
    dataset = netCDF4.Dataset("./3B42_Daily.20171231.7.nc4.nc4")
    return (dataset.variables['precipitation'][lat][lon])


# 2017-07-30 to 2018-07-30
def parseDates():
    date = datetime.date(2017, 7, 29)
    for i in range(366):
        date += datetime.timedelta(days=1)
        print(date.strftime("%Y%m%d"))


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

# # a = (dataset.variables['precipitation'][73][:])
# # print(a[9])


# # k = dataset.dimensions.keys()
# # print(k)
# # f = open('test_logs.txt', 'a+')
# # f.write(str(k))
