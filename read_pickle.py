import pandas as pd


def main():
    df = pd.read_pickle("land_use_pickled.pkl")
    print(df)

if __name__ == '__main__':
    main()