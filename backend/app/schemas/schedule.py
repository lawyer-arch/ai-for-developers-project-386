from pydantic import BaseModel, Field


class AvailabilityResponse(BaseModel):
    id: int
    days: str
    start_time: str
    end_time: str
    specific_date: str | None = None

    model_config = {"from_attributes": True}


class ScheduleBase(BaseModel):
    name: str = Field(min_length=1, max_length=255)
    time_zone: str = "Europe/Moscow"


class ScheduleCreate(ScheduleBase):
    pass


class ScheduleResponse(ScheduleBase):
    id: int
    owner_id: int
    availability: list[AvailabilityResponse] = []

    model_config = {"from_attributes": True}


class AvailabilityCreate(BaseModel):
    days: str  # JSON array stored as string: "[0,1,2,3,4]"
    start_time: str  # "HH:MM"
    end_time: str  # "HH:MM"
    specific_date: str | None = None
