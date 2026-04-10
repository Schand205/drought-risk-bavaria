from wetterdienst.provider.dwd.observation import DwdObservationRequest
from wetterdienst import Settings

import pandas as pd

from datetime import datetime
from dateutil.relativedelta import relativedelta

from pathlib import Path

# path relativ to working directory
data_folder = Path("../../data/raw")
file_save_name = data_folder / "temp_and_precept_height.csv"


# Get the date two months ago 
end_date_raw = datetime.now() - relativedelta(months=1)
end_date_str = end_date_raw.strftime("%Y-%m-%d")

settings = Settings(
    ts_shape="long",
    ts_humanize=True,
    ts_convert_units=True
)

# sequence: (lon_min, lat_min, lon_max, lat_max)
bbox = (8.9, 47.2, 13.8, 50.6)  # Bayern

request = DwdObservationRequest(
    parameters=[
        ("monthly", "climate_summary", "temperature_air_mean_2m"),
        ("monthly", "climate_summary", "precipitation_height"),
    ],
    start_date="2000-01-01",
    end_date=end_date_str,
    settings=Settings(ts_shape="long")
).filter_by_bbox(*bbox)

df = request.values.all().df    # .df is a polars df

df.write_csv(file_save_name)
