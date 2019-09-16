import pandas as pd


def lu_percentage(df_subs):
    total_area = df_subs['area_land_use'].sum()
    df_subs.insert(3, "perc", (df_subs['area_land_use'] / total_area) * 100)
    return df_subs


def main():
    # Milano Vornoi polygons network
    vornoi = "/home/olivera/Documents/data/milano-vornoi-network.geojson"
    # Urban Atlas Milano
    urban_atlas = "/home/olivera/Documents/data/Milano-grid-UA-extend-dissolve-geojson.geojson"
    # Urban Atlas intersect vornoi polygons
    ua_vornoi = "/home/olivera/Documents/data/ua_intersect_vornoi_geojson.geojson"

    # urban atlas intersect vornoi polygons attribute table
    attr_table = "/home/olivera/Documents/data/milano-ua-attr-table.xls"
    df = pd.read_excel(attr_table)

    pd.set_option('display.max_columns', 999)

    for i in range(1, 314):
        df_subs = df[df.cid == i]
        # get the row of max area value
        max_area_row = df_subs.loc[df_subs['area_land_use'].idxmax()]
        land_use = max_area_row['ITEM2012']
        # print(land_use)
        # print(df_subs)
        new_df = lu_percentage(df_subs)
        #writing files for each polygon it's land use profile
        new_df.to_csv("/home/olivera/Documents/data/land_use_profiles/poly_" + str(i) + ".csv", index=False, sep=';')



if __name__ == '__main__':
    main()
