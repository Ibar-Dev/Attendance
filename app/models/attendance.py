from datetime import date
from uuid import UUID, uuid4

from pydantic import EmailStr
from sqlmodel import Field, SQLModel


class Attendance(SQLModel, table=True):
    __tablename__ = "attendances"

    id: int | None = Field(
        default=None,
        primary_key=True,
    )

    guid: UUID = Field(
        default_factory=uuid4,
        unique=True,
        index=True,
    )

    full_name: str = Field(
        min_length=2,
        max_length=50,
        index=True,
    )

    email: EmailStr = Field(
        index=True,
    )

    event_type: str = Field(
        min_length=3,
        max_length=50,
    )

    event_date: date = Field()

    bench: bool = Field(
        default=False,
    )