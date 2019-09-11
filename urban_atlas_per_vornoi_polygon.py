import json
import geopandas as gpd
import shapely
import geopy



def main():
    #Milano Vornoi polygons network
    vornoi = "/home/olivera/Documents/milano-vornoi-network.geojson"
    #Urban Atlas Milano
    urban_atlas = "/home/olivera/Documents/Milano-grid-UA-extend-dissolve-geojson.geojson"
    #Urban Atlas intersect vornoi polygons
    ua_vornoi = "/home/olivera/Documents/ua_intersect_vornoi_geojson.geojson"
    for i in range(1, 314):
        with open(ua_vornoi, 'r') as f:
            data = json.load(f)
            for feature in data['features']:
                v_land_use_class = feature['properties']['ITEM2012']
                v_cid = feature['properties']['cid']
                v_area = feature['properties']['area_land_use']
                if v_cid==i:
                    print(v_land_use_class, v_cid, v_area)





if __name__ == '__main__':
     main()