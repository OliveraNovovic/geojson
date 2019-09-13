
import pandas as pd



def main():
    #Milano Vornoi polygons network
    vornoi = "/home/olivera/Documents/data/milano-vornoi-network.geojson"
    #Urban Atlas Milano
    urban_atlas = "/home/olivera/Documents/data/Milano-grid-UA-extend-dissolve-geojson.geojson"
    #Urban Atlas intersect vornoi polygons
    ua_vornoi = "/home/olivera/Documents/data/ua_intersect_vornoi_geojson.geojson"

    #urban attlas intersect vornoi polygons attribute table
    attr_table = "/home/olivera/Documents/data/milano-ua-attr-table.xls"
    df = pd.read_excel(attr_table)

    for i in range(1, 314):
        df_subs = df[df.cid == i]
        # get the row of max area value
        max_area_row = df_subs.loc[df_subs['area_land_use'].idxmax()]
        land_use = max_area_row['ITEM2012']
        print(land_use)


if __name__ == '__main__':
     main()