# import pyproj

# WGS84 = pyproj.CRS("EPSG:4326")
# BGS2005 = pyproj.CRS("EPSG:7801")
#### SR-ORG:8577 #### https://spatialreference.org/ref/sr-org/bgs2005/
#### BGS2005 = pyproj.CRS('PROJCS["BGS2005",GEOGCS["GCS_GRS_1980",DATUM["D_GRS_1980",SPHEROID["GRS_1980",6378137.0,298.257222101]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]],PROJECTION["Lambert_Conformal_Conic"],PARAMETER["False_Easting",500000.0],PARAMETER["False_Northing",4725824.3591],PARAMETER["Central_Meridian",25.5],PARAMETER["Standard_Parallel_1",42.0],PARAMETER["Standard_Parallel_2",43.33333333333334],PARAMETER["Scale_Factor",1.0],PARAMETER["Latitude_Of_Origin",42.6678756833],UNIT["Meter",1.0]]')
debug = True

PATHS_CONFIG = {
    "dirSource": "C:/Users/User/PycharmProjects/cadparser/input/",
    "dirOutput": "C:/Users/User/PycharmProjects/cadparser/output/",
    "dirBase": "C:/Users/User/PycharmProjects/cadparser/",
    "dirArchive": "C:/Users/User/PycharmProjects/cadparser/archive/",
    "errorpage": "https://cadtodxf.com/error"
}

WGS84 = "EPSG:4326"
BGS2005 = "EPSG:7801"
BGS2005WKT = 'PROJCS["BGS2005",' \
             'GEOGCS["GCS_GRS_1980",' \
             'DATUM["D_GRS_1980",' \
             'SPHEROID["GRS_1980",6378137.0,298.257222101]],' \
             'PRIMEM["Greenwich",0.0],' \
             'UNIT["Degree",0.0174532925199433]],' \
             'PROJECTION["Lambert_Conformal_Conic"],' \
             'PARAMETER["False_Easting",500000.0],' \
             'PARAMETER["False_Northing",4725824.3591],' \
             'PARAMETER["Central_Meridian",25.5],' \
             'PARAMETER["Standard_Parallel_1",42.0],' \
             'PARAMETER["Standard_Parallel_2",43.33333333333334],' \
             'PARAMETER["Scale_Factor",1.0],' \
             'PARAMETER["Latitude_Of_Origin",42.6678756833],' \
             'UNIT["Meter",1.0]]'
