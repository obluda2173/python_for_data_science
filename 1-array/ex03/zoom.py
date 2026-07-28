import matplotlib.pyplot as plt
from load_image import ft_load


def main():
    try:
        im = ft_load("animal.jpg")
        print(im)

        cy, cx = 300, 650
        h, w = 400, 400
        r0, c0 = cy - h // 2, cx - w // 2
        if r0 < 0 or c0 < 0 or r0 + h > im.shape[0] or c0 + w > im.shape[1]:
            raise ValueError(f"crop at ({cy},{cx}) exceeds image {im.shape[:2]}")

        im = im[r0:r0 + h, c0:c0 + w, :1]
        print(f"New shape after slicing: {im.shape}")
        print(im)

        plt.imshow(im[:, :, 0], cmap="gray")
        plt.show()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
