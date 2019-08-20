

def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3



def main():
    duomo_clusters_sort = "/home/olivera/Documents/FPM_vornoi_results/clusters_Duomo_sort.txt"
    with open(duomo_clusters_sort, 'r') as dcs:
        lines = dcs.readlines()
        for i in range(0, 2):
            #results = list(map(int, results))
            #results = [int(i) for i in results]

            line1 = lines[i].split(";")[1]
            elems_l1 = line1.split(",")
            l1_int = [int(e) for e in elems_l1]

            line2 = lines[i+1].split(";")[1]
            elems_l2 = line2.split(",")
            l2_int = [int(e) for e in elems_l2]

            print(l1_int)
            print(l2_int)

            intersec = intersection(l1_int, l2_int)
            print(intersec)





if __name__ == '__main__':
    main()
