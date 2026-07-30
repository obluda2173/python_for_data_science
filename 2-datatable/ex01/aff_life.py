from load_csv import load
import matplotlib.pyplot as plt


def main():
    df = load("life_expectancy_years.csv")
    df = df.set_index("country")

    row = df.loc["Austria"]
    row.index = row.index.astype(int)
    row.plot()

    plt.title("Austria Life expectancy projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.show()


if __name__ == "__main__":
    main()
