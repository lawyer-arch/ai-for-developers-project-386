from datetime import datetime

from pydantic import BaseModel, Field


class EventTypeBase(BaseModel):
    title: str = Field(min_length=1, max_length=255)
    slug: str = Field(min_length=1, max_length=255, pattern=r"^[a-z0-9-]+$")
    description: str | None = Field(default=None, max_length=2048)
    length: int = Field(ge=1)
    slot_interval: int = Field(default=15, ge=1)
    minimum_booking_notice: int = Field(default=120, ge=0)
    before_event_buffer: int = Field(default=0, ge=0)
    after_event_buffer: int = Field(default=0, ge=0)
    requires_confirmation: bool = False
    location: str | None = Field(default=None, max_length=512)
    schedule_id: int | None = None


class EventTypeCreate(EventTypeBase):
    pass


class EventTypeResponse(EventTypeBase):
    id: int
    owner_id: int
    created_at: datetime

    model_config = {"from_attributes": True}
