# -*- coding: utf-8 -*-
"""
Display one representative image for each of the 8 Tusayan White Ware types
in a 4-row by 2-column panel.

Data source: Pawlowicz & Downum (2021) - Single_Sherd_8_Type_Analyzer dataset.
"""

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import warnings

# Suppress harmless deprecation warnings for older image formats
warnings.filterwarnings("ignore", category=UserWarning)

# Base directory for the reference images
BASE_DIR = "data/Single_Sherd_8_Type_Analyzer/Reference_Database/Reference_Images"

# One representative image filename for each of the 8 Tusayan White Ware types.
# These were selected from the Reference_Images directory that was extracted
# from the Zenodo supplemental data (Single_Sherd_8_Type_Analyzer.zip).
TYPE_IMAGES = {
    "Black Mesa B/W": "PP_Tusayan_132.jpg",
    "Dogoszhi B/W": "PP_Tusayan_134.jpg",
    "Flagstaff B/W": "PP_Tusayan_136.jpg",
    "Kayenta B/W": "PP_Tusayan_138.jpg",
    "Pueblo II B/W (Tusayan)": "PP_Tusayan_141.jpg",
    "Pueblo III B/W (Tusayan)": "PP_Tusayan_145.jpg",
    "Sosi B/W": "Sosi_1.jpg",
    "Wupatki B/W": "PP_Wupatki_001.jpg",
}

def main():
    # Create a 4×2 grid of subplots
    fig, axes = plt.subplots(nrows=4, ncols=2, figsize=(8, 12))
    fig.suptitle("Eight Tusayan White Ware Types – One Representative Sherd Each", fontsize=14, y=0.98)

    # Flatten the 2D array of axes for easy iteration
    ax_flat = axes.flatten()

    for idx, (type_name, filename) in enumerate(TYPE_IMAGES.items()):
        filepath = os.path.join(BASE_DIR, filename)
        if not os.path.exists(filepath):
            print(f"Warning: {filepath} not found; skipping {type_name}")
            ax_flat[idx].set_visible(False)
            continue

        img = mpimg.imread(filepath)
        ax_flat[idx].imshow(img)
        ax_flat[idx].set_title(type_name, fontsize=10)
        ax_flat[idx].axis("off")

    # Hide any unused subplots (if any image was missing)
    for idx in range(len(TYPE_IMAGES), len(ax_flat)):
        ax_flat[idx].set_visible(False)

    # Adjust layout and display
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

if __name__ == "__main__":
    main()