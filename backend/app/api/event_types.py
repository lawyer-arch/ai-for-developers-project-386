from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db import get_db
from app.models.event_type import EventType
from app.schemas.event_type import EventTypeCreate, EventTypeResponse

router = APIRouter(prefix="/api/v1/event-types", tags=["Event Types"])


@router.post("", response_model=EventTypeResponse, status_code=201)
async def create_event_type(body: EventTypeCreate, db: AsyncSession = Depends(get_db)) -> EventType:
    event_type = EventType(**body.model_dump(), owner_id=1)  # TODO: get from auth
    db.add(event_type)
    await db.commit()
    await db.refresh(event_type)
    return event_type


@router.get("", response_model=list[EventTypeResponse])
async def list_event_types(db: AsyncSession = Depends(get_db)) -> list[EventType]:
    result = await db.execute(select(EventType).where(EventType.owner_id == 1))  # TODO: auth
    return list(result.scalars().all())


@router.get("/{event_type_id}", response_model=EventTypeResponse)
async def get_event_type(event_type_id: int, db: AsyncSession = Depends(get_db)) -> EventType:
    result = await db.execute(select(EventType).where(EventType.id == event_type_id))
    event_type = result.scalar_one_or_none()
    if not event_type:
        raise HTTPException(status_code=404, detail="Event type not found")
    return event_type
