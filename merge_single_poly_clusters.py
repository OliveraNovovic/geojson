



def main():
    nov = "/home/olivera/Documents/FPM_vornoi_results/clusters_per_vpoly_sort_november"
    dec = "/home/olivera/Documents/FPM_vornoi_results/clusters_per_vpoly_sort_december"
    for i in range(1, 314):
        new_file = open("/home/olivera/Documents/data/clusters_vpoly_" + str(i) + ".txt", 'w')
        first_file = nov + "/clusters_vpoly_nov_" + str(i) + "_sort.txt"
        with open(first_file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                new_file.write(line)

        second_file = dec + "/clusters_vpoly_dec_" + str(i) + "_sort.txt"
        with open(second_file, 'r') as r:
            linesr = r.readlines()
            for line in linesr:
                new_file.write(line)


    new_file.close()



if __name__=='__main__':
    main()