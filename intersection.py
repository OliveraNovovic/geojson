import json
import matplotlib.pyplot as plt
import numpy as np

def normalized(array):
    max = np.max(array)
    norm_array = []
    for el in array:
        norm_array.append(el/max)
    #print(norm_array)
    return np.std(norm_array)

def plot_values(dist_array):
    fig, ax1 = plt.subplots()
                    #start,stop,step
    stop = len(dist_array) + 1
    t = np.arange(1.00, stop, 1.00)
    #s1 = np.exp(t)
    s1 = np.array(dist_array)
    ax1.plot(t, s1, 'b-', label='intersection area between clusters by day')
    ax1.set_xlabel('number of intersection between sequential days', fontsize='x-large')
    # Make the y-axis label, ticks and tick labels match the line color.
    ax1.set_ylabel('intersection area', color='b', fontsize='x-large')
    ax1.tick_params('y', colors='b')
    legend = ax1.legend(loc='upper right', shadow=True, fontsize='x-large')
    ax1.set_title('Duomo', fontsize='x-large')

    fig.tight_layout()
    plt.show()

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def union(lst1, lst2):
    lst3 = lst1
    for l2 in lst2:
        if l2 not in lst1:
            lst3.append(l2)
    return lst3

def jaccard(intersec, uni):
    jaccard_similarity = len(intersec)/len(uni)
    return jaccard_similarity




def main():
    duomo_clusters_sort = "/home/olivera/Documents/FPM_vornoi_results/clusters_Duomo_sort.txt"
    vornoi = "/home/olivera/Documents/milano-vornoi-network-EPSG32632.geojson"
    jaccard_sim_array = []
    intersect_area_array = []
    with open(vornoi, 'r') as f:
        data = json.load(f)
        with open(duomo_clusters_sort, 'r') as dcs:
            lines = dcs.readlines()
            for i in range(0, 61):
                #results = list(map(int, results))
                #results = [int(i) for i in results]

                line1 = lines[i].split(";")[1]
                elems_l1 = line1.split(",")
                l1_int = [int(e) for e in elems_l1]

                line2 = lines[i+1].split(";")[1]
                elems_l2 = line2.split(",")
                l2_int = [int(e) for e in elems_l2]

                intersec = intersection(l1_int, l2_int) #this is intersection between two consecutive days
                #print(intersec)
                uni = union(l1_int, l2_int)
                #print(uni)
                jaccard_sim = jaccard(intersec, uni)
                jaccard_sim_array.append(jaccard_sim)
                #print("Jaccard similarity ", jaccard_sim)
                intersec_area = 0
                for cid in intersec:
                    for feature in data['features']:
                        v_cid = feature['properties']['cid']
                        v_area = feature['properties']['area']
                        if cid==v_cid:
                            #print(cid, v_area)
                            intersec_area = intersec_area + v_area
                intersect_area_array.append(intersec_area)
                #print("Intersection area in m^2 ", intersec_area)



    #print("Intersection array length ", len(intersect_area_array))
    #print("Jaccard similarity array length ", len(jaccard_sim_array))
    print("St. dev. of intersection array ", np.std(intersect_area_array))
    print("Mean of intersection area ", np.mean(intersect_area_array))
    print("St. dev. of Jaccard similarity array ", np.std(jaccard_sim_array))
    print("Mean of Jaccard similarity ", np.mean(jaccard_sim_array))
    #don't perform normalization for now...
    #print("St. dev. of intersection array (normalized) ", normalized(intersect_area_array))
    #print("St. dev. of Jaccard similarity array (normalized) ", normalized(jaccard_sim_array))

    plot_values(intersect_area_array)
    #plot_values(jaccard_sim_array)



if __name__ == '__main__':
    main()
