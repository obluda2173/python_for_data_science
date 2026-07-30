import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load


def zoom():
    """Load, crop, keep only the 1st channel, and plot the image."""
    try:
        im = ft_load("animal.jpg")
        print(im)

        cy, cx = 300, 650
        h, w = 400, 400
        r0, c0 = cy - h // 2, cx - w // 2
        if r0 < 0 or c0 < 0 or r0 + h > im.shape[0] or c0 + w > im.shape[1]:
            raise ValueError(f"crop at ({cy},{cx}) exceeds image")

        im = im[r0:r0 + h, c0:c0 + w, :1]

        return im
    except Exception as e:
        print(f"Error: {e}")


def main():
    """Transpose a zoomed image and display its first channel in grayscale."""
    try:
        im = zoom()

        r, c, _ = im.shape
        im_T = [[0 for _ in range(r)] for _ in range(c)]

        for i in range(r):
            for j in range(c):
                im_T[j][i] = im[i][j]

        im_T = np.array(im_T)
        print(f"New shape after Transpose: {im_T.shape}")
        print(im_T)

        plt.imshow(im_T[:, :, 0], cmap="gray")
        plt.show()

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
