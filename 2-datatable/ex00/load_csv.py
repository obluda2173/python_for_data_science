import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """Load a CSV file, print its dimensions, and return it as a DataFrame."""
    try:
        dataset = pd.read_csv(path)
    except (FileNotFoundError, IsADirectoryError, PermissionError) as e:
        print(f"{type(e).__name__}: {e}")
        return None
    except (pd.errors.EmptyDataError, pd.errors.ParserError,
            UnicodeDecodeError) as e:
        print(f"{type(e).__name__}: {e}")
        return None
    except (ValueError) as e:
        print(f"{type(e).__name__}: {e}")
        return None
    print(f"Loading dataset of dimensions {dataset.shape}")
    return dataset
