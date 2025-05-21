from matplotlib import rcParams
from pathlib import Path

def load_custom_fonts():
    from matplotlib import font_manager
    font_dir = Path(__file__).parents[2] / "07_assets" / "fonts"
    font_files = font_manager.findSystemFonts(fontpaths=[font_dir])
    for font in font_files:
        font_manager.fontManager.addfont(font)
    rcParams['font.family'] = 'Roboto Condensed'

NYT_COLORS = {
    "black": "#000000",
    "gray": "#666666",
    "blue": "#1f77b4",
    "red": "#d62728"
}

def apply_nyt_style():
    rcParams.update({
        "axes.facecolor": "white",
        "axes.edgecolor": "white",
        "axes.labelcolor": NYT_COLORS["black"],
        "xtick.color": NYT_COLORS["gray"],
        "ytick.color": NYT_COLORS["gray"],
        "figure.figsize": (9, 6),
        "axes.titleweight": "bold",
        "axes.titlesize": 18,
        "axes.labelsize": 12,
        "font.size": 12,
        "figure.dpi": 300
    })