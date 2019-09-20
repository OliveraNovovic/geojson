

def find_line(date, duomo_clusters, wfile):
    with open(duomo_clusters, 'r') as dc:
        lines = dc.readlines()
        for line in lines:
            elem = line.split(";")
            ddate = elem[0]
            cluster = elem[1]
            if ddate==date:
                wfile.write(ddate + ';' + cluster)



def main():
    path = "/home/olivera/Documents/FPM_vornoi_results"
    for i in range(1, 314):
        nov = "/clusters_per_vpoly_november/clusters_vpoly_" + str(i) + "_november.txt"
        dec = "/clusters_per_vpoly_december/clusters_vpoly_" + str(i) + "_december.txt"
        vpoly_clusters = path + dec
        vpoly_clusters_sort = path + "/clusters_vpoly_dec_" + str(i) + "_sort.txt"
        wfile = open(vpoly_clusters_sort, 'w')
        for i in range(1, 31):
            if i<10:
                date = "nov0" + str(i)
                find_line(date, vpoly_clusters, wfile)
            else:
                date = "nov" + str(i)
                find_line(date, vpoly_clusters, wfile)

        for i in range(1, 32):
            if i<10:
                date = "dec0" + str(i)
                find_line(date, vpoly_clusters, wfile)
            else:
                date = "dec" + str(i)
                find_line(date, vpoly_clusters, wfile)

        date = "jan01"
        find_line(date, vpoly_clusters, wfile)

    wfile.close()




if __name__ == '__main__':
    main()