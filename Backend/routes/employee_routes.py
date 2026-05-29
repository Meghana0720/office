from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from controllers.employee_controller import EmployeeController
from schemas.employee import EmployeeCreate, EmployeeResponse, EmployeeDeleteResponse
from typing import List
from db.config import get_db

router = APIRouter(prefix="/api/employees", tags=["Employees"])

@router.post(
    "/",
    response_model=EmployeeResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Add a new employee"
)
def add_employee(
    employee: EmployeeCreate,
    db: Session = Depends(get_db)
):
    """Create a new employee record"""
    return EmployeeController.add_employee(db, employee)

@router.get(
    "/",
    response_model=List[EmployeeResponse],
    summary="Get all employees"
)
def get_employees(
    db: Session = Depends(get_db)
):
    """Retrieve all employees from database"""
    return EmployeeController.get_employees(db)

@router.delete(
    "/{employee_id}",
    response_model=EmployeeDeleteResponse,
    summary="Delete an employee"
)
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db)
):
    """Delete an employee by ID"""
    return EmployeeController.delete_employee(db, employee_id)