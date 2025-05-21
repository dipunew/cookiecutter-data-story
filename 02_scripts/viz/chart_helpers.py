import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from .style_config import apply_nyt_style, load_custom_fonts

def nyt_line_chart(df, x, y, headline="", subhead="", date_fmt="%b %Y", output_path=None):
    load_custom_fonts()
    apply_nyt_style()

    fig, ax = plt.subplots()
    ax.plot(df[x], df[y], color="#1f77b4", linewidth=2.5)

    ax.set_title(headline, loc="left", pad=20)
    ax.text(0, 1.05, subhead, transform=ax.transAxes, fontsize=12, ha='left', va='center', color="#666666")

    ax.xaxis.set_major_formatter(DateFormatter(date_fmt))
    ax.spines[['top', 'right', 'left', 'bottom']].set_visible(False)
    ax.tick_params(axis='both', which='both', length=0)
    ax.grid(False)

    plt.tight_layout()
    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()