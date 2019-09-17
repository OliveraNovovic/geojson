import pandas as pd


def main():
    df = pd.read_pickle("/home/olivera/Documents/data/urban_profile.pkl")
    print(df)

if __name__ == '__main__':
    main()