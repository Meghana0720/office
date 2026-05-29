from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from db.config import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    employee_name = Column(String(100), nullable=False)
    employee_role = Column(String(100), nullable=False)
    employee_email = Column(String(100), unique=True, nullable=False, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def to_dict(self):
        return {
            "id": self.id,
            "employee_name": self.employee_name,
            "employee_role": self.employee_role,
            "employee_email": self.employee_email,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }

    def __repr__(self):
        return f"<Employee(name={self.employee_name}, email={self.employee_email})>"