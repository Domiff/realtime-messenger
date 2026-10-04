from datetime import datetime, timezone
from typing import Annotated

from pydantic import BaseModel, ConfigDict, PlainSerializer


def as_utc(value: datetime) -> str:
    if value.tzinfo is None:
        value = value.replace(tzinfo=timezone.utc)
    return value.isoformat()


UTCDatetime = Annotated[datetime, PlainSerializer(as_utc, return_type=str)]


class BaseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)


class DateTimeSchema(BaseModel):
    created_at: UTCDatetime
    updated_at: UTCDatetime
