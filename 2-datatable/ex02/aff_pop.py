import matplotlib.pyplot as plt
import numpy as np
from load_csv import load


SCALES = ((1e9, "B"), (1e6, "M"), (1e3, "K"))
SUFFIX = {s: scale for scale, s in SCALES}


def to_float(val):
    if not isinstance(val, str) or not val:
        return np.nan
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
    df = load("population_total.csv").set_index("country")
    pop = df.loc[["Austria", "France"]].map(to_float).T
    pop.index = pop.index.astype(int)
    pop = pop.loc[1800:2050]

    pop.plot()
    plt.title("Population Projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend(loc="lower right")
    plt.gca().yaxis.set_major_formatter(to_string)
    plt.show()


if __name__ == "__main__":
    main()
