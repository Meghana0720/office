from sqlalchemy.orm import Session
from models.employee import Employee
from schemas.employee import EmployeeCreate
from typing import List, Optional

class EmployeeService:
    
    @staticmethod
    def create_employee(db: Session, employee: EmployeeCreate) -> Employee:
        """Create a new employee in database"""
        db_employee = Employee(
            employee_name=employee.employee_name.strip(),
            employee_role=employee.employee_role.strip(),
            employee_email=employee.employee_email.lower().strip()
        )
        db.add(db_employee)
        db.commit()
        db.refresh(db_employee)
        return db_employee
    
    @staticmethod
    def get_all_employees(db: Session) -> List[Employee]:
        """Get all employees ordered by creation date (newest first)"""
        return db.query(Employee).order_by(Employee.created_at.desc()).all()
    
    @staticmethod
    def get_employee_by_email(db: Session, email: str) -> Optional[Employee]:
        """Get employee by email address"""
        return db.query(Employee).filter(Employee.employee_email == email.lower()).first()
    
    @staticmethod
    def get_employee_by_id(db: Session, employee_id: int) -> Optional[Employee]:
        """Get employee by ID"""
        return db.query(Employee).filter(Employee.id == employee_id).first()
    
    @staticmethod
    def delete_employee(db: Session, employee_id: int) -> bool:
        """Delete employee by ID"""
        employee = db.query(Employee).filter(Employee.id == employee_id).first()
        if employee:
            db.delete(employee)
            db.commit()
            return True
        return False