"""
crear_attendance()
obtener_attendance()
listar_attendances()
"""
from datetime import date

from pydantic import EmailStr
from sqlmodel import Session, select
from sqlmodel.sql._expression_select_cls import SelectOfScalar

from app.database import engine
from app.models.attendance import Attendance


def crear_attendance(
    nombre:str,
    email:EmailStr,
    event_type:str,
    event_date:date
    ) -> Attendance:
    
    with Session(bind=engine) as session:
        
        nuevo_evento: Attendance = Attendance(
            full_name= nombre,
            email=email,
            event_type=event_type,
            event_date= event_date
        )

        session.add(instance=nuevo_evento)
        session.commit()
        session.refresh(instance=nuevo_evento)

        return nuevo_evento


def obtener_attendance_por_id(
    id: int
    ) -> Attendance | None:
    
    with Session(bind=engine) as session:
        sentencia_id: SelectOfScalar[Attendance] = select(Attendance).where(
            Attendance.id == id
        )

        attendance_id: Attendance | None = session.exec(
            statement=sentencia_id
        ).first()

        return attendance_id