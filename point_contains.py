from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import json

def area(cid):
    #vornoi polygons with area EPSG 32632
    vornoi_network_epsg_32632 = "/home/olivera/Documents/milano-vornoi-network-EPSG32632.geojson"

    with open(vornoi_network_epsg_32632, 'r') as f:
        data = json.load(f)
        for feature in data['features']:
            v_cid = feature['properties']['cid']
            poly_area = feature['properties']['area']
            if v_cid == cid:
                return poly_area



def osm_points_num(poly):
    #osm points with coordinates
    osm_points = "/home/olivera/Documents/milano-osm_points.geojson"
    #counter of points
    point_count = 0
    with open(osm_points, 'r') as f:
        data = json.load(f)
        for feature in data['features']:
            points = feature['geometry']['coordinates']
            p = Point(points)
            contains = poly.contains(p)
            if contains:
                point_count += 1
    return point_count


def main():
    #vornoi_network no area epsg 4326
    vornoi_network_4326 = "/home/olivera/Documents/milano-vornoi-network.geojson"

    #write results to file
    wfile = open('osm_points_per_vornoi_poly.csv', 'w')
    wfile.write("cid,area_poly,osm_points_per_poly,poi_density" + '\n') #header

    #Bocconi
    b = Point(9.1909264, 45.4487489)
    with open(vornoi_network_4326, 'r') as f:
        data = json.load(f)
        for feature in data['features']:
            points = []
            cid = feature['properties']['cid']
            geom = feature['geometry']['coordinates']
            geom_str = str(geom)[3:-3]
            elem = geom_str.split('],')
            for e in elem:
                coords = e.split(', ')
                lon = float(coords[0].strip(' ['))
                lat = float(coords[1].strip(']'))
                p = (lon, lat)  # shapely uses order lon, lat
                points.append(p)
            poly = Polygon(points)
            osm_points_per_poly = osm_points_num(poly)
            area_poly = area(cid) #area of vornoi polygon in m^2
            poi_density = osm_points_per_poly/area_poly
            print(cid, area_poly, osm_points_per_poly, poi_density)
            wfile.write(str(cid) + ',' + str(area_poly) + ',' +
                        str(osm_points_per_poly) + ',' + str(poi_density) + '\n')

    wfile.close()




if __name__ == '__main__':
    main()