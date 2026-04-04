from wetterdienst.provider.dwd.observation import DwdObservationRequest
from wetterdienst import Settings

from datetime import datetime
from dateutil.relativedelta import relativedelta

# Get the date two months ago 
end_date = datetime.now() - relativedelta(months=1)
end_date_str = end_date.strftime("%Y-%m-%d")

request = DwdObservationRequest(
    parameter=["temperature_air_mean_2m", "precipitation_height"],
    resolution="monthly",
    start_date="2000-01-01",
    end_date=end_date_str,
    settings=Settings(ts_shape="long")
).filter_by_bbox(
    lat_min=47.2, lat_max=50.6,   # Bayern
    lon_min=8.9,  lon_max=13.8
)

df = request.values.all().df
