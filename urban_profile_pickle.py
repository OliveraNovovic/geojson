import numpy as np
import pandas as pd

def testdf():
    ZEROS = np.zeros((4,4), dtype=np.int)

    df = pd.DataFrame(ZEROS,  columns=['A1','B1','C1','D1'])

    df.loc[2,'C1'] = 32
    print(df)

def main():
    #testdf()

    pd.set_option('display.max_columns', 999)

    attr_table = "/home/olivera/Documents/data/milano-ua-attr-table.xls"
    df = pd.read_excel(attr_table)
    land_use_list = []
    for item in df['ITEM2012']:
        if item not in land_use_list:
            land_use_list.append(item)

    urban_profile_df = pd.DataFrame(index=range(1, 314), columns=land_use_list)
    urban_profile_df.fillna(0)
    #urban_profile_df.loc[1, 'Pastures'] = 555

    for i in range(1, 314):
        file = open("/home/olivera/Documents/data/land_use_profiles/poly_" + str(i) + ".csv", 'r')
        lines = file.readlines()[1:] #skip the header
        for line in lines:
            el = line.split(';')
            item2012 = el[0]
            cid = int(el[1])
            area = el[2]
            perc = round(float(el[3]), 2)
            print(perc)
            urban_profile_df.loc[cid, item2012] = perc


        file.close()

    print(urban_profile_df)




if __name__=='__main__':
    main()