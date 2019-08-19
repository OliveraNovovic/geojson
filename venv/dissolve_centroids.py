import os
import numpy as np
import geopandas as gpd
import matplotlib


def main():
    #/home/olivera/PycharmProjects/geojson/comm_perLoc_perDay
    location = "Duomo"
    newfile = open(location + "_centroids.txt", 'w')
    for i in range(1, 31):
        file = location + "Day" + str(i) + ".geojson"
        path = "/home/olivera/PycharmProjects/geojson/comm_perLoc_perDay/" + file
        print(path)
        geojson_file = gpd.read_file(path)

        dissolve = geojson_file.unary_union
        centroid = dissolve.centroid
        print(centroid.to_wkt())
        newfile.write(centroid.to_wkt() + '\n')

    newfile.close()





if __name__ == '__main__':
    main()