import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator
import numpy as np
import pandas as pd
from load_csv import load


SCALES = ((1e9, "B"), (1e6, "M"), (1e3, "K"))
SUFFIX = {s: scale for scale, s in SCALES}


def to_float(val):
    if isinstance(val, (int, float)):
        return float(val)
    if not isinstance(val, str) or not val.strip():
        return np.nan
    val = val.strip()
    scale = SUFFIX.get(val[-1].upper())
    try:
        return float(val) if scale is None else float(val[:-1]) * scale
    except ValueError:
        return np.nan


def to_string(x, _pos=None):
    for scale, suffix in SCALES:
        if abs(x) >= scale:
            return f"{x / scale:g}{suffix}"
    return f"{x:g}"


def main():
    gdp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life = load("life_expectancy_years.csv")
    year = "1900"

    df = pd.DataFrame({
        "gdp": gdp.set_index("country")[year].map(to_float),
        "life": life.set_index("country")[year].map(to_float),
    }).dropna()

    plt.scatter(df["gdp"], df["life"], label=year)
    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")

    plt.xscale("log")
    ax = plt.gca()
    ax.xaxis.set_major_locator(FixedLocator([300, 1000, 10000]))
    plt.gca().xaxis.set_major_formatter(to_string)

    plt.show()


if __name__ == "__main__":
    main()
