
import numpy as np
import matplotlib.pyplot as plt
from geopy.distance import geodesic

def plot_values(dist_array, avg):
    fig, ax1 = plt.subplots()
                    #start,stop,step
    t = np.arange(1.00, 31.0, 1.00)
    #s1 = np.exp(t)
    s1 = np.array(dist_array)
    s2 = np.array([avg for i in range(1,31)])
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


def main():
    file = open("Duomo_centroids.txt", 'r')
    #Bocconi
    #b = (45.4487489, 9.1909264)
    #Duomo
    b = (45.4643254, 9.190493)
    dst_array = []
    lines = file.readlines()
    for line in lines:
        el = line.split(" ")
        print(el[1][1:], el[2][:-2])
        lon = float(el[1][1:])
        lat = float(el[2][:-2])
        a = (lat, lon)
        dist_array = pw_dist(a, b, dst_array)

    avg = np.mean(dist_array)
    diameter = np.max(dist_array)
    print(dist_array)
    print(avg, diameter)
    plot_values(dist_array, avg)


if __name__ == '__main__':
    main()