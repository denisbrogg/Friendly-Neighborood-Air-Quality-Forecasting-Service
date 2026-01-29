import yaml
from pydantic import BaseModel


class AirQualityForecastingServiceConfig(BaseModel):
    city: str
    street: str
    aqicn_id: str
    aqicn_data_path: str

    @classmethod
    def from_yaml(cls, file_path: str) -> "Config":
        with open(file_path, "r") as f:
            data = yaml.safe_load(f)
        return cls(**data)
