
import numpy as np
import matplotlib.pyplot as plt
from geopy.distance import geodesic
from shapely.geometry import Polygon
from shapely.ops import transform
from functools import partial
import pyproj

def plot_values(dist_array, avg):
    fig, ax1 = plt.subplots()
                    #start,stop,step
    t = np.arange(1.00, 63.0, 1.00)
    #s1 = np.exp(t)
    s1 = np.array(dist_array)
    s2 = np.array([avg for i in range(1,63)])
    ax1.plot(t, s1, 'b-', label='pairwise_distance_per_day')
    ax1.plot(t, s2, 'r--', label='avg_pairwise_distance')
    ax1.set_xlabel('days', fontsize='x-large')
    # Make the y-axis label, ticks and tick labels match the line color.
    ax1.set_ylabel('pairwise distance', color='b', fontsize='x-large')
    ax1.tick_params('y', colors='b')
    legend = ax1.legend(loc='upper right', shadow=True, fontsize='x-large')
    ax1.set_title('Duomo', fontsize='x-large')

    fig.tight_layout()
    plt.show()



def pw_dist(a, b, da):
    dst = geodesic(a, b).meters
    da.append(dst)
    return da

def convex_hull(points):
    polygon = Polygon(points)
    convex_hull_4326 = polygon.convex_hull
    print(convex_hull_4326.wkt)

    project = partial(
        pyproj.transform,
        pyproj.Proj(init='EPSG:4326'),
        pyproj.Proj(init='EPSG:32632'))

    poly_tranform = transform(project, polygon)
    convex_hull = poly_tranform.convex_hull
    chull_area = convex_hull.area
    chull_perimeter = convex_hull.length
    chull = [chull_area, chull_perimeter]
    return chull


def main():
    file = open("duomo_centroids.txt", 'r')
    #Bocconi
    #b = (45.4487489, 9.1909264)
    #Duomo
    #b = (45.4643254, 9.190493)
    #Mean centroid point
    b = (45.459460134814755, 9.193164901461797)
    dst_array = []
    points = []
    lines = file.readlines()
    for line in lines:
        el = line.split(" ")
        #print(el[1][1:], el[2][:-2])
        lon = float(el[1][1:])
        lat = float(el[2][:-2])
        a = (lat, lon)      #geopy uses order lat, lon
        point = (lon, lat)  #shapely uses order lon, lat
        dist_array = pw_dist(a, b, dst_array)
        points.append(point)

    avg = np.mean(dist_array)
    diameter = np.max(dist_array)
    gyration = np.std(dist_array)
    chull = convex_hull(points)

    print("Average pairwise distance is ", avg, " in meters")
    print("Diameter is ", diameter, " in meters")
    print("Gyration is", gyration)
    print("Convex hull area in km^2 ", chull[0]/1000000)
    print("Convex hull perimeter in km ", chull[1]/1000)
    plot_values(dist_array, avg)


if __name__ == '__main__':
    main()