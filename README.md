# 🌡️ Drought Risk Forecasting Bavaria

Predicting drought risk in Bavaria using machine learning on climate and hydrology data.

---

## Overview

This project builds a drought risk forecasting system for Bavaria using the **SPEI index** (Standardized Precipitation-Evapotranspiration Index) as target variable. We compare LSTM and Random Forest models and apply SHAP for explainability.

**Research question:**  
*Can we reliably predict short- and medium-term drought risk in Bavaria by combining station-based climate data with gridded reanalysis products?*

---

## Features

- Automated data ingestion from DWD, ERA5/Copernicus, LfU Bayern, and CAMELS-DE
- SPEI-3 and SPEI-12 calculation pipeline
- LSTM (PyTorch) vs. Random Forest (scikit-learn) model comparison
- SHAP-based explainability for feature importance
- Interactive Streamlit dashboard for regional drought visualization

---

## Data Sources

| Source | Data | Access |
|---|---|---|
| [DWD Open Data](https://opendata.dwd.de) | Temperature, precipitation (stations) | Free, `wetterdienst` API |
| [Copernicus ERA5](https://cds.climate.copernicus.eu) | Evapotranspiration, ET₀ (gridded) | Free account + `cdsapi` |
| [LfU Bayern](https://www.lfu.bayern.de) | Groundwater levels | Free, CSV / REST |
| [CAMELS-DE](https://doi.org/10.5281/zenodo.7755276) | Catchment attributes, runoff | Free, Zenodo download |

> **Note:** All data sources have their own license terms. Please refer to each provider's terms before redistribution. ERA5 data is subject to the [Copernicus License](https://cds.climate.copernicus.eu/api/v2/terms/static/licence-to-use-copernicus-products.pdf).

---

## Project Structure

```
drought-risk-bavaria/
│
├── data/
│   ├── raw/                  # Downloaded source data (not tracked by git)
│   ├── processed/            # Harmonized, resampled datasets
│   └── features/             # Feature store (Parquet / NetCDF)
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_spei_calculation.ipynb
│   ├── 03_model_lstm.ipynb
│   └── 04_model_rf_shap.ipynb
│
├── src/
│   ├── ingestion/            # Download scripts per data source
│   │   ├── dwd.py
│   │   ├── era5.py
│   │   ├── lfu.py
│   │   └── camels.py
│   ├── preprocessing/        # Harmonization, resampling, SPEI
│   │   ├── harmonize.py
│   │   └── spei.py
│   ├── models/               # LSTM and Random Forest implementations
│   │   ├── lstm.py
│   │   └── random_forest.py
│   └── dashboard/            # Streamlit app
│       └── app.py
│
├── tests/
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

---

## Quickstart

### 1. Clone & install

```bash
git clone https://github.com/<your-org>/drought-risk-bavaria.git
cd drought-risk-bavaria
pip install -r requirements.txt
```

### 2. Set up CDS API credentials

Create `~/.cdsapirc`:

```
url: https://cds.climate.copernicus.eu/api/v2
key: <your-uid>:<your-api-key>
```

### 3. Download data

```bash
python src/ingestion/dwd.py
python src/ingestion/era5.py
python src/ingestion/lfu.py
python src/ingestion/camels.py
```

### 4. Run preprocessing & SPEI calculation

```bash
python src/preprocessing/harmonize.py
python src/preprocessing/spei.py
```

### 5. Train models

```bash
python src/models/lstm.py
python src/models/random_forest.py
```

### 6. Launch dashboard

```bash
streamlit run src/dashboard/app.py
```

---

## Tech Stack

| Category | Libraries |
|---|---|
| Data wrangling | `pandas`, `xarray`, `geopandas` |
| Climate data | `wetterdienst`, `cdsapi`, `climate-indices` |
| ML | `scikit-learn`, `PyTorch` |
| Explainability | `shap` |
| Visualization | `matplotlib`, `plotly`, `streamlit` |

---

## Model Comparison

| Model | Strengths | Limitations |
|---|---|---|
| LSTM | Captures temporal dependencies | Requires more data, less interpretable |
| Random Forest | Fast, interpretable via SHAP | Limited temporal memory |

Target metric: **RMSE** and **Pearson r** on SPEI-3 and SPEI-12.

---

## Roadmap

- [x] Project setup & data source identification
- [ ] Automated ingestion pipeline
- [ ] SPEI calculation & validation
- [ ] LSTM baseline model
- [ ] Random Forest + SHAP analysis
- [ ] Streamlit dashboard
- [ ] Potential cooperation with LfU Bayern / DWD

---

## Contributing

This is a personal project. Feel free to open issues or pull requests.

---

## License

This project is licensed under the **GNU Affero General Public License v3.0 (AGPL-3.0)** — see [LICENSE](LICENSE) for details.  
Any derivative work, including server-side usage, must be released under the same license.  
Data sources retain their respective licenses (see table above).

---

## Acknowledgements

- [DWD](https://www.dwd.de) for open climate data
- [Copernicus Climate Change Service](https://climate.copernicus.eu) for ERA5
- [LfU Bayern](https://www.lfu.bayern.de) for groundwater data
- [CAMELS-DE](https://doi.org/10.5281/zenodo.7755276) — Klingler et al. (2023)
