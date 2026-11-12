from datetime import date
from uuid import UUID, uuid4

from pydantic import EmailStr
from sqlmodel import Field, SQLModel


#* Esta clase es la que usaremos para asignar a una persona a una reunion o evento. Por lo tanto cada reunion o evento tendran un identificador unico pero los demas datos si puede repetirse porque es posible que una misma persona este convocada a varios eventos.
class Attendance(SQLModel, table=True):
    __tablename__= "attendances"  # pyright: ignore[reportAssignmentType]

    id: int | None = Field( #identificador interno BD
        default=None,
        primary_key=True,
    )

    guid: UUID = Field( #identificador externo API
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
        default=True,
    )