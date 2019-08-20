import json
from json import dump
import os

def mygeojsonfile(day, comm_file, loc_name):
    feature_collection = []
    with open(comm_file, 'r') as commread:
        line = commread.readlines()[day - 1]
        print(line)
        cs = []
        el = line.split(',')
        for e in el:
            cs.append(int(e.strip()))

        #print(cs)
        comm_set = cs
    # comm_set = (3855, 3655, 4255, 3455, 4056, 3456, 4256, 3656, 3856, 3857, 4257, 4057, 3657, 3457, 3858, 3658, 4058, 3258, 4258, 3458, 3859, 3259, 3459, 3059, 3659, 4259, 4059, 3460, 3260, 3060, 4060, 3660, 3860, 4260, 2860, 3261, 3461, 3661, 3061, 3861, 4061, 3462, 3662, 3262, 3862, 4062, 1934, 4154, 4155, 3955, 3555, 3755, 3556, 4156, 3756, 3356, 3956, 3957, 3757, 3557, 4157, 3357, 3558, 4158, 3958, 3758, 3358, 3959, 4159, 2959, 3759, 3359, 3559, 3159, 4160, 3760, 3160, 2960, 3560, 3360, 3960, 3161, 2961, 3961, 3361, 3561, 4161, 3761, 3362, 3962, 3162, 3762, 3963)
    with open('milano-grid.geojson', 'r') as f:
        data = json.load(f)
        for feature in data['features']:
            cellid = feature['properties']['cellId']
            # print(cellid)
            # print(feature)
            # print(comm_set)
            if cellid in comm_set:
                # print("zeeeeeah")
                # print(feature)
                feature_collection.append(feature)

        newjsonfile = 'comm_perLoc_perDay/' + loc_name + 'Day' + str(day) + '.geojson'
        #'BocconiDay' + str(day) + '.geojson'
        with open(newjsonfile, 'w') as f:
            f.write("{" + '\n' +
                    '"type": "FeatureCollection",' + '\n' +
                    '"name": "myfile",' + '\n' +
                    '"crs": {"type": "name", "properties": {"name": "urn:ogc:def:crs:OGC:1.3:CRS84"}},' + '\n' +
                    '"features":' + '\n')
            dump(feature_collection, f)
            f.write("}")


def main():
    #Milano Vornoi polygons network
    vornoi = "/home/olivera/Documents/milano-vornoi-network.geojson"
    #/home/olivera/Documents/FPM_vornoi_results
    duomo_clusters = "/home/olivera/Documents/FPM_vornoi_results/clusters_Duomo.txt"

    with open(duomo_clusters, 'r') as d:
        lines = d.readlines()
        for line in lines:
            feature_collection = []
            elem = line.split(';')
            date = elem[0]
            #print(date)
            cluster = elem[1].split(",")
            #print(cluster)
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

            newjsonfile = 'duomo_single_clusters/' + 'duomo_' + str(date) + '.geojson'
            with open(newjsonfile, 'w') as f:
                f.write("{" + '\n' +
                        '"type": "FeatureCollection",' + '\n' +
                        '"name": "myfile",' + '\n' +
                        '"crs": {"type": "name", "properties": {"name": "urn:ogc:def:crs:OGC:1.3:CRS84"}},' + '\n' +
                        '"features":' + '\n')
                dump(feature_collection, f)
                f.write("}")



if __name__ == '__main__':
    main()
