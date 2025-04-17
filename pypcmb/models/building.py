from dataclasses import dataclass

@dataclass
class BuildingSection:
    type: str  # 'wall', 'roof', 'floor'
    area: float  # m^2
    orientation: str  # 'N', 'S', 'E', 'W'
    insulation_level: float  # R-value
    exposure_to_sunlight: float  # 0.0 to 1.0

@dataclass
class BuildingProfile:
    climate_zone: str
    sections: list[BuildingSection]
