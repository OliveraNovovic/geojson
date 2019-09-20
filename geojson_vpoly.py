import json
from json import dump
import os



def main():
    #Milano Vornoi polygons network
    vornoi = "/home/olivera/Documents/data/milano-vornoi-network.geojson"
    vpoly_clusters = "/home/olivera/Documents/data/clusters_per_vpoly"

    for i in range(1, 314):
        file = vpoly_clusters + "/clusters_vpoly_" + str(i) + ".txt"
        with open(file, 'r') as d:
            lines = d.readlines()
            for line in lines:
                feature_collection = []
                elem = line.split(';')
                date = elem[0]
                # print(date)
                cluster = elem[1].split(",")
                # print(cluster)
                for cid in cluster:
                    with open(vornoi, 'r') as f:
                        data = json.load(f)
                        for feature in data['features']:
                            v_cid = feature['properties']['cid']
                            print(v_cid)
                            if v_cid == int(cid.strip()):
                                print("yeeees")
                                feature_collection.append(feature)
                print(feature_collection)

                newjsonfile = 'vpoly_single_clusters/' + 'vpoly_' + str(i) + '_' + str(date) + '.geojson'
                with open(newjsonfile, 'w') as f:
                    f.write("{" + '\n' +
                            '"type": "FeatureCollection",' + '\n' +
                            '"name": "myfile",' + '\n' +
                            '"crs": {"type": "name", "properties": {"name": "urn:ogc:def:crs:OGC:1.3:CRS84"}},' + '\n' +
                            '"features":' + '\n')
                    dump(feature_collection, f)
                    f.write("}")





if __name__=='__main__':
    main()