# 🧪 Cookiecutter Data Journalism Project Template

This is a reusable project template for story-specific, reproducible, NYT-style data journalism projects using Python, Quarto, and Jupyter. Inspired by workflows from the New York Times, FT, Bloomberg, and The Guardian.

## 📁 Project Structure

```
{{ cookiecutter.beat }}/{{ cookiecutter.project_name }}/
├── 00_inputs/          # Source HTML, PDFs, docs
├── 01_data/            # Raw/cleaned/sql/geo data
├── 02_scripts/         # Scrapers, wranglers, chart helpers
├── 03_notebooks/       # Exploratory analysis + chart creation
├── 04_outputs/         # Final exports: charts, tables, video
├── 05_publish/         # Quarto or web output
├── 06_story/           # Draft text + notes
├── 07_assets/          # Fonts, logos, backgrounds
└── config/             # pyproject.toml, quarto.yml, .env
```

## 🚀 Usage

1. Install cookiecutter:

```bash
pip install cookiecutter
```

2. Generate a new story project:

```bash
cookiecutter gh:yourusername/cookiecutter-data-story
```

3. Follow prompts:
- `project_name`: crude_price_update
- `beat`: economy
- `description`: Daily India petrol price tracker

4. Activate environment and get started:

```bash
cd economy/crude_price_update
uv init
uv sync --upgrade
source .venv/bin/activate
```

## ✨ Included Features

- `style_config.py`: Preloaded NYT-style chart style
- `chart_helpers.py`: Reusable chart functions with headline/subhead/date
- `cache.py`: Simple hash-based caching of charts
- `pyproject.toml`: All required Python dependencies
- `quarto.yml`: Config for Quarto HTML output
- `jupyterlab` + `matplotlib` ready

## 🖼 Example Chart Output

```python
nyt_line_chart(
    df=df,
    x="date",
    y="price",
    headline="India’s Petrol Prices Are Rising",
    subhead="Metro average per litre, Jan 2022–May 2025",
    output_path=Path("04_outputs/charts/petrol_prices_trend.png")
)
```

## 📝 License

MIT — free to adapt for your own newsroom or data desk.