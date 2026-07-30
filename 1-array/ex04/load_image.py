import imageio.v3 as iio
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """Load an image and return its pixels as an RGB NumPy array."""
    try:
        im = iio.imread(path)
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {path}")
    except Exception as e:
        raise ValueError(f"Cannot load image '{path}': {e}")
    print(f"The shape of image is: {im.shape}")
    return im
