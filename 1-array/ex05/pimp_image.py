import numpy as np
import matplotlib.pyplot as plt


def _display(image, cmap=None) -> None:
    plt.imshow(image, cmap=cmap)
    plt.show()


def ft_invert(array) -> np.ndarray:
    """Inverts the color of the image received."""
    out = 255 - array
    _display(out)
    return out


def ft_red(array) -> np.ndarray:
    """Applies a red filter to the image received."""
    out = array.copy()
    out[:, :, 1] = out[:, :, 1] * 0
    out[:, :, 2] = out[:, :, 2] * 0
    _display(out)
    return out


def ft_green(array) -> np.ndarray:
    """Applies a green filter to the image received."""
    out = array.copy()
    out[:, :, 0] = out[:, :, 0] - out[:, :, 0]
    out[:, :, 2] = out[:, :, 2] - out[:, :, 2]
    _display(out)
    return out


def ft_blue(array) -> np.ndarray:
    """Applies a blue filter to the image received."""
    out = array.copy()
    out[:, :, 0] = 0
    out[:, :, 1] = 0
    _display(out)
    return out


def ft_grey(array) -> np.ndarray:
    """Applies a greyscale filter to the image received."""
    grey = array.sum(axis=2) / 3
    _display(grey, cmap="gray")
    return grey
