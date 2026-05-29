from pydantic import BaseModel, EmailStr, Field, ConfigDict
from datetime import datetime
from typing import Optional

class EmployeeBase(BaseModel):
    employee_name: str = Field(..., min_length=2, max_length=100, description="Employee full name")
    employee_role: str = Field(..., min_length=2, max_length=100, description="Employee job role")
    employee_email: EmailStr = Field(..., description="Valid email address")

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeResponse(EmployeeBase):
    id: int
    created_at: Optional[datetime] = None
    
    model_config = ConfigDict(from_attributes=True)

class EmployeeDeleteResponse(BaseModel):
    message: str
    deleted_id: int