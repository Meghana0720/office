from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from services.employee_service import EmployeeService
from schemas.employee import EmployeeCreate, EmployeeResponse, EmployeeDeleteResponse
from typing import List

class EmployeeController:
    
    @staticmethod
    def add_employee(db: Session, employee_data: EmployeeCreate) -> EmployeeResponse:
        """Add new employee with validation"""
        # Check if email already exists
        existing_employee = EmployeeService.get_employee_by_email(db, employee_data.employee_email)
        if existing_employee:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Employee with email '{employee_data.employee_email}' already exists"
            )
        
        # Create new employee
        employee = EmployeeService.create_employee(db, employee_data)
        return EmployeeResponse.model_validate(employee)
    
    @staticmethod
    def get_employees(db: Session) -> List[EmployeeResponse]:
        """Get all employees"""
        employees = EmployeeService.get_all_employees(db)
        return [EmployeeResponse.model_validate(emp) for emp in employees]
    
    @staticmethod
    def delete_employee(db: Session, employee_id: int) -> EmployeeDeleteResponse:
        """Delete employee by ID"""
        # Check if employee exists
        employee = EmployeeService.get_employee_by_id(db, employee_id)
        if not employee:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Employee with id {employee_id} not found"
            )
        
        # Delete employee
        EmployeeService.delete_employee(db, employee_id)
        return EmployeeDeleteResponse(
            message="Employee deleted successfully",
            deleted_id=employee_id
        )