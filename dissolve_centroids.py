import os
import numpy as np
import geopandas as gpd
import matplotlib


def main():
    #/home/olivera/PycharmProjects/geojson/comm_perLoc_perDay
    # location = "Duomo"
    # newfile = open(location + "_centroids.txt", 'w')
    # for i in range(1, 31):
    #     file = location + "Day" + str(i) + ".geojson"
    #     path = "/home/olivera/PycharmProjects/geojson/comm_perLoc_perDay/" + file
    #     print(path)
    #     geojson_file = gpd.read_file(path)
    #
    #     dissolve = geojson_file.unary_union
    #     centroid = dissolve.centroid
    #     print(centroid.to_wkt())
    #     newfile.write(centroid.to_wkt() + '\n')
    #
    # newfile.close()

    for i in range(1, 314):
        vpoly = "vpoly_" + str(i)
        newfile = open("vpoly_centroids/" + vpoly + ".txt", 'w')
        folder_path = "/home/olivera/Documents/data/vpoly_single_clusters/"

        date = ["nov01", "nov02", "nov03", "nov04", "nov05", "nov06", "nov07", "nov08",
                "nov09", "nov10", "nov11", "nov12", "nov13", "nov14", "nov15",
                "nov16", "nov17", "nov18", "nov19", "nov20", "nov21", "nov22",
                "nov23", "nov24", "nov25", "nov26", "nov27", "nov28", "nov29",
                "nov30", "dec01", "dec02", "dec03", "dec04", "dec05", "dec06",
                "dec07", "dec08", "dec09", "dec10", "dec11", "dec12", "dec13",
                "dec14", "dec15", "dec16", "dec17", "dec18", "dec19", "dec20",
                "dec21", "dec22", "dec23", "dec24", "dec25", "dec26", "dec27",
                "dec28", "dec29", "dec30", "dec31", "jan01"]
        #for file in os.listdir(folder_path):
        for d in date:
            vpoly_cluster = folder_path + vpoly + "_" + d + ".geojson"
            geojson_file = gpd.read_file(vpoly_cluster)
            dissolve = geojson_file.unary_union
            centroid = dissolve.centroid
            print(centroid.to_wkt())
            newfile.write(centroid.to_wkt() + '\n')

        newfile.close()






if __name__ == '__main__':
    main()