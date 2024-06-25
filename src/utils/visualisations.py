from matplotlib import pyplot as plt
import numpy as np

def overlay_pixel_intensity_values(image: np.ndarray, font_size: int = 6) -> None:
    """
    Overlays pixel intensity values on a given grayscale image.

    Parameters:
    image (np.ndarray): 2D array representing a grayscale image with pixel values.
    font_size (int): Size of the font to use for overlaying text. Default is 6.

    Returns:
    None
    """
        # Validate inputs
    if not isinstance(image, np.ndarray):
        raise TypeError("The 'image' parameter must be a numpy.ndarray.")
    if not isinstance(font_size, int):
        raise TypeError("The 'font_size' parameter must be an integer.")
    # Create a figure and axis
    fig, ax = plt.subplots()

    # Display the image
    ax.imshow(image, cmap='gray', vmin=0, vmax=255)

    # Loop through each pixel in the image
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            # Add text annotation with pixel value
            ax.text(j, i, str(image[i, j]), color='red', ha='center', va='center', fontsize=font_size)

    # Remove axis ticks
    ax.axis("off")

    # Show the plot
    plt.show()

