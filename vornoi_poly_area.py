import json
from json import dump
import os



def main():
    #Milano Vornoi polygons network
    vornoi = "/home/olivera/Documents/milano-vornoi-network-EPSG32632.geojson"
    with open(vornoi, 'r') as f:
        data = json.load(f)
        for feature in data['features']:
            v_cid = feature['properties']['cid']
            v_area = feature['properties']['area']
            v_perimetar = feature['properties']['perimeter']
            v_poly_geom = feature['geometry']
            print(v_cid, v_area, v_perimetar)
            print(v_poly_geom)



if __name__ == '__main__':
    main()